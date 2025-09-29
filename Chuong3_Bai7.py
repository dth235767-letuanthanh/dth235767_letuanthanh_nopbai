'''
Câu 7: Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày
vừa nhập (ngày/tháng/năm).
'''
print("Chương trình tìm ngày kế tiếp")

# Nhập vào ngày, tháng, năm
day = int(input("Nhập vào ngày: "))
month = int(input("Nhập vào tháng: "))
year = int(input("Nhập vào năm: "))

# Kiểm tra xem tháng có hợp lệ không
if month < 1 or month > 12:
    print("Tháng không hợp lệ")
else:
    # Xác định số ngày trong tháng đã nhập
    if month in (1, 3, 5, 7, 8, 10, 12):
        days_in_month = 31
    elif month in (4, 6, 9, 11):
        days_in_month = 30
    elif month == 2:
        # Kiểm tra năm nhuận
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            days_in_month = 29
        else:
            days_in_month = 28

    # Kiểm tra ngày có hợp lệ không
    if day < 1 or day > days_in_month:
        print("Ngày không hợp lệ")
    else:
        # Tìm ngày kế tiếp
        day += 1

        if day > days_in_month:  # Nếu ngày kế tiếp là ngày đầu tháng sau
            day = 1
            month += 1

            if month > 12:  # Nếu tháng sau là tháng 13, thì chuyển sang năm mới
                month = 1
                year += 1

        print(f"Ngày kế tiếp là: {day}/{month}/{year}")
