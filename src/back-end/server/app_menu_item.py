from business.menu_item import MenuItem


def update(parameters):
    menu_item_id = parameters['id']
    name = parameters['name']
    category = parameters['category']
    price = parameters['price']
    description = parameters['description']

    menu_item = MenuItem()
    menu_item.load(menu_item_id)

    menu_item.set_name(name)
    menu_item.set_price(price)
    menu_item.set_category(category)
    menu_item.set_description(description)

    result = menu_item.update()
    return result
