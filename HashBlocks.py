def main():
    num = int(input("Enter Shape Size Number: "))
    generate_blocks(num)

def generate_blocks(n):
    for i in range(n):
        for j in range(n):
            print("#", end="")
        print()
main()