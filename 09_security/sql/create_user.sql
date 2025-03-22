CREATE TABLE
    users (
        id SERIAL PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    );

INSERT INTO
    users (username, password)
VALUES
    ('alice', 'pass123'),
    ('bob', 'hunter2'),
    ('charlie', 'qwerty'),
    ('diana', 'letmein'),
    ('edward', 'admin123'),
    ('frank', 'welcome'),
    ('grace', 'password1'),
    ('hannah', 'monkey'),
    ('ian', 'abc123'),
    ('julia', 'trustno1');