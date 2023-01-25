# calc_sum_and_count_all_numbers_div_by_2_or_7(max_exclusive)

def calc_sum_and_count_all_numbers_div_by_2_or_7(max_exclusive : int):
    list_2 = []
    list_7 = []
    for i in range(1, max_exclusive - 1):
        if i % 2 == 0:
            list_2.append(i)
        elif i % 7 == 0:
            list_7.append(i)
            
    #print count and sum
    
    print("Count % 2: ", len(list_2))
    print("Numbers % 2: ", list_2)
    
    print("Count % 7: ", len(list_7))
    print("Numbers % 7: ", list_7)
    
    print("Sum count: ", (len(list_7) + len(list_2)))
    print("Sum numbers: ", (sum(list_2) + sum(list_7)))
    

if __name__ == "__main__":
    calc_sum_and_count_all_numbers_div_by_2_or_7(int(input("Max Range (exclude): ")))