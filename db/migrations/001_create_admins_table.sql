CREATE TABLE admins IF NOT EXISTS {
    id serial primary key,
    name varchar,
    password varchar,
    created_at timestamp,
    updated_at timestamp
};