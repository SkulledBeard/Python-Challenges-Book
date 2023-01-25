#roman numbers to decilmal number
# I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000

    
def from_roman_number(roman_number):
    
    dec_number = []
    for i in range(len(roman_number)):
        match roman_number[i]:
            case "M":
                dec_number.append(1000)
            case "D":
                dec_number.append(500)
            case "C":
                dec_number.append(100)
            case "L":
                dec_number.append(50)
            case "X":
                dec_number.append(10)
            case "V":
                dec_number.append(5)
            case "I":
                dec_number.append(1)
            case _:
                print("Wrong input: " + roman_number[i])
                
    for i in range(len(dec_number)-1, 1, -1):
        if dec_number[i-1] < dec_number[i]:
            dec_number[i-1] = dec_number[i] - dec_number.pop(i-1)
            
    print(sum(dec_number))


if __name__ == "__main__":
    from_roman_number(input("Input roman Number:"))