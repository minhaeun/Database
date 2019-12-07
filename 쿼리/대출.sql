-- book_detail(book_no,area_no, title, author, publisher, published_date)
-- book((book_unique_no, book_no, condition )

-- 서적 검색
select book_detail.book_no, area.category, book_detail.title, book_detail.author, book_detail.publisher, book_detail.published_date
from book_detail, area
where area.area_no = book_detail.area_no
    and book_detail.title like '%?%'

-- 서적 상세조회
select book.book_unique_no, book.condition, book.book_no from book where book.book_no = 86421;

-- 대출처리
update book set condition='대여중' where book_unique_no=%s
insert into rental (user_no, book_unique_no, rental_date, due_date, note) VALUES (%s, %s, %s, date_add(%s,interval %s day), '')

-- 반납처리
update book set condition='대여가능' where book_unique_no=%s;
update rental set return_date=%s
    where userno=%s and book_unique_no=%s;

-- 연장처리
update rental set due_date=date_add(due_date,interval %s day) where rental_no=%s;
