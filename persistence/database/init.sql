create table if not exists houses (
    id integer,
    name integer,
    points integer,
    primary key (id)
);

create table if not exists students (
    id integer,
    first_name text,
    last_name text,
    house_id integer,
    primary key (id),
    foreign key (house_id) references houses(id)
);

-- add houses
insert into houses (name, points)
values (0, 0);
insert into houses (name, points)
values (1, 0);
insert into houses (name, points)
values (2, 0);
insert into houses (name, points)
values (3, 0);

-- add students
insert into students (first_name, last_name, house_id) values ('Isabella', 'Thornwood', 1);
insert into students (first_name, last_name, house_id) values ('Lucas', 'Pendragon', 1);
insert into students (first_name, last_name, house_id) values ('Lily', 'Nightshade', 2);
insert into students (first_name, last_name, house_id) values ('Oliver', 'Moonstone', 2);
insert into students (first_name, last_name, house_id) values ('Emily', 'Blackwood', 3);
insert into students (first_name, last_name, house_id) values ('Jasper', 'Ravenscroft', 3);
insert into students (first_name, last_name, house_id) values ('Sophia', 'Wilderidge', 4);
insert into students (first_name, last_name, house_id) values ('Ethan', 'Ironhart', 4);
insert into students (first_name, last_name, house_id) values ('Mia', 'Emberly', 2);
insert into students (first_name, last_name, house_id) values ('Finley', 'Silverthorn', 1);

-- extend student with spellcrafting things
alter table students
add student_level integer;

create table if not exists spells (
    id integer,
    name text,
    complexity integer,
    damage integer,
    min_level integer,
    description text,
    primary key (id)
);

insert into spells (name, complexity, damage, min_level, description) VALUES ('Expelliarmus', 1, 5, 1, 'Disarm the opponent');
insert into spells (name, complexity, damage, min_level, description) VALUES ('Stupefy', 2, 10, 1, 'Stun the opponent');
insert into spells (name, complexity, damage, min_level, description) VALUES ('Reducto', 3, 15, 2, 'Incapitates the opponent');
insert into spells (name, complexity, damage, min_level, description) VALUES ('Petrificus Totalus', 3, 17, 3, 'Immobilize the opponent');