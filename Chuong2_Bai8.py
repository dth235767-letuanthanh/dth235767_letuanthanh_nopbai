'''
Câu 8: Trình bày các loại lỗi khi lập trình và cách bắt lỗi trong Python.
'''
try:
    # Lỗi cú pháp
    # print(Hello World)  # Uncomment để gây lỗi cú pháp

    # Lỗi thực thi (RuntimeError)
    x = 10 / 0  # Chia cho 0 gây lỗi ZeroDivisionError

    # Lỗi tham chiếu (NameError)
    print(a)  # Biến 'a' chưa được định nghĩa

    # Lỗi kiểu dữ liệu (TypeError)
    result = "Hello" + 10  # Không thể cộng chuỗi và số nguyên

    # Lỗi chỉ số (IndexError)
    lst = [1, 2, 3]
    print(lst[5])  # Chỉ số vượt quá phạm vi

except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")

except NameError:
    print("Lỗi: Biến chưa được định nghĩa!")

except TypeError:
    print("Lỗi: Kiểu dữ liệu không hợp lệ!")

except IndexError:
    print("Lỗi: Chỉ số vượt quá phạm vi!")

except Exception as e:
    print(f"Lỗi không xác định: {e}")

else:
    print("Không có lỗi xảy ra.")

finally:
    print("Đoạn mã này luôn được thực thi.")