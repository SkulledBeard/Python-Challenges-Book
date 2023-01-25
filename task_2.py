# print numbers as text

def numer_as_text(str_number):
    value_to_text = ""
    for i in range(len(str_number)):
    # used in the book
    # remainder = number % 10
            
        if str_number[i] == "0":
            value_to_text = "ZERO"
        
        if str_number[i] == "1":
            value_to_text = "ONE"
        
        if str_number[i] == "2":
            value_to_text = "TWO"
        
        if str_number[i] == "3":
            value_to_text = "THREE"
        
        if str_number[i] == "4":
            value_to_text = "FOUR"
        
        if str_number[i] == "5":
            value_to_text = "FIVE"
        
        if str_number[i] == "6":
            value_to_text = "SIX"
        
        if str_number[i] == "7":
            value_to_text = "SEVEN"
        
        if str_number[i] == "8":
            value_to_text = "EIGHT"
        
        if str_number[i] == "9":
            value_to_text = "NINE"
            
        print(value_to_text, " ")
   
if __name__ == "__main__":
            
    numer_as_text(input("Number to print: "))