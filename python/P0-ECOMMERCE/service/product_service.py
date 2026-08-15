from dao.product_dao import ProductDAO


class ProductService:

    def __init__(self):
        self.product_dao = ProductDAO()

    def add_product(self, name, price, quantity):
        self.product_dao.create_table()
        self.product_dao.add_product(name, price, quantity)

    def get_products(self):
        self.product_dao.create_table()
        return self.product_dao.get_products()

    def update_product(self, product_id, name, price, quantity):
        self.product_dao.update_product(
            product_id,
            name,
            price,
            quantity
        )

    def delete_product(self, product_id):
        self.product_dao.delete_product(product_id)