from service.product_service import ProductService


class ProductController:

    def __init__(self):
        self.product_service = ProductService()

    def add_product(self):
        print("\n--- Add Product ---")

        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        self.product_service.add_product(name, price, quantity)

    def view_products(self):
        print("\n--- Products ---")

        products = self.product_service.get_products()

        if not products:
            print("No products available.")
            return

        for product in products:
            print(
                "ID:", product[0],
                "| Name:", product[1],
                "| Price:", product[2],
                "| Quantity:", product[3]
            )

    def update_product(self):
        print("\n--- Update Product ---")

        product_id = int(input("Enter product ID: "))
        name = input("Enter new name: ")
        price = float(input("Enter new price: "))
        quantity = int(input("Enter new quantity: "))

        self.product_service.update_product(
            product_id,
            name,
            price,
            quantity
        )

    def delete_product(self):
        print("\n--- Delete Product ---")

        product_id = int(input("Enter product ID: "))

        self.product_service.delete_product(product_id)