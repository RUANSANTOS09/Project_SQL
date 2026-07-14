create database delivery;

use delivery;

create table restaurant(
    restaurant_id int not null auto_increment,
    name varchar(255) not null,
    primary key (restaurant_id)
);

create table dishes(
    dishes_id int not null auto_increment,
    name varchar(255) not null,
    restaurant_id int not null,
    price decimal(10,2) not null,
    primary key (dishes_id),
    foreign key (restaurant_id) references restaurant(restaurant_id)
);


create table customer(
    customer_id int not null auto_increment,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    email varchar(255) not null,
    primary key (customer_id)
);

alter table customer
add constraint unique_email
unique(email);

create table address(
    address_id int not null auto_increment,
    name varchar(255) not null,
    primary key (address_id)
);


create table orders(
    order_id int not null auto_increment,
    restaurant_id int not null,
    customer_id int not null,
    address_id int not null,
    primary key (order_id),
    foreign key (restaurant_id) references restaurant(restaurant_id),
    foreign key (customer_id) references customer(customer_id),
    foreign key (address_id) references address(address_id)
);

create table order_items(
    order_items_id int not null auto_increment,
    order_id int not null,
    dishes_id int not null,
    amount int not null,
    price_at_order decimal(10,2) not null,
    primary key (order_items_id),
    foreign key (dishes_id) references dishes(dishes_id),
    foreign key (order_id) references orders(order_id)
);

insert into restaurant(name)
     values('Coco Bambu'),
           ('Outback Steakhouse Brasil'),
           ('Madero'),
           ('Paris 6'),
           ('Fogo de Chão');

insert into dishes(name, restaurant_id, price)
     values('Camarão Internacional', 1, 220.00),
           ('Camarão Coco Bambu', 1, 250.00),
           ('Ribs on the Barbie', 2, 100.00),
           ('Alice Springs Chicken', 2, 85.00),
           ('Cheeseburguer Madero', 3, 55.00),
           ('L Entrecôte Madero', 3, 95.00),
           ('Grand Gateau', 4, 50.00),
           ('Risoto de Camarão', 4, 90.00),
           ('Picanha', 5, 120.00),
           ('Costela bovina', 5, 110.00);
insert into customer(first_name, last_name, email)
     values('Ruan', 'Santos', 'rs@gmail.com'),
           ('Isabella', 'Almeida', 'ia@gmail.com'),
           ('Reginaldo', 'Almeida', 'ra@gmail.com'),
           ('Gabriela', 'Almeida', 'ga@gmail.com'),
           ('Isabelly', 'Santos', 'isa@gmail.com');

insert into address(name)
     values('Rua 76, Casa 01 Pinheiros'),
           ('Rua 16, Casa 09 Sitio cercado'),
           ('Rua 76, Casa 97 Itaim Bibi'),
           ('Rua 76, Casa 97 Itaim bibi'),
           ('Rua L, Casa 14 Jardim Europa');

insert into orders(restaurant_id, customer_id, address_id)
     values(1, 2, 4),
           (2, 1, 1),
           (3, 3, 2),
           (4, 4, 3),
           (5, 5, 5);

insert into order_items(order_id, dishes_id, amount, price_at_order)
     values(1, 1, 4, 880.00),
           (2, 2, 2, 500.00),
           (3, 3, 1, 100.00),
           (4, 4, 1, 85.00),
           (5, 5, 2, 110.00);