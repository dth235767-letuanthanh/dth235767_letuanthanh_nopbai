'''
Câu 7: Trình bày một số cách nhập dữ liệu từ bàn phím.
'''
# 1. Nhập một chuỗi
name = input("Nhập tên của bạn: ")  # Nhập tên dưới dạng chuỗi
print(f"Chào {name}!")  # In ra tên người dùng

# 2. Nhập một số nguyên và chuyển kiểu dữ liệu
age = int(input("Nhập tuổi của bạn: "))  # Chuyển chuỗi thành số nguyên
print(f"Tuổi của bạn là {age} năm.")  # In ra tuổi

# 3. Nhập một số thực và chuyển kiểu dữ liệu
height = float(input("Nhập chiều cao của bạn (m): "))  # Chuyển chuỗi thành số thực
print(f"Chiều cao của bạn là {height} m.")  # In ra chiều cao

# 4. Nhập nhiều giá trị trong một dòng
x, y = map(int, input("Nhập hai số nguyên, cách nhau bằng dấu cách: ").split())  # Nhập và chia tách chuỗi, chuyển thành số nguyên
print(f"Bạn đã nhập x = {x} và y = {y}.")  # In ra hai số

# 5. Nhập một chuỗi và xử lý
sentence = input("Nhập một câu: ").lower()  # Chuyển chuỗi thành chữ thường
print(f"Câu bạn nhập là: {sentence}")  # In ra câu đã được chuyển thành chữ thường
