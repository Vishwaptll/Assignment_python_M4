#20.Write python program that user to enter only odd numbers, else will raise an exception

class EvenNumberError(Exception):
    def __init__(self, number):
        self.number = number
    
    def __str__(self):
        return f"Error: {self.number} is an even number. Please enter an odd number."

def get_odd_number():
    while True:
        try:
            number = int(input("Enter an odd number: "))
            if number % 2 == 0:
                raise EvenNumberError(number)
            else:
                return number
        except ValueError:
            print("Error: Please enter a valid integer.")
        except EvenNumberError as e:
            print(e)

if __name__ == "__main__":
    try:
        odd_number = get_odd_number()
        print(f"You entered an odd number: {odd_number}")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
