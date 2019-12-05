create database library default CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
use library;

create table user(
   user_no int primary key auto_increment,
   user_id varchar(32) not null,
   user_password varchar(32) not null,
   user_name varchar(32) not null,
   phonenum varchar(12),
   email varchar(32),
   max int
);

create table area(
   area_no int primary key auto_increment,
   category varchar(32) not null
);

create table book_detail(
   book_no int primary key auto_increment,
   area_no int,
   title varchar(32) not null,
   subtitle varchar(32) not null,
   publisher varchar(32) not null,
   published_date datetime,
   author varchar(32) not null, -- 저자가 여러명인 경우 어떻게 할까? 저자테이블 추가하거나, 그냥 놔두거나
   foreign key (area_no) references area(area_no)
);

create table book (
   book_unique_no varchar(32) primary key,
   book_no int,
   `condition` varchar(10) not null,
   foreign key (book_no) references book_detail(book_no)
);

create table rental(
   user_no int,
   book_no int,
   rental_date datetime default CURRENT_TIMESTAMP,
   return_date datetime,
   state varchar(10) not null,
   foreign key(user_no) references user(user_no),
   foreign key(book_no) references book_detail(book_no)
   );

create table reservation(
   user_no int,
   book_no int,
   reservation_date datetime,
   foreign key(user_no) references user(user_no),
   foreign key(book_no) references book_detail(book_no)
);

