from service.cart_service import CartService


class CartController:

    def __init__(self):
        self.cart_service = CartService()

    def add_to_cart(self, user_id):
        print("\n--- Add to Cart ---")

        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))

        self.cart_service.add_to_cart(
            user_id,
            product_id,
            quantity
        )

        print("Product added to cart!")

    def view_cart(self, user_id):
        print("\n--- Your Cart ---")

        cart_items = self.cart_service.get_cart(user_id)

        if not cart_items:
            print("Cart is empty.")
            return

        total = 0

        for item in cart_items:
            print(
                "Cart ID:", item[0],
                "| Product:", item[2],
                "| Price:", item[3],
                "| Quantity:", item[4],
                "| Subtotal:", item[5]
            )

            total += item[5]

        print("-------------------------")
        print("Total:", total)