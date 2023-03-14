menu_sql = """
create table tests.rr_menu_items (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(200),
    category varchar(200),
    price int,
    description varchar(200),
    PRIMARY KEY (id)
);
"""

order_sql = """
create table tests.rr_order_items (
    id int NOT NULL AUTO_INCREMENT,
    reservation_id int,
    menu_item_id int,
    count int,
    total_price int,
    comment varchar(200),
    PRIMARY KEY (id)
);
"""

reservation_sql = """
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
"""

roles_sql = """
create table tests.rr_roles (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(100),
    PRIMARY KEY (id)
);
"""

seating_sql = """
create table tests.rr_seating_tables (
    id int NOT NULL AUTO_INCREMENT,
    seat_count int,
    available varchar(20),
    PRIMARY KEY (id)
);
"""

user_roles_sql = """
create table tests.rr_user_roles (
    user_id int,
    role_id int
);
"""

users_sql = """
create table tests.rr_user (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(200),
    lastName varchar(200),
    email varchar(200),
    password varchar(200),
    birthday varchar(200),
    PRIMARY KEY (id)
);
"""