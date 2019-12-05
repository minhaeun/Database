-- 회원조회(대여중인 책), 사용자 정보, 대여번호, 책 제목, 책 unique번호,
-- 대여내용(+연체내용)
select user.user_name, user.phonenum, rental.rental_no, rental.book_unique_no,
    book_detail.title, book_detail.author, rental.rental_date, rental.due_date, datediff(now(), due_date) overdue,
    ifnull(datediff(now(), rental_date)*100 / datediff(due_date,rental_date), "100") percent 
from user, rental, book_detail, book
where user.user_no = rental.user_no
    and book.book_unique_no = rental.book_unique_no
    and book.book_no = book_detail.book_no
    and user.user_id = 'biccon'
    and rental.return_date is null;

-- 연체내용
select datediff(now(), rental.due_date)
from rental,user
where
    user.user_no = rental.user_no
    and datediff(now(), rental.due_date) > 0 -- 연체 1일 이상인것
    and user.user_id = 'biccon'
    and rental.return_date is null;

-- 반납처리
