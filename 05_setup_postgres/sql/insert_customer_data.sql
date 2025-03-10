SET
    search_path TO ezecream_05;

INSERT INTO
    customer (first_name, last_name, address, email)
VALUES
    (
        'Ragnar',
        'Lothbrok',
        '1 Valhalla Way',
        'ragnar@kattegat.com'
    ),
    (
        'Lagertha',
        'Lothbrok',
        '2 Shieldmaiden Road',
        'lagertha@kattegat.com'
    ),
    (
        'Bjorn',
        'Ironside',
        '3 Viking Bay',
        'bjorn@kattegat.com'
    ),
    (
        'Ivar',
        'the Boneless',
        '4 The Great Heathen Army Camp',
        'ivar@danes.com'
    );

SELECT
    *
FROM
    customer;