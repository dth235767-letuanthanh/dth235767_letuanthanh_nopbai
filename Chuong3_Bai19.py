'''
Câu 19: Tính giá trị biểu thức S
Nhập x,n. Tính S(x,n)= x + x^3/3! + x^5/5! + ... + x^2n+1/(2n+1)!
'''
import math

def tinh_S(x, n):
    S = 0
    for i in range(n + 1):
        mu = 2 * i + 1            # Lũy thừa và giai thừa là số lẻ: 1,3,5,...
        tu = x ** mu              # Tính x^(2i+1)
        mau = math.factorial(mu)  # Tính (2i+1)!
        S += tu / mau
    return S

# Nhập dữ liệu từ người dùng
x = float(input("Nhập giá trị x: "))
n = int(input("Nhập số n (số số hạng): "))

# Tính và in kết quả
result = tinh_S(x, n)
print(f"Gía trị biểu thức S({x},{n}) = {result}")
