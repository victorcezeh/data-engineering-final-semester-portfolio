-- create schema
CREATE SCHEMA IF NOT EXISTS INK_STORE;

-- create and populate tables
create table if not exists INK_STORE.CUSTOMERS
(
    customer_key serial primary key,
    prefix varchar(10),
    first_name varchar(255),
    last_name varchar(255),
    birth_month varchar(25),
    marital_status varchar(10),
    gender varchar(10),
    email_address varchar(255),
    annual_income varchar(255),
    total_children int,
    educational_level varchar(50),
    occupation varchar(255),
    home_owner varchar(10)
);

COPY INK_STORE.CUSTOMERS (customer_key, prefix, first_name, last_name, birth_month, marital_status, gender, email_address, annual_income, total_children, educational_level, occupation, home_owner)
FROM '/data/customers.csv' DELIMITER ',' CSV HEADER;