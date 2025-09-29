'''
Câu 6: Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ.
(vd: n=35 => Ba mươi lăm, n=5 => năm).
'''
def doc_so(n):
    # Các danh sách lưu tên chữ cho hàng chục và hàng đơn vị
    hang_chuc = ["", "Mười", "Hai mươi", "Ba mươi", "Bốn mươi", "Năm mươi",
                 "Sáu mươi", "Bảy mươi", "Tám mươi", "Chín mươi"]
    hang_don_vi = ["", "một", "hai", "ba", "bốn", "năm",
                   "sáu", "bảy", "tám", "chín"]

    # Trường hợp số không hợp lệ
    if n < 0 or n > 99:
        return "Số không hợp lệ"
    
    # Trường hợp số bằng 0
    if n == 0:
        return "Không"
    
    # Trường hợp số nhỏ hơn 10 (1 đến 9)
    elif n < 10:
        return hang_don_vi[n].capitalize()

    # Trường hợp số từ 10 trở lên
    else:
        chuc = n // 10       # Lấy phần chục
        don_vi = n % 10      # Lấy phần đơn vị

        chuc_str = hang_chuc[chuc]    # Đọc phần chục
        don_vi_str = ""

        # Xử lý các trường hợp đặc biệt cho phần đơn vị
        if don_vi == 0:
            don_vi_str = ""  # Nếu đơn vị = 0 thì không cần đọc phần đơn vị
        elif don_vi == 1 and chuc > 1:
            don_vi_str = "mốt"  # Trường hợp "mười mốt"
        elif don_vi == 4 and chuc > 1:
            don_vi_str = "tư"  # Trường hợp "hai tư", "ba tư", ...
        elif don_vi == 5 and chuc >= 1:
            don_vi_str = "lăm"  # Trường hợp "mười lăm", "hai lăm", ...
        else:
            don_vi_str = hang_don_vi[don_vi]  # Đọc phần đơn vị còn lại

        # Trả về kết quả cuối cùng
        if don_vi_str == "":
            return chuc_str
        else:
            return f"{chuc_str} {don_vi_str}"

# Nhập số và hiển thị kết quả
n = int(input("Nhập số (0-99): "))
print(doc_so(n))
