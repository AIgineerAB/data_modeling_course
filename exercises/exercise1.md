# Exercise 1 - going in to logical and physical data modeling

These exercises are for you to learn fundamental concepts in data modeling. Many of them can be done with pen and paper, physical whiteboard or with an ERD software such as Lucidchart and dbdiagram. It is good practice to work analogue as an important part of data modeling is to align various stakeholders with a mix of technical and business knowledge. It is also advised to discuss with your peers as data modeling usually is not done in solitude.

## 0. Hospital example

Going back to the hospital exercise from [exercise0, task 1](https://github.com/AIgineerAB/data_modeling_course/blob/main/exercises/exercise0.md), we will build logical and physical data models. This is the conceptual data model after we've added the composite entities to take care of many-to-many relationships.

<img src="https://github.com/kokchun/assets/blob/main/data_modeling/conceptual_hospital.png?raw=true" alt="hospital conceptual" width="500">

a) Create a logical data model using lucidcharts

b) Identify different keys on the various entities

c) Identify child entities and parent entities. What makes them into parent/child relationships?

d) Create a physical data model using dbdiagram

e) Create a few tables manually, insert given data plus some more, and try to manually link foreign keys to primary keys. Can you satisfy that a doctor can work at several departments and several hospitals?

## 1. Implement hospital example in postgres

a) Now implement your physical model from e) and add the data from task 0e). Make sure that you have correctly specified different domain constraints.

b) Now lets try to add a row in HospitalDepartment with a hospital_id that doesn't exist in the hospital table. What happens here and why?

c) Do similar to b) but try adding a department_id to HospitalDepartment that doesn't exist in the Department.

d) Now try to do normal delete a record in Hospital that the HospitalDepartment refers to. What happens?

e) Now use delete on cascade and check what happens.

f) Try to violate a domain constraint, what did you try and what result did you get?

## 2. Identify keys

| EmployeeID | Förnamn | Efternamn | AvdelningID | E-post                       | Telefon     |
| ---------- | ------- | --------- | ----------- | ---------------------------- | ----------- |
| 201        | Erik    | Johansson | 1           | erik.johansson@coolfirma.se  | 070-1234567 |
| 202        | Anna    | Karlsson  | 2           | anna.karlsson@coolfirma.se   | 073-2345678 |
| 203        | Johan   | Andersson | 1           | johan.andersson@coolfirma.se | 072-3456789 |
| 204        | Sara    | Lindgren  | 3           | sara.lindgren@coolfirma.se   | 076-4567890 |
| 205        | Maria   | Svensson  | 2           | maria.svensson@coolfirma.se  | 070-5678901 |


a) Which columns could be candidate keys here?

b) From this set of candidate keys, which one would you choose as primary key and which ones as alternate keys?

c) Is your primary key considered as natural key or surrogate key?

d) Create another table with a primary key where one of the columns in this table could act as a foreign key.

## 3. Sakila exercise

In SQL course we have queried the sakila database a lot to learn various concepts such as joining, union, filtering. Now lets [download it from kaggle](https://www.kaggle.com/datasets/atanaskanev/sqlite-sakila-sample-database?resource=download) and try to understand its data model.

Study the ERD and try to answer the following questions 

a) Is this a conceptual, logical or physical ERD, motivate?

b) How many entities are in the database?

c) Which are the composite entities?

d) Try to find suitable relationship labels between entities

e) Try to write out some possible relationship statements between the entities.

f) Can you find if there is any errors/mistakes in this ERD? 


## 4. Theoretical questions

a) The following constraints are commonly used in RDBMS:

- NOT NULL
- UNIQUE
- CHECK
- DEFAULT
- FOREIGN KEY
- PRIMARY KEY

b) What does the physical modeling have that the logical data model don't have.

c) How do you ensure referential integrity and why is it desirable to have it?

d) How do the cardinality relationships in the modeling actually affect the implementations? 

e) What does domain constraint mean? 

f) What does composite key mean and when do you use it?

g) What is dbml used for? 

## Glossary

| Glossary                | Meaning |
| ----------------------- | ------- |
| composite entity        |         |
| domain                  |         |
| constraint              |         |
| domain constraint       |         |
| entity constraint       |         |
| primary key             |         |
| foreign key             |         |
| bridge table            |         |
| information engineering |         |
| attributes              |         |
| data integrity          |         |
| entity integrity        |         |
| referential integrity   |         |
| relation instance       |         |
| child entity            |         |
| parent entity           |         |
| natural key             |         |
| surrogate key           |         |
| candidate key           |         |
| alternate key           |         |
|                         |         |
