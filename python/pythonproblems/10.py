def inventory_report(inventory, gst=0.05, **filters):

    # 1. Unique categories
    categories = set()

    for item in inventory:
        categories.add(item[1])

    print("Categories:", sorted(categories))


    # 2. Low stock using filter()
    def check_stock(item):
        return item[2] < 10

    low_stock = list(filter(check_stock, inventory))

    low_stock_names = []

    for item in low_stock:
        low_stock_names.append(item[0])

    print("Reorder:", low_stock_names)


    # 3. Prices with GST using map()
    def add_gst(item):
        return (item[0], item[3] * (1 + gst))

    prices = dict(map(add_gst, inventory))

    print("Prices incl. GST:", prices)


    # 4. Apply filters
    matches = []

    for item in inventory:

        if "category" in filters:
            if item[1] != filters["category"]:
                continue

        if "max_price" in filters:
            if item[3] > filters["max_price"]:
                continue

        matches.append(item[0])

    print("Matching filters", filters, ":", matches)

    return matches


inv = [
    ("Masala Chai", "Tea", 5, 20),
    ("Green Tea", "Tea", 15, 30),
    ("Samosa", "Snack", 8, 15),
    ("Biscuit", "Snack", 25, 10)
]

inventory_report(inv, category="Snack", max_price=15)