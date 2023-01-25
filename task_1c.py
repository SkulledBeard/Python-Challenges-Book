#is_even(n) is_odd(n) check if number is even or odd

    
def is_even(number):
    return (number%2 == 0)

def is_odd(number):
    return (number%2 != 0)
    

if __name__ == "__main__":
    input_first = int(input("Number to check: "))
    
    if is_even(input_first):
        print("The number is even!")
    elif is_odd(input_first):
        print("The number is odd!")
        