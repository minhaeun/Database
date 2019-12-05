-- request (request_no, user_no, title, publisher, author, request_date, state)
insert into request
    (user_no, title, publisher, author, request_date, state)
    VALUES (1, 'book title', 'publisher', 'author', CURRENT_TIMESTAMP, '신청중')

-- 신청중, 접수중, 