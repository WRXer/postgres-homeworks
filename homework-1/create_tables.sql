-- SQL-команды для создания таблиц
create table employees
(
	employee_id int primary key,
	first_name varchar(50) not null,
	last_name varchar(50) not null,
	title varchar(100) not null,
	birth_date date not null,
	notes text not null
);

CREATE TABLE customers
(
	customer_id varchar(5) PRIMARY KEY,
	company_name varchar(50) NOT NULL,
	contact_name varchar(50) NOT NULL
);

create table orders
(
	order_id int primary key,
	customer_id varchar(5) references customers(customer_id),
	employee_id int references employees(employee_id) not null,
	order_date date not null,
	ship_city varchar(25) not null
);

SELECT * FROM orders;
SELECT * FROM employees;
SELECT * FROM customers;