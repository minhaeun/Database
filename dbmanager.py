import pymysql


class DBManager():
    def __init__(self):
        self.conn = pymysql.connect(
            host='192.168.0.18', port=3306, user='root', passwd='', db='library', autocommit=True)

    def select(self, query, *args):
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query, args)
        rows = cursor.fetchone()
        return rows

    def selects(self, query, *args):
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query, args)
        rows = cursor.fetchall()
        return rows

    def insert(self, query, *args):
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        return cursor.execute(query, args)
        # cursor.commit()

    def inquery_info(self, userid):
        sql = '''
            select 
                user.*,
                count(if(return_date is null,1,null)) total,
                count(if((datediff(due_date,now())<0) and (return_date is null),1,null)) overdue
            from user,rental
            where
                user.user_no=rental.user_no
                and user.user_id=%s
            group by user.user_no;
        '''
        return self.select(sql, userid)

    def inquery_rental(self, userid, size, page):
        sql = '''
            select rental.rental_no, rental.book_unique_no,
                book_detail.title, book_detail.author, cast(rental.rental_date as date) rental_date, cast(rental.due_date as date) due_date, datediff(now(), due_date) overdue,
                ifnull(datediff(now(), rental_date)*100 / datediff(due_date,rental_date), "100") percent, rental.note
            from user, rental, book_detail, book
            where user.user_no = rental.user_no
                and book.book_unique_no = rental.book_unique_no
                and book.book_no = book_detail.book_no
                and user.user_id = %s
                and rental.return_date is null
            limit %s, %s;
        '''
        return self.selects(sql, userid, size * (page-1), size)

    def inquery_reservation(self, userid):
        sql = '''
            select
                r.reservation_no, 
                r.book_no,
                book_detail.title,
                book_detail.author,
                cast(reservation_date as date) reservation_date,
                state,
                (select count(1) possible from book,reservation r2
                    where book.book_no=r2.book_no and r.reservation_no=r2.reservation_no and `condition`='대여가능') possible_count -- 현재 대여가능한 책 개수
            from
                reservation r,
                book_detail,
                user
            where user.user_no = r.user_no
                and book_detail.book_no = r.book_no
                and user.user_id = %s
                and state = '예약중'
            ;
        '''
        return self.selects(sql, userid)
    
    def return_book(self, rental_no, book_unique_no):
        sql = '''
            update rental set return_date=CURRENT_TIMESTAMP
                where rental_no=%s;
        '''
        self.insert(sql, rental_no)

        sql = '''
            update book set `condition`='대여가능' where book_unique_no=%s;
        '''
        self.insert(sql, book_unique_no)
        

    def extend_book(self, rental_no):
        sql = '''
            update rental set due_date=date_add(due_date,interval %s day) where rental_no=%s;
        '''
        self.insert(sql, 5, rental_no)

    def rental_book(self, reservation_no, user_no, book_no):
        sql = '''
            select book_unique_no from book
            where 
                book_no = %s
                and `condition`='대여가능'
            order by book_unique_no asc
            limit 1;
        '''
        row = self.select(sql, book_no)
        if(row is not None):
            book_unique_no = row['book_unique_no']
            sql = '''
                update book set `condition`='대여중' where book_unique_no=%s;
            '''
            self.insert(sql, book_unique_no)
            sql = '''
                insert into rental (user_no, book_unique_no, rental_date, due_date, note) VALUES (%s, %s, CURRENT_TIMESTAMP, date_add(CURRENT_TIMESTAMP,interval %s day), '')
            '''
            self.insert(sql, user_no, book_unique_no, 5)
            sql = '''
                update reservation set `state`='예약완료' where reservation_no=%s
            '''
            self.insert(sql, reservation_no)
            return 0
        else:
            return -1
        # book_no로 대여 안되어있는 book_unique_no 하나 찾아서 대여처리

    def request_book(self, title, area_no, publisher, published_date, author):
        sql = '''
            insert into book_detail (area_no, title, publisher, published_date, author) VALUES (%s, %s, %s, %s, %s )
        '''
        return self.insert(sql, area_no, title, publisher, published_date, author)

    def inquery_category(self):
        sql = '''
            select * from area
        '''
        return self.selects(sql)

     
    def search_book(self, title, size, page):
        sql = '''
            select
                book_detail.*,
                count(if(book.condition='대여가능' and book.book_unique_no,1,NULL)) count
            from
                book_detail
            left outer join
                book
            on
                book.book_no = book_detail.book_no
            where
                book_detail.title like %s
            group by book_detail.book_no
            limit %s, %s
            ;
        '''
        return self.selects(sql, "%"+title+"%", size * (page-1), size)