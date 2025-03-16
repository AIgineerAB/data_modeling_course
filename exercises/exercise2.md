# Exercise 2 - normalizing tables

These exercises are for you to learn fundamental concepts in data modeling. Many of them can be done with pen and paper, physical whiteboard or with an ERD software such as Lucidchart and dbdiagram. It is good practice to work analogue as an important part of data modeling is to align various stakeholders with a mix of technical and business knowledge. It is also advised to discuss with your peers as data modeling usually is not done in solitude.

## 0. Ezecream orders

Our beloved ice cream company Ezecream has a Sales table that looks like this

| order_id | order_date | customer_id | customer_name  | customer_address | product_id | product_name | quantity |
| -------- | ---------- | ----------- | -------------- | ---------------- | ---------- | ------------ | -------- |
| 101      | 2024-04-05 | 05          | Ragnar Lodbrok | Kattegatt 3      | 3          | Blåbärsmagi  | 20       |
| 101      | 2024-04-05 | 05          | Ragnar Lodbrok | Kattegatt 3      | 5          | Lakritsdröm  | 15       |
| 101      | 2024-04-05 | 05          | Ragnar Lodbrok | Kattegatt 3      | 1          | Lichipichi   | 35       |
| 105      | 2025-01-10 | 15          | Feliz Fernadu  | Madridugatan 2   | 8          | Gitlass      | 30       |
| ...      | ...        | ...         | ...            | ...              | ...        | ...          | ...      |

a) Find different problems with this table, so that Ezecream will take you in for internship to fix it for them

b) Does this table satisfy 1NF, 2NF? Motivate.

b) Normalize this table to 3NF, make conceptual diagram and relational schema notation for each relation. Relational schema notation is `RelationName(attribute1, attribute2, ...)`

c) Now also add price attribute. Think about what would happen when price increases or decreases.

d) Write SQL code to get the total price for Ragnar Lodbrok. Insert data into your tables and test it out.

## 1. Sakila

Use the same ERD from Sakila as in exercise1 task 3.

a) Is this normalized to 3NF?

b) Lets zoom in to the inventory, explain how it works for tracking films in each stores.

c) Do we have a way to know if a film is rented out or not?

## 2. Revisiting the doctor example

Remember the doctor, hospital and department example from exercise0 and exercise1.

a) Does the design fulfill 3NF, motivate based on the rules for the normal forms.

b) You should have realised from this question in exercise1 0e)

> "Create a few tables manually, insert given data plus some more, and try to manually link foreign keys to primary keys. Can you satisfy that a doctor can work at `several departments and several hospitals?`"

that this creates ambiguity. This can be solved with a ternary relationship, which connects three entities simultaneously. Now make a new iteration for this data model.

c) In your design do you have bridge tables as well in addition to the ternary relationship. Motivate why you should or should not have them.

## 3. Theoretical questions

a) What are the differences between first, second, third normal forms?

b) Can a normalized design still have flaws? Can you come up with example where this might happen?

c) If a > b and b > c, then a > c. What could this pattern be called?

d) When is ternary relationship needed?

e) In general how far do you need to normalize your design?

f) What's the purpose of normalizations?

g) Is a ternary relationship a bridge table

## Glossary

| Glossary                   | Meaning |
| -------------------------- | ------- |
| normalization              |         |
| insertion anomaly          |         |
| update anomaly             |         |
| deletion anomaly           |         |
| normal forms               |         |
| boyce-codd normal form     |         |
| transitive dependency      |         |
| functional dependency      |         |
| ternary relationship       |         |
| composite primary key      |         |
| relational schema notation |         |
| entity constriants         |         |
|                            |         |
|                            |         |
|                            |         |
