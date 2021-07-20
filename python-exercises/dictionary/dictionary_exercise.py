"""
These are exercises for dictionary
"""


def calculate_total_pricelist(price_list, *orders):
    result = dict()

    for order in orders:
        for product in order:
            ((name, num),) = product.items()
            if name in result:
                result[name] += price_list[name] * num
            else:
                result[name] = price_list[name] * num
    print(result)


def update_delivery_quantity(orders, delivery_order):
    for order in orders:
        for delivery in delivery_order:
            if order["product"] == delivery["product"]:
                order["delivered_qty"] += delivery["delivered_qty"]

    print(orders)


def get_consolidated_order_list(orders):
    consolidated_order_list = dict()

    for order in orders:

        # Check if that order contains unique product if yes update the ordered quantity otherwise create
        # a new entry for dictionary
        if order["product"] not in consolidated_order_list:
            consolidated_order_list[order["product"]] = order
        else:
            consolidated_order_list[order["product"]]["ordered_qty"] += order[
                "ordered_qty"
            ]

    print(list(consolidated_order_list.values()))


if __name__ == "__main__":

    # Exercise 1
    order_1 = [{"PowerCore": 1}, {"PowerLine": 1}]
    order_2 = [{"PowerLine": 2}]
    order_3 = [{"PowerCore": 1}, {"PowerPort": 2}]

    price_list = {"PowerCore": 790000, "PowerLine": 200000, "PowerPort": 750000}

    calculate_total_pricelist(price_list, order_1, order_2, order_3)

    # Exercise 2
    order = [
        {"product": "PowerCore", "ordered_qty": 2, "delivered_qty": 0},
        {"product": "PowerLine", "ordered_qty": 5, "delivered_qty": 0},
        {"product": "PowerPort", "ordered_qty": 3, "delivered_qty": 0},
    ]

    delivery_order = [
        {"product": "PowerCore", "delivered_qty": 2},
        {"product": "PowerLine", "delivered_qty": 3},
    ]

    update_delivery_quantity(order, delivery_order)

    # Exercise 3
    order = [
        {
            "product": "PowerCore",
            "ordered_qty": 2,
        },
        {
            "product": "PowerLine",
            "ordered_qty": 5,
        },
        {
            "product": "PowerPort",
            "ordered_qty": 3,
        },
        {
            "product": "PowerCore",
            "ordered_qty": 1,
        },
        {
            "product": "PowerPort",
            "ordered_qty": 1,
        },
    ]

    get_consolidated_order_list(order)
