# calc_checksum(input) => input[n] => z1 z2 z3 ... zn => (1*z1 + 2*z2 + 3*z3 + ...... + n*zn) % 10 


list_1 = []
def calc_checksum(input):
    
    for i in range(len(input)):
        list_1.append(int((i + 1) * int(input[i])))
    print(sum(list_1), " % 10 = " , (sum(list_1) % 10))
    
if __name__ == "__main__":
    calc_checksum(input("Give Checknums: "))