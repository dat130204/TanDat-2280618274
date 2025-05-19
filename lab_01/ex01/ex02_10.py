def dao_nguoc_chuoi(chuoi):
    return chuoi[:: -1]
input_string = input("Mời nhập chuổi cần đảo ngược: ")
print("Chuổi đảo ngược là:", dao_nguoc_chuoi(input_string))