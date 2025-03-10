CREATE TABLE
    IF NOT EXISTS Customer (
        customer_id SERIAL PRIMARY KEY,
        first_name VARCHAR(50)
    );

SELECT * FROM Customer;