-- create schema
CREATE SCHEME IF NOT EXISTS INK_STORE;

-- create and populate tables
create table if not exists INK_STORES.CUSTOMERS
(
    customer_key int primary key,
    prefix varchar(3),
    first_name varchar(255),
    last_name varchar(255),
    birth_month date,
    marital_status char(1),
    gender char(1),
    email_address varchar(255),
    annual_income int,
    total_children int,
    educational_level varchar(50),
    occupation varchar(255),
    home_owner char(1)
);

COPY INK_STORE.CUSTOMERS ("customer key", prefix, "first name", "last name", "birth month", "marital status", gender, "email address", "annual income", "total children", "educational level", occupation, "home owner")
FROM '/data/customers.csv' DELIMITER ',' CSV HEADER;