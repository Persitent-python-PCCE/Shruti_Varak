from service.order_service import OrderService
from service.cart_service import CartService


class OrderController:

    def __init__(self):
        self.order_service = OrderService()
        self.cart_service = CartService()

    def place_order(self, user_id):

        print("\n--- Place Order ---")

        cart_items = self.cart_service.get_cart(user_id)

        if not cart_items:
            print("Cart is empty.")
            return

        total = 0

        order_items = []

        for item in cart_items:

            product_id = item[1]
            product_name = item[2]
            price = item[3]
            quantity = item[4]
            subtotal = item[5]

            print(
                product_name,
                "| Quantity:", quantity,
                "| Subtotal:", subtotal
            )

            total += subtotal

            order_items.append(
                (product_id, quantity, price)
            )

        print("-------------------------")
        print("Order Total:", total)

        confirm = input("Place order? (yes/no): ")

        if confirm.lower() == "yes":

            order_id = self.order_service.place_order(
                user_id,
                order_items,
                total
            )

            self.cart_service.clear_cart(user_id)

            print("Order placed successfully!")
            print("Order ID:", order_id)

        else:
            print("Order cancelled.")

    def order_history(self, user_id):

        print("\n--- Order History ---")

        orders = self.order_service.get_orders(user_id)

        if not orders:
            print("No orders found.")
            return

        for order in orders:
            print(
                "Order ID:", order[0],
                "| Total:", order[1],
                "| Status:", order[2]
            )