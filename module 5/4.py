def get_odd_number():
    while True:
        try:
            number = int(input("Enter an odd number: "))
            if number % 2 != 1:
                raise ValueError("You must enter an odd number.")
            return number
        except ValueError as ve:
            print(ve)

if __name__ == "__main__":
    try:
        odd_number = get_odd_number()
        print(f"Odd number entered: {odd_number}")
    except KeyboardInterrupt:
        print("\nProgram terminated by the user.")
    except Exception as e:
        print(f"An error occurred: {e}")
