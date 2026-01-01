# Exercise 1 - going in to logical and physical data modeling

These exercises are for you to learn fundamental concepts in data modeling. Many of them can be done with pen and paper, physical whiteboard or with an ERD software such as Lucidchart and dbdiagram. It is good practice to work analogue as an important part of data modeling is to align various stakeholders with a mix of technical and business knowledge. It is also advised to discuss with your peers as data modeling usually is not done in solitude.

## 0. Library Bookly
Going back to the library exercise from [exercise0, task 0](https://github.com/AIgineerAB/data_modeling_course/blob/main/exercises/exercise0.md), now build the logical and physical models upon the conceptual model that you have bulit. Your conceptual model includes these entities: Book, Member and Borrow (where a borrow event is the transaction of a libray).

When building your logical and physical models, consider these more detailed requirements:
- There can be more than one copy of a book
- For each borrow, member can borrow more than one book copy

Also, think about how the models can be affected if the stakeholders require the database to store also data about (you don't need to update your models but just suggest briefly how the models should be changed):
- Librarians
- Reservation
- Publishers
- Book Categories


## 1. Hospital example
The json data below represent data of three table: Hospital, Department and Doctor. 

```json
{
  "hospital": "Sjukhusstock",
  "address": "Drottninggatan 3, Stockholm",
  "departments": [
    {
      "name": "Kardiologi",
      "doctors": [
        { "id": 1, "name": "Dr. Abra Abrahamson" },
        { "id": 2, "name": "Dr. Erika Eriksson" }
      ]
    },
    {
      "name": "Neurologi",
      "doctors": [{ "id": 3, "name": "Dr. Sven Svensson" }]
    }
  ]
}
```

a) Can you draft three tables and covert these json data into rows of respective tables. 

b) This is the conceptual data model after we've added the composite entities to take care of many-to-many relationships. We will build the logical and physical models upon it. 

<img src="https://github.com/kokchun/assets/blob/main/data_modeling/conceptual_hospital.png?raw=true" alt="hospital conceptual" width="500">

From the relationship cardinalities on the diagram, can you describe the business rules of this hospital system, for instance, are doctors allowed to work in multiple hospitals and departments?

c) Create a logical data model using lucidcharts

d) Identify different keys on the various entities

e) Identify child entities and parent entities. What makes them into parent/child relationships?

f) Create a physical data model using dbdiagram

g) Create a few tables manually, insert given data plus some more, and try to manually link foreign keys to primary keys. Can you satisfy that a doctor can work at several departments and several hospitals?

## 2. Implement hospital example in postgres

a) Now implement your physical model from e) and add the data below. Make sure that you have correctly specified different column constraints.

b) Now lets try to add a row in HospitalDepartment with a hospital_id that doesn't exist in the hospital table. What happens here and why?

c) Do similar to b) but try adding a department_id to HospitalDepartment that doesn't exist in the Department.

d) Now try to do normal delete a record in Hospital that the HospitalDepartment refers to. What happens?

e) Now use delete on cascade and check what happens.

f) Try to violate a column constraint, what did you try and what result did you get?

## 3. Identify keys

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

d) Create another table with a primary key where one of the columns in this table could act as a foreign key. For instance, you can create a table with more information about each avdelning. 

## 4. Sakila exercise

In SQL course we have queried the sakila database a lot to learn various concepts such as joining, union, filtering. Now lets [download it from kaggle](https://www.kaggle.com/datasets/atanaskanev/sqlite-sakila-sample-database?resource=download) and try to understand its data model.

Study the ERD and try to answer the following questions 

a) Is this a conceptual, logical or physical ERD, motivate?

b) How many entities are in the database?

c) Which are the composite entities?

d) Try to find suitable relationship labels between entities

e) Try to write out some possible relationship statements between the entities.

f) Can you find if there is any errors/mistakes in this ERD? 


## 5. Theoretical questions

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

e) What does composite key mean and when do you use it?

f) What is dbml used for? 

## Glossary

| Glossary                | Meaning |
| ----------------------- | ------- |
| composite entity        |         |
| constraint              |         |
| primary key             |         |
| foreign key             |         |
| bridge table            |         |
| attributes              |         |
| referential integrity   |         |
| child entity            |         |
| parent entity           |         |
| natural key             |         |
| surrogate key           |         |
| candidate key           |         |
| alternate key           |         |
