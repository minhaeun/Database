-- 예약
insert into reservation (user_no, book_no, reservation_date, `state`) VALUES (
    select user_no from user where user_id='biccon',
    1,
    CURRENT_TIMETSTAMP,
    '예약중'
);


/*
    예약조회
    - 예약중인 사용자별 책 정보
    - 대출 가능한 책의 개수 포함(>0, 대출가능, 대출불가능)
*/
select
    r.reservation_no, 
    r.book_no,
    book_detail.title,
    book_detail.author,
    reservation_date,
    state,
    (select count(1) possible from book,reservation r2
        where book.book_no=r2.book_no and r.reservation_no=r2.reservation_no and `condition`='대여가능') possible_count -- 현재 대여가능한 책 개수
from
    reservation r,
    book_detail,
    user
where user.user_no = r.user_no
    and book_detail.book_no = r.book_no
    and user.user_id = 'biccon'
;

-- 예약 상태는 예약중, 예약완료가 있고, 대여 가능 필드 추가(book_no로 대여 가능한 책 개수 join and count > 0), 