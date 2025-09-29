'''
Câu 18: Vẽ các hình dưới dây
'''
def hinh_vuong_rong(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

def tam_giac_trai(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            if j == 1 or i == n or i == j:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

def tam_giac_phai(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j == n or i == n or j == n - i + 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

n = int(input("Nhập chiều cao n: "))

print("\nHình vuông rỗng:")
hinh_vuong_rong(n)

print("\nTam giác vuông góc trái:")
tam_giac_trai(n)

print("\nTam giác vuông góc phải:")
tam_giac_phai(n)
