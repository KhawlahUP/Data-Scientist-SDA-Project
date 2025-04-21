from calculator import add, subtract, multiply, divide, square, power, sqrt

def show_menu():
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Power")
    print("7. Square Root")
    print("0. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an operation (0-7): ")
        
        if choice == "0":
            print("Goodbye!")
            break

        try:
            if choice in ["1", "2", "3", "4", "6"]:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                if choice == "1":
                    print("Result:", add(a, b))
                elif choice == "2":
                    print("Result:", subtract(a, b))
                elif choice == "3":
                    print("Result:", multiply(a, b))
                elif choice == "4":
                    print("Result:", divide(a, b))
                elif choice == "6":
                    print("Result:", power(a, b))
            elif choice == "5":
                a = float(input("Enter a number: "))
                print("Result:", square(a))
            elif choice == "7":
                a = float(input("Enter a number: "))
                print("Result:", sqrt(a))
            else:
                print("Invalid choice. Please select from the menu.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
