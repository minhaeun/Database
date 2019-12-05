-- %캠핑%이 포함된 책을 도서관에서 구매했다고 insert 하주기
insert into book (book_no,`condition`) select book_no,'대여가능' from book_detail where title like '%캠핑%';

-- 책 검사
select book_unique_no