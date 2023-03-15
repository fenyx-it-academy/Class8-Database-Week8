# Class8-Database-Week8

- **Note:** In order to create your ER diagrams, you can use dbdesigner, pgadmin, lucidchart or any other tool you like. In order to learn how to generate in pgAdmin, you can also check this article: https://medium.com/geekculture/creating-a-sql-entity-relationship-diagram-erd-ced5ad1239d0

## 1. Entity Relationship Diagram - Company

Your task is to design and describe the database of a company.

- You are working in a IT company where multiple small teams deliver one product each. Every member of a team have a responsibilitiy (title) such as product owner, backend developer, frontend developer, data engineer etc. Also each product is being developed for a different customer, and these customers are serving within different domains. Your task is to design and create a database where you can handle (store and retrieve) all these information.

Your tasks:

- Choose your entities, write down their attributes.

- Create tables for these entities according to normalization rules.

- Explain the relationships between entities.

- Create an entity relationship diagram where you display all these information graphically.

Below is an example ERD. Try to come up with a similar end result. Good luck!

![erd-sample](https://user-images.githubusercontent.com/45574672/201494999-f67ed2ac-d1d5-4d06-9dfb-ba205eb7828e.png)


## 2. Import ERD 

- Import the company ERD created in exercise 1 to pgAdmin 

## 3. Import Pagila DB with data

- Create the Pagila DB in your pgAdmin.
- Import the Pagila DB to your pgAdmin. First create the tables by running following SQL query https://github.com/devrimgunduz/pagila/blob/master/pagila-schema.sql and then import the data with this one https://github.com/devrimgunduz/pagila/blob/master/pagila-insert-data.sql
- Generate ERD for this database from pgAdmin.
- Explore this database.

## 4. Connect to DB with Python

- Now, connect to this imported Pagila database from python code.
- Select all rows from `actor` table
- Select first row of `category` table
- Select first 50 rows of `address` table

Do the above operations inside python code. (Use `fetchOne()`, `fetchMany()`, `fetchAll()` etc.) 

## 5. Create DB with Python

- Create an empty database named `PyCoders` from your pgAdmin
- Create a file named `exercise5.py`: this file will connect to `PyCoders` database
- After connecting to database:
  - Create a table with name `students`
    - This table will have `student_id` and `name` columns
  - Create a table with name `teachers`
    - This table will have `teacher_id` and `name` columns
  - Now add 3 records for both of these databases.
- You should do all of these inside the python code. 
- After doing these, run `SELECT` queries to get all data from both tables. Print these outputs.

## Hackerrank Questions

- 1. Select All SQL: https://www.hackerrank.com/challenges/select-all-sql/problem
- 2. Weather Observation Station 1: https://www.hackerrank.com/challenges/weather-observation-station-1/problem

