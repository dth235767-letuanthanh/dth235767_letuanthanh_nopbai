'''
Câu 10: Tính dãy số
Yêu cầu:
Cho biểu thức toán học sau:
Tính S(x,n) = x + x^2/2! + x^3/3! + ... + x^n/n!
Viết chương trình cho phép nhập x, n và xuất ra kết quả của biểu thức.'''
print("Chương trình tính biểu thức S(x, n) = x + x^2/2! + x^3/3! + ... + x^n/n!")

# Nhập x và n
x = float(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n (n >= 1): "))

# Kiểm tra n hợp lệ
if n < 1:
    print("n phải lớn hơn hoặc bằng 1")
else:
    S = 0
    giaithua = 1  # Biến lưu giá trị n! để tái sử dụng

    for i in range(1, n + 1):
        giaithua *= i         # Tính i! (giai thừa)
        S += x**i / giaithua  # Cộng vào tổng

    print("Giá trị của biểu thức S(x, n) là:", round(S, 6))
