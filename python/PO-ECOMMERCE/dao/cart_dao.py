from config.database import get_connection


class CartDAO:

    def create_table(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cart (
                cart_id INT PRIMARY KEY AUTO_INCREMENT,
                user_id INT NOT NULL,
                product_id INT NOT NULL,
                quantity INT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                FOREIGN KEY (product_id) REFERENCES products(product_id)
            )
        """)

        connection.commit()
        connection.close()

    def add_to_cart(self, user_id, product_id, quantity):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO cart (user_id, product_id, quantity)
            VALUES (%s, %s, %s)
            """,
            (user_id, product_id, quantity)
        )

        connection.commit()
        connection.close()

    def get_cart(self, user_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT cart.cart_id,
                cart.product_id,
                products.name,
                products.price,
                cart.quantity,
                products.price * cart.quantity
            FROM cart
            JOIN products
            ON cart.product_id = products.product_id
            WHERE cart.user_id = %s
            """,
            (user_id,)
        )

        cart_items = cursor.fetchall()

        connection.close()

        return cart_items

    def get_cart_for_order(self, user_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT cart.product_id,
                cart.quantity,
                products.price
            FROM cart
            JOIN products
            ON cart.product_id = products.product_id
            WHERE cart.user_id = %s
            """,
            (user_id,)
        )

        items = cursor.fetchall()

        connection.close()

        return items

    def clear_cart(self, user_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM cart WHERE user_id = %s",
            (user_id,)
        )

        connection.commit()
        connection.close()