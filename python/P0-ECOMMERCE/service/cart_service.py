from dao.cart_dao import CartDAO


class CartService:

    def __init__(self):
        self.cart_dao = CartDAO()

    def add_to_cart(self, user_id, product_id, quantity):
        self.cart_dao.create_table()

        self.cart_dao.add_to_cart(
            user_id,
            product_id,
            quantity
        )

    def get_cart(self, user_id):
        self.cart_dao.create_table()

        return self.cart_dao.get_cart(user_id)

    def clear_cart(self, user_id):
     self.cart_dao.clear_cart(user_id)