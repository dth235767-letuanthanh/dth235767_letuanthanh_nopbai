'''
Câu 9: Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm.
'''
print("Chương trình xác định quý của một tháng")

# Nhập tháng
month = int(input("Nhập vào một tháng (1-12): "))

# Xác định quý
if month >= 1 and month <= 3:
    print("Tháng", month, "thuộc quý 1")
elif month >= 4 and month <= 6:
    print("Tháng", month, "thuộc quý 2")
elif month >= 7 and month <= 9:
    print("Tháng", month, "thuộc quý 3")
elif month >= 10 and month <= 12:
    print("Tháng", month, "thuộc quý 4")
else:
    print("Tháng không hợp lệ")
