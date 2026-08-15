from controller.user_controller import UserController
from controller.product_controller import ProductController
from controller.cart_controller import CartController
from controller.order_controller import OrderController


def main():

    user_controller = UserController()
    product_controller = ProductController()
    cart_controller = CartController()
    order_controller = OrderController()

    user_id = 1

    while True:

        print("\n===== P0 E-COMMERCE =====")
        print("1. Register")
        print("2. Login")
        print("3. View Products")
        print("4. Add Product")
        print("5. Update Product")
        print("6. Delete Product")
        print("7. Add to Cart")
        print("8. View Cart")
        print("9. Place Order")
        print("10. Order History")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            user_controller.register()

        elif choice == "2":
            user = user_controller.login()

            if user:
                user_id = user[0]

        elif choice == "3":
            product_controller.view_products()

        elif choice == "4":
            product_controller.add_product()

        elif choice == "5":
            product_controller.update_product()

        elif choice == "6":
            product_controller.delete_product()

        elif choice == "7":
            cart_controller.add_to_cart(user_id)

        elif choice == "8":
            cart_controller.view_cart(user_id)

        elif choice == "9":
            order_controller.place_order(user_id)

        elif choice == "10":
            order_controller.order_history(user_id)

        elif choice == "11":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()