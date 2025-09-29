'''
Câu 11: Kiểm tra số nguyên tố
Yêu cầu:
Viết chương trình nhập vào một số, kiểm tra xem số này có phải là số nguyên tố
hay không. Hỏi người dùng có tiếp tục sử dụng hay thoát phần mềm.
'''
print("Chương trình kiểm tra số nguyên tố")

while True:
    # Nhập số nguyên từ người dùng
    num = int(input("Nhập một số: "))

    # Kiểm tra số nguyên tố
    if num < 2:
        print(num, "không phải là số nguyên tố.")
    else:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, "là số nguyên tố.")
        else:
            print(num, "không phải là số nguyên tố.")

    # Hỏi người dùng có tiếp tục hay không
    tiep_tuc = input("Bạn có muốn tiếp tục? (c/k): ")
    if tiep_tuc.lower() != 'c':
        print("Chương trình kết thúc.")
        break
