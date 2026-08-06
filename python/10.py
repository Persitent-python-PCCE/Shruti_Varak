def inventory_report(inventory, gst=0.05, **filters):

    categories = sorted(set(item[1] for item in inventory))
    print("Categories:", categories)

    low_stock = list(filter(lambda item: item[2] < 10, inventory))
    print("[!] Reorder soon (stock < 10):", [item[0] for item in low_stock])

    prices = dict(map(lambda item: (item[0], round(item[3] * (1 + gst), 2)), inventory))
    print("Prices incl. GST:", prices)

    matches = inventory

    if "category" in filters:
        matches = list(filter(lambda item: item[1] == filters["category"], matches))

    if "max_price" in filters:
        matches = list(filter(lambda item: item[3] <= filters["max_price"], matches))

    result = [item[0] for item in matches]

    print(f"Matching filters {filters}:", result)

    return result


inv = [
    ("Masala Chai", "Tea", 5, 20),
    ("Green Tea", "Tea", 15, 30),
    ("Samosa", "Snack", 8, 15),
    ("Biscuit", "Snack", 25, 10),
]

inventory_report(inv, category="Snack", max_price=15)

