create table tests.rr_reservation (
    id int NOT NULL AUTO_INCREMENT,
    timestamp varchar(100),
    customer_name varchar(20),
    customer_id int,
    name varchar(20),
    seat_count int,
    table_id int,
    for_date varchar(100),
    for_how_long varchar(100),
    status varchar(100),
    latest_comment varchar(100),
    waiter_id int,
    total_price int,
    tip_percent int,
    PRIMARY KEY (id)
);