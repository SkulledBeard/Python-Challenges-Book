#perfekt number / sum of divider is the number

    
def calc_perfect_numbers(max_exclusive):
    list_perfect_numbers = []
    list_divider= []
    
    for i in range(1, max_exclusive):
        for j in range(1,i):
            if (i%j) == 0:
                list_divider.append(j)
        
        if sum(list_divider) == i:
            list_perfect_numbers.append(i)
            
        list_divider.clear()
            
    print(list_perfect_numbers)

if __name__ == "__main__":                
    calc_perfect_numbers(int(input("Max Number (exclude): ")))