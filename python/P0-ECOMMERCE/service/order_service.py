from dao.order_dao import OrderDAO


class OrderService:

    def __init__(self):
        self.order_dao = OrderDAO()

    def create_order(self, user_id, total_amount):
        self.order_dao.create_tables()

        return self.order_dao.create_order(
            user_id,
            total_amount
        )

    def add_order_item(self, order_id, product_id, quantity, price):
        self.order_dao.add_order_item(
            order_id,
            product_id,
            quantity,
            price
        )

    def place_order(self, user_id, cart_items, total_amount):

        order_id = self.create_order(
            user_id,
            total_amount
        )

        for item in cart_items:

            product_id = item[0]
            quantity = item[1]
            price = item[2]

            self.add_order_item(
                order_id,
                product_id,
                quantity,
                price
            )

        return order_id

    def get_orders(self, user_id):
        self.order_dao.create_tables()

        return self.order_dao.get_orders(user_id)