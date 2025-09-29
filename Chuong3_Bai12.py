'''
Câu 12: Xuất bảng cửu chương
'''
print("Chương trình in bảng cửu chương từ 2 đến 9")

# Duyệt từ bảng cửu chương 2 đến 9
for i in range(2, 10):
    print(f"\nBảng cửu chương {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
