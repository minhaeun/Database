-- 회원 정보
select count(datediff(due_date,now()) < 0) 
from user, rental r
where
    user.user_no = r.user_no
    and r.return_date is null
    and user.user_id = 'biccon'
;

select 
    user.*,
    count(1) total,
    count(if(datediff(due_date,now())<0,1,null)) overdue
from user,rental
where
    user.user_no=rental.user_no
    and rental.return_date is null
    and user.user_id=''
group by user.user_no;


-- 회원조회(대여중인 책), 사용자 정보, 대여번호, 책 제목, 책 unique번호,
-- 대여내용(+연체내용)
select rental.rental_no, rental.book_unique_no,
    book_detail.title, book_detail.author, rental.rental_date, rental.due_date, datediff(now(), due_date) overdue,
    ifnull(datediff(now(), rental_date)*100 / datediff(due_date,rental_date), "100") percent 
from user, rental, book_detail, book
where user.user_no = rental.user_no
    and book.book_unique_no = rental.book_unique_no
    and book.book_no = book_detail.book_no
    and user.user_id = 'biccon'
    and rental.return_date is null;

-- 연체내용
select rental.rental_no, rental.book_unique_no, 
    book_detail.title, book_detail.author, rental.due_date,
    datediff(now(), rental.due_date) overdue
from rental,user, book_detail, book
where
    user.user_no = rental.user_no
    and book.book_unique_no = rental.book_unique_no
    and book.book_no = book_detail.book_no
    and datediff(now(), rental.due_date) > 0 -- 연체 1일 이상인것
    and user.user_id = 'biccon'
    and rental.return_date is null;

-- 반납처리
