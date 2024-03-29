from business.menu_item import MenuItem


def add(parameters):
    name = parameters.get('name')
    category = parameters.get('category')
    price = parameters.get('price')
    description = parameters.get('description')

    menu_item = MenuItem()
    menu_item.set_name(name)
    menu_item.set_price(price)
    menu_item.set_category(category)
    menu_item.set_description(description)

    result = menu_item.add()
    return {'result': result}


def delete(parameters):
    menu_item_id = parameters.get('id')

    menu_item = MenuItem()
    menu_item.load(menu_item_id)

    result = menu_item.delete()
    return {'result': result}


def load(parameters):
    menu_item_id = parameters.get('id')
    menu_item = MenuItem()
    menu_item.load(menu_item_id)
    return menu_item.to_json()


def update(parameters):
    menu_item_id = parameters.get('id')
    name = parameters.get('name')
    category = parameters.get('category')
    price = parameters.get('price')
    description = parameters.get('description')

    menu_item = MenuItem()
    menu_item.load(menu_item_id)

    menu_item.set_name(name)
    menu_item.set_price(price)
    menu_item.set_category(category)
    menu_item.set_description(description)

    result = menu_item.update()
    return {'result': result}


def select_all():
    menu_items = MenuItem.select_all_menu_items()
    return menu_items


def categories():
    category = MenuItem.get_categories()
    return category

def truncate():
    result = MenuItem.truncate()
    return {'result': result}
