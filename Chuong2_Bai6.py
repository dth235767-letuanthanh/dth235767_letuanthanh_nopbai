'''
Câu 6: Trình bày ý nghĩa toán tử /, //, %, **, and, or, is
'''# Toán tử chia thực (/): Kết quả là số thực
x = 7 / 3  # 2.3333333333333335
print(x)

# Toán tử chia lấy phần nguyên (//): Kết quả là số nguyên
y = 7 // 3  # 2
print(y)

# Toán tử lấy phần dư (%): Kết quả là phần dư của phép chia
z = 7 % 3  # 1
print(z)

# Toán tử lũy thừa (**): Tính số mũ
a = 2 ** 3  # 8
print(a)

# Toán tử logic "and": Kiểm tra xem cả hai điều kiện đều đúng không
b = (5 > 3) and (10 > 5)  # True
print(b)

# Toán tử logic "or": Kiểm tra xem ít nhất một điều kiện đúng không
c = (5 < 3) or (10 > 5)  # True
print(c)

# Toán tử "is": Kiểm tra xem hai đối tượng có cùng địa chỉ bộ nhớ
d = [1, 2, 3]
e = d
f = [1, 2, 3]
print(d is e)  # True, vì e và d cùng trỏ đến một đối tượng
print(d is f)  # False, vì f là một đối tượng khác mặc dù giá trị giống d
