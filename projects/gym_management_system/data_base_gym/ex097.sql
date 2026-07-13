CREATE database gym;
 use gym;

create table instructors (
    instructors_id int not null auto_increment,
    name varchar(255) not null,
    specialty varchar(255) not null,
    primary key (instructors_id)
);


create table classes (
    class_id int not null auto_increment,
    class_name varchar(255) not null,
    duration_minutes int not null,
    instructor_id int not null,
    primary key (class_id),
    foreign key (instructor_id) references instructors (instructors_id)
);

create table members (
    member_id int not null auto_increment,
    name varchar(255) not null,
    email varchar(255) not null,
    primary key (member_id)
);

alter table members
add constraint unique_email
unique(email);

create table enrollments(
    enrollments_id int not null auto_increment,
    member_id int not null,
    class_id int not null,
    enrollment_date date not null,
    primary key (enrollments_id),
    foreign key (member_id) references members(member_id),
    foreign key (class_id) references classes(class_id) 
);

insert into instructors(name, specialty)
     values('Pedro', 'Musculação'),
           ('Lucas', 'Crossfit');


insert into classes(class_name, duration_minutes, instructor_id)
     values('Spinning', 30, 1),
           ('Yoga Flow', 40, 2);

insert into members(name, email)
     values('Ruan', 'GYMruan@gmail.com'),
           ('Isabella', 'GYMisabella@gmail.com');

insert into enrollments(member_id, class_id, enrollment_date)
       values(1, 1, '2026-06-14'),
             (2, 2, '2026-07-15'),
             (2, 1, '2025-06-17');