from config.database import get_connection


class UserDAO:

    def create_table(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                role VARCHAR(20) DEFAULT 'USER'
            )
        """)

        connection.commit()
        connection.close()

    def register_user(self, name, email, password):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (name, email, password)
        )

        connection.commit()
        connection.close()

        print("User registered successfully!")
    def login_user(self, email, password):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email = %s AND password = %s",
            (email, password)
        )

        user = cursor.fetchone()

        connection.close()

        return user
    def get_users(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users")

        users = cursor.fetchall()

        connection.close()

        return users