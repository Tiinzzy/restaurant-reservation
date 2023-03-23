from business.seating_table import SeatingTable


def add(parameters):
    seat_count = parameters.get('seat_count')
    available = (parameters.get('available') == 'True')
    seating_table = SeatingTable()
    seating_table.set_seat_count(seat_count)
    seating_table.set_available(available)

    result = seating_table.add()
    return {'result': result}


def available_seats(parameters):
    seat_count = parameters.get('seat_count')
    result = SeatingTable.select_available_seats(int(seat_count))
    return result


def select_all():
    result = SeatingTable.select_all_seating_tables()
    return result


def load(parameters):
    seat_id = parameters.get('id')
    table = SeatingTable()
    table.load(seat_id)
    return table.to_json()


def update(parameters):
    seat_id = parameters.get('id')
    available = parameters.get('available')

    table = SeatingTable()
    table.load(seat_id)
    table.set_available(available)

    result = table.update()
    return {'result': result}
