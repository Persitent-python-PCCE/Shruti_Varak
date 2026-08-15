from config.database import get_connection


class ProductDAO:

    def create_table(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                quantity INT NOT NULL
            )
        """)

        connection.commit()
        connection.close()

    def add_product(self, name, price, quantity):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)",
            (name, price, quantity)
        )

        connection.commit()
        connection.close()

        print("Product added successfully!")

    def get_products(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM products")

        products = cursor.fetchall()

        connection.close()

        return products

    def update_product(self, product_id, name, price, quantity):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE products
            SET name = %s, price = %s, quantity = %s
            WHERE product_id = %s
            """,
            (name, price, quantity, product_id)
        )

        connection.commit()
        connection.close()

        print("Product updated successfully!")

    def delete_product(self, product_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM products WHERE product_id = %s",
            (product_id,)
        )

        connection.commit()
        connection.close()

        print("Product deleted successfully!")