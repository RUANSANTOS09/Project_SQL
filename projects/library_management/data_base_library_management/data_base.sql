create database library_management
use library_management;

create table author(
    author_id int not null auto_increment,
    name varchar(255) not null,
    primary key (author_id)
);


create table book(
    book_id int not null auto_increment,
    name varchar(255) not null,
    primary key (book_id)
);

create table book_authors (
    book_authors_id int not null auto_increment,
    book_id int not null,
    author_id int not null,
    primary key (book_authors_id),
    foreign key(book_id) references book(book_id),
    foreign key(author_id) references author(author_id)
);

create table members (
    members_id int not null auto_increment,
    name varchar(255) not null,
    email varchar(255) not null,
    primary key (members_id)
);

alter table members
add constraint unique_email
unique(email);


create table loan (
    loan_id int not null auto_increment,
    book_id int not null,
    members_id int not null,
    withdrawal_date date not null,
    due_date date not null,
    return_date date,
    primary key (loan_id),
    foreign key (book_id) references book(book_id),
    foreign key (members_id) references members(members_id)
);

insert into author(name)
     values('Machado de Assis'),
           ('George Orwell'),
           ('Antoine de Saint-Exupéry'),
           ('J. K. Rowling'),
           ('J. R. R. Tolkien');

insert into book (name)
     values('Dom Casmurro'),
           ('1984'),
           ('O Pequeno Príncipe'),
           ('Harry Potter e a Pedra Filosofal'),
           ('O Hobbit');

insert into book_authors (book_id, author_id)
     values(1, 1),
           (2,2),
           (3,3),
           (4,4),
           (5,5);

insert into members(name,email)
     values('Ruan', 'ru@gmail.com'),
           ('Isabella', 'isa@gmail.com'),
           ('Reginaldo', 're@gmail.com'),
           ('Gabriela', 'ga@gmail.com'),
           ('Isabelly', 'isab@gmail.com');

insert into loan(book_id, members_id, withdrawal_date, due_date, return_date)
     values(1,1, '2025-06-04', '2025-12-04', '2025-12-01'),
           (2,2, '2025-04-01', '2025-10-01', NULL),
           (3,3, '2025-02-10', '2025-08-10', NULL),
           (4,4, '2025-06-24', '2025-12-24', '2025-12-06'),
           (5,5, '2025-06-04', '2025-12-04', NULL);