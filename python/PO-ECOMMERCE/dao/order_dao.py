from config.database import get_connection


class OrderDAO:

    def create_tables(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id INT PRIMARY KEY AUTO_INCREMENT,
                user_id INT NOT NULL,
                total_amount DECIMAL(10,2) NOT NULL,
                status VARCHAR(30) DEFAULT 'PLACED',
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS order_items (
                order_item_id INT PRIMARY KEY AUTO_INCREMENT,
                order_id INT NOT NULL,
                product_id INT NOT NULL,
                quantity INT NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                FOREIGN KEY (order_id) REFERENCES orders(order_id),
                FOREIGN KEY (product_id) REFERENCES products(product_id)
            )
        """)

        connection.commit()
        connection.close()

    def create_order(self, user_id, total_amount):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO orders (user_id, total_amount)
            VALUES (%s, %s)
            """,
            (user_id, total_amount)
        )

        order_id = cursor.lastrowid

        connection.commit()
        connection.close()

        return order_id

    def add_order_item(self, order_id, product_id, quantity, price):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO order_items
            (order_id, product_id, quantity, price)
            VALUES (%s, %s, %s, %s)
            """,
            (order_id, product_id, quantity, price)
        )

        connection.commit()
        connection.close()

    def get_orders(self, user_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT order_id, total_amount, status
            FROM orders
            WHERE user_id = %s
            """,
            (user_id,)
        )

        orders = cursor.fetchall()

        connection.close()

        return orders