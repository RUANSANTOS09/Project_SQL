create database bookstore;
use bookstore;

create table authors(
    author_id int not null auto_increment,
    name varchar(255) not null,
    nationality varchar(255) not null,
    primary key (author_id)
);

alter table authors add birth_date date;

create table books(
    book_id int not null auto_increment,
    title varchar(255) not null,
    price decimal(10,2) not null,
    authors_id int not null,
    primary key (book_id),
    foreign key (authors_id) references authors(author_id)
);

alter table books add stock int;


insert into authors (name, nationality, birth_date)
     values('Ruan', 'Brazil', '2008-06-05'), 
           ('Jake', 'Estados Unidos', '1999-05-02');

insert into books (title, price, authors_id)
     values('Rapido e Devagar', 60.49, 1),
           ('Habitos atomicos', 87.99, 2),
           ('A mente milionária', 45.50, 2);

update books
set stock = 10
where book_id = 10;

update books 
set stock = 200
where book_id = 11;

update books 
set stock = 150 
where book_id = 12;