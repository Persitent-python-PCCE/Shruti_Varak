import csv

category_revenue = {}
product_quantity = {}

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        category = row["category"]
        quantity = int(row["quantity"])
        price = float(row["unit_price"])

        revenue = quantity * price

        if category in category_revenue:
            category_revenue[category] = category_revenue[category] + revenue
        else:
            category_revenue[category] = revenue

        if product in product_quantity:
            product_quantity[product] = product_quantity[product] + quantity
        else:
            product_quantity[product] = quantity

    print("Category Revenue:", category_revenue)

    top_product = max(product_quantity, key=product_quantity.get)

    print("Top-selling product:", top_product)
    print("Quantity:", product_quantity[top_product])