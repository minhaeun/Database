
-- 중복조회
select count(1) from user where user_id=?

-- 회원삽입
insert into user (user_id,user_name,phonenum,email) values (?,?,?,?)
