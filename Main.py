from math_function import *


def main():

    data_1 = int(input("Masukkan input 1 :"))
    data_2 = int(input("Masukkan input 2 :"))
    operator = input("Masukkan operator :") 

    if operator == "+":
        result = add(data_1, data_2)
    elif operator == "*":
        result = add(data_1, data_2)
    elif operator == "/":
        result = add(data_1, data_2)
    else:
        print("Operator tidak tersedia, hanya operator penjumlahan (+), perkalianan (*), pembagian (/) yang tersedia")

    print("{} {} {} = {} ".format(data_1, operator, data_2, result))


if __name__ == "__main__":
    print("Hello Main !")
    main()
