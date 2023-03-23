from business.reservation import Reservation


def add(parameters):
    timestamp = parameters['timestamp']
    customer_name = parameters['customer_name']
    customer_id = parameters['customer_id']
    seat_count = parameters['seat_count']
    table_id = parameters['table_id']
    for_date = parameters['for_date']
    for_how_long = parameters['for_how_long']
    status = parameters['status']
    latest_comment = parameters['latest_comment']
    waiter_id = parameters['waiter_id']
    reservation_type = parameters['reservation_type']
    total_price = parameters['total_price']
    tip_percent = parameters['tip_percent']

    reservation = Reservation()
    reservation.set_timestamp(timestamp)
    reservation.set_customer_name(customer_name)
    reservation.set_customer_id(customer_id)
    reservation.set_seat_count(seat_count)
    reservation.set_table_id(table_id)
    reservation.set_for_date(for_date)
    reservation.set_for_how_long(for_how_long)
    reservation.set_status(status)
    reservation.set_latest_comment(latest_comment)
    reservation.set_waiter_id(waiter_id)
    reservation.set_reservation_type(reservation_type)
    reservation.set_total_price(total_price)
    reservation.set_tip_percent(tip_percent)

    result = reservation.add()
    return result


def select_all():
    reservations = Reservation.select_all()
    return reservations


def load(parameters):
    reservation_id = parameters['id']
    reservation = Reservation()
    reservation.load(reservation_id)
    return reservation.to_json()


def update(parameters):
    reservation_id = parameters['id']
    timestamp = parameters['timestamp']
    customer_name = parameters['customer_name']
    customer_id = parameters['customer_id']
    seat_count = parameters['seat_count']
    table_id = parameters['table_id']
    for_date = parameters['for_date']
    for_how_long = parameters['for_how_long']
    status = parameters['status']
    latest_comment = parameters['latest_comment']
    waiter_id = parameters['waiter_id']
    reservation_type = parameters['reservation_type']
    total_price = parameters['total_price']
    tip_percent = parameters['tip_percent']

    reservation = Reservation()
    reservation.load(reservation_id)

    reservation.set_timestamp(timestamp)
    reservation.set_customer_name(customer_name)
    reservation.set_customer_id(customer_id)
    reservation.set_seat_count(seat_count)
    reservation.set_table_id(table_id)
    reservation.set_for_date(for_date)
    reservation.set_for_how_long(for_how_long)
    reservation.set_status(status)
    reservation.set_latest_comment(latest_comment)
    reservation.set_waiter_id(waiter_id)
    reservation.set_reservation_type(reservation_type)
    reservation.set_total_price(total_price)
    reservation.set_tip_percent(tip_percent)

    result = reservation.update()
    return result


def add_order_item(parameters):
    reservation_id = parameters['reservation_id']
    menu_item_id = parameters['menu_item_id']
    count = parameters['count']

    reservation = Reservation()
    reservation.load(reservation_id)
    result = reservation.add_order_item(menu_item_id, count)
    return result


def select_all_order_items(parameters):
    reservation_id = parameters['reservation_id']

    reservation = Reservation()
    reservation.load(reservation_id)
    result = reservation.select_all_order_items()
    return result


def update_order_item(parameters):
    reservation_id = parameters['reservation_id']
    order_item_id = parameters['order_item_id']
    count = parameters['count']

    reservation = Reservation()
    reservation.load(reservation_id)
    result = reservation.update_order_item(order_item_id, count)
    return result


def delete_order_item(parameters):
    reservation_id = parameters['reservation_id']
    menu_item_id = parameters['menu_item_id']

    reservation = Reservation()
    reservation.load(reservation_id)
    result = reservation.delete_order_item(menu_item_id)
    return result
