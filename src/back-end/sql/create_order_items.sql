create table tests.rr_order_items (
    id int NOT NULL AUTO_INCREMENT,
    reservation_id int,
    menu_item_id int,
    count int,
    total_price int,
    comment varchar(200),
    PRIMARY KEY (id)
);