import pymysql


class DBManager():
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost', port=3306, user='root', passwd='', db='library')
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def select(self, query, *args):
        cursor = self.cursor
        cursor.execute(query, args)
        rows = cursor.fetchone()
        return rows

    def selects(self, query, *args):
        cursor = self.cursor
        cursor.execute(query, args)
        rows = cursor.fetchall()
        return rows

    def insert(self, query, *args):
        cursor = self.cursor
        cursor.execute(query, args)
        cursor.commit()

    def inquery_info(self, userid):
        sql = '''
            select 
                user.*,
                count(1) total,
                count(if(datediff(due_date,now())<0,1,null)) overdue
            from user,rental
            where
                user.user_no=rental.user_no
                and rental.return_date is null
                and user.user_id=%s
            group by user.user_no;
        '''
        return self.select(sql, userid)

    def inquery_rental(self, userid, size, page):
        sql = '''
            select rental.rental_no, rental.book_unique_no,
                book_detail.title, book_detail.author, rental.rental_date, rental.due_date, datediff(now(), due_date) overdue,
                ifnull(datediff(now(), rental_date)*100 / datediff(due_date,rental_date), "100") percent, rental.note
            from user, rental, book_detail, book
            where user.user_no = rental.user_no
                and book.book_unique_no = rental.book_unique_no
                and book.book_no = book_detail.book_no
                and user.user_id = %s
                and rental.return_date is null
            limit %s,%s;
        '''
        return self.selects(sql, userid, size * (page-1), size)

    def inquery_overdue(self, userid):
        sql = '''
            select datediff(now(), rental.due_date)
            from rental,user
            where
                user.user_no = rental.user_no
                and datediff(now(), rental.due_date) > 0 -- 연체 1일 이상인것
                and user.user_id = %s
                and rental.return_date is null;
        '''
        return self.selects(sql, userid)