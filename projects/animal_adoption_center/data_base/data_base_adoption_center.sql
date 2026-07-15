create database animal_adoption_center;
use animal_adoption_center;

create table animals(
    animals_id int not null auto_increment,
    name varchar(255) not null,
    species varchar(255) not null,
    age int not null,
    sex varchar(255) not null,
    primary key (animals_id)
);

create table adopters(
    adopters_id int not null auto_increment,
    name varchar(255) not null,
    email varchar(255) not null,
    primary key (adopters_id)
);

alter table adopters
add constraint unique_email
unique(email);


create table adoptions(
    adoptions_id int not null auto_increment,
    adopters_id int not null,
    animals_id int not null,
    adoption_date date not null,
    primary key (adoptions_id),
    foreign key (adopters_id) references adopters(adopters_id),
    foreign key (animals_id) references animals(animals_id)
);


insert into animals(name, species, age, sex)
     values('Max', 'Cachorro', 5, 'Male'),
           ('Luna', 'Gato', 2, 'Female'),
           ('Thor', 'Cachorro', 1, 'Male'),
           ('Mel', 'Coelho', 3, 'Female'),
           ('Nina', 'Papagaio', 2, 'Female');

insert into adopters(name, email)
          values('Ruan', 'ru@gmail.com'),
                ('Isabella', 'isa@gmail.com'),
                ('Reginaldo', 're@gmail.com'),
                ('Gabriela', 'ga@gmail.com'),
                ('Isabelly', 'isab@gmail.com');

insert into adoptions(adopters_id, animals_id, adoption_date)
     values(3,3, '2026-12-01'),
           (4,4, '2026-10-02'),
           (5,5, '2026-01-31');