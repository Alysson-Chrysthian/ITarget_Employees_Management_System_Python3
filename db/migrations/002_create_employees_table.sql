CREATE TABLE employees IF NOT EXISTS {
    id serial primary key,
    name varchar,
    email varchar, 
    cpf varchar,
    registration varchar,
    gender varchar,
    street varchar,
    linguee varchar,
    number int,
    cep varchar,
    birthday timestamp,
    created_at timestamp,
    updated_at timestamp
};