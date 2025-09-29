'''
Câu 15: Giải thích cách chạy các dòng lệnh range
Yêu cầu:
(a) range(5)
(b) range(5, 10)
(c) range(5, 20, 3)
(d) range(20, 5, -1)
(e) range(20, 5, -3)
(f) range(10, 5)
(g) range(0)
(h) range(10, 101, 10)
(i) range(10, -1, -1)
(j) range(-3, 4)
(k) range(0, 10, 1)
'''# (a) range(5) tạo dãy số từ 0 đến 4
print(list(range(5)))  # [0, 1, 2, 3, 4]

# (b) range(5, 10) tạo dãy số từ 5 đến 9
print(list(range(5, 10)))  # [5, 6, 7, 8, 9]

# (c) range(5, 20, 3) tạo dãy số bắt đầu 5, bước 3, đến <20
print(list(range(5, 20, 3)))  # [5, 8, 11, 14, 17]

# (d) range(20, 5, -1) tạo dãy giảm từ 20 đến 6 (lớn hơn 5)
print(list(range(20, 5, -1)))  # [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]

# (e) range(20, 5, -3) tạo dãy giảm từ 20, bước 3, đến >5
print(list(range(20, 5, -3)))  # [20, 17, 14, 11, 8]

# (f) range(10, 5) bước mặc định +1, nhưng start > stop => dãy rỗng
print(list(range(10, 5)))  # []

# (g) range(0) dãy rỗng vì stop = 0
print(list(range(0)))  # []

# (h) range(10, 101, 10) tạo dãy từ 10 đến 100, bước 10
print(list(range(10, 101, 10)))  # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# (i) range(10, -1, -1) tạo dãy giảm từ 10 đến 0
print(list(range(10, -1, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# (j) range(-3, 4) tạo dãy từ -3 đến 3
print(list(range(-3, 4)))  # [-3, -2, -1, 0, 1, 2, 3]

# (k) range(0, 10, 1) tạo dãy từ 0 đến 9, bước 1
print(list(range(0, 10, 1)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
