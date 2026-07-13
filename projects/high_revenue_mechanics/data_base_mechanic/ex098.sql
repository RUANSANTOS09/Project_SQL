create database mechanic;

use mechanic;

create table customer(
    customer_id int not null auto_increment,
    name varchar(255) not null,
    email varchar(255) not null,
    primary key (customer_id)
);

alter table customer
add constraint unique_customer
unique(email);

create table vehicles(
    vehicles_id int not null auto_increment,
    model varchar(255) not null,
    problem_description varchar(255) not null,
    plate varchar(255) not null,
    customer_id int not null,
    primary key (vehicles_id),
    foreign key (customer_id) references customer(customer_id)
);

alter table vehicles
add constraint unique_plate
unique(plate);

create table mechanic(
    mechanic_id int not null auto_increment,
    name varchar(255) not null,
    primary key (mechanic_id)
);

create table services_performed(
    services_performed_id int not null auto_increment,
    services varchar(255) not null,
    mechanic_id int not null,
    vehicles_id int not null,
    price decimal(10,2) not null,
    service_date date not null,
    primary key (services_performed_id),
    foreign key(mechanic_id) references mechanic(mechanic_id),
    foreign key(vehicles_id) references vehicles(vehicles_id)
);

insert into customer(name, email)
     values('Ruan', 'ruan@gmail.com'),
           ('Isabella', 'isabella@gmail.com'),
           ('Gabriela', 'gabriela@gmail.com'),
           ('Reginaldo', 'reginaldo@gmail.com'),
           ('Isabelly', 'isabelly@gmail.com');

insert into vehicles(model, problem_description, plate, customer_id)
     values('Lamborghini Urus', 'Desgaste dos freios', 'GDF-890', 1),
           ('GTR-R35', 'Superaquecimento da transmissão', 'HGT-098', 2),
           ('Ferrari 458 Italia', 'Problemas na suspensão', 'HJY-756', 3),
           ('Lamborghini Aventador', 'Superaquecimento da transmissão ISR','FTD-739', 4),
           ('Ferrari Purosangue', 'Vazamento de óleo', 'BAM-158', 5);

insert into mechanic(name)
     values('Pedro'),
           ('Luan'),
           ('Leticia'),
           ('Maicon'),
           ('Valdemir'),
           ('Alexandre'),
           ('Alexa');

insert into services_performed(services, mechanic_id, vehicles_id, price, service_date)
      values('Troca dos discos e pastilhas de freio', 7, 1, 45000, '2028-03-28'),
            ('Manutenção do arrefecimento da transmissão', 3, 2, 12000, '2029-01-18'),
            ('Reparo da suspensão', 5, 3, 25000, '2029-11-08'),
            ('Manutenção da refrigeração da transmissão', 2, 4, 35000, '2027-07-30'),
            ('Reparo do vazamento de óleo', 1, 5, 18000, '2034-02-10');





