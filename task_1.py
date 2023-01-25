# func calc(m,n) => m * n => / 2 => % 7

def calc(m, n):
    return ((m * n) / 2) % 7

if __name__ == "__main__":
    print(calc(int(input("First Numeber:")), int(input("Second Number:"))))