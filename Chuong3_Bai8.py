'''
Câu 8: Nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’ . Hãy xuất kết quả theo
đúng phép toán đã nhập.
'''
print("Chương trình thực hiện phép tính đơn giản")

# Nhập vào 2 số
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

# Nhập phép toán
operator = input("Nhập phép toán (+, -, *, /): ")

# Thực hiện phép toán
if operator == '+':
    result = a + b
    print("Kết quả:", result)
elif operator == '-':
    result = a - b
    print("Kết quả:", result)
elif operator == '*':
    result = a * b
    print("Kết quả:", result)
elif operator == '/':
    if b != 0:
        result = a / b
        print("Kết quả:", result)
    else:
        print("Lỗi: Không thể chia cho 0")
else:
    print("Phép toán không hợp lệ")
