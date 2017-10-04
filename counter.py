import sys

def count_on_bits(number):
    onbits = 0
    n = int(number)
    while n != 0:
        n = n & (n - 1)
        onbits += 1

    return onbits

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Give me just one num\nand I'll count its bits\nbut if you keep mum\nthen that's it, I quits!")
        quit()
    
    print(count_on_bits(sys.argv[1]))