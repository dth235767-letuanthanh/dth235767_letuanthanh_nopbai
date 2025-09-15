'''
Câu 9: Giải thích kết quả tính toán của các biểu thức
Câu 9: Giải thích kết quả tính toán của các biểu thức
Yêu cầu:
Cho các biến với giá trị
Trang 20/84
i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2 = 5.0
d3 = -0.5
Cho biết kết quả và giải thích cách thực hiện của các lệnh sau:
(a) i1 + (i2 * i3)
(b) i1 * (i2 + i3)
(c) i1 / (i2 + i3)
(d) i1 // (i2 + i3)
(e) i1 / i2 + i3
(f) i1 // i2 + i3
(g) 3 + 4 + 5 / 3
(h) 3 + 4 + 5 // 3
(i) (3 + 4 + 5) / 3
(j) (3 + 4 + 5) // 3
(k) d1 + (d2 * d3)
(l) d1 + d2 * d3
(m) d1 / d2 - d3
(n) d1 / (d2 - d3)
(o) d1 + d2 + d3 / 3
(p) (d1 + d2 + d3) / 3
(q) d1 + d2 + (d3 / 3)
(r) 3 * (d1 + d2) * (d1 - d3)
'''
# Khai báo biến
i1, i2, i3 = 2, 5, -3
d1, d2, d3 = 2.0, 5.0, -0.5

# Tính toán các biểu thức với i1, i2, i3
results_i = {
    "a": i1 + (i2 * i3),           # i1 + (i2 * i3)
    "b": i1 * (i2 + i3),           # i1 * (i2 + i3)
    "c": i1 / (i2 + i3),           # i1 / (i2 + i3)
    "d": i1 // (i2 + i3),          # i1 // (i2 + i3)
    "e": i1 / i2 + i3,             # i1 / i2 + i3
    "f": i1 // i2 + i3,            # i1 // i2 + i3
    "g": 3 + 4 + 5 / 3,            # 3 + 4 + 5 / 3
    "h": 3 + 4 + 5 // 3,           # 3 + 4 + 5 // 3
    "i": (3 + 4 + 5) / 3,          # (3 + 4 + 5) / 3
    "j": (3 + 4 + 5) // 3          # (3 + 4 + 5) // 3
}

# Tính toán các biểu thức với d1, d2, d3
results_d = {
    "k": d1 + (d2 * d3),            # d1 + (d2 * d3)
    "l": d1 + d2 * d3,              # d1 + d2 * d3
    "m": d1 / d2 - d3,              # d1 / d2 - d3
    "n": d1 / (d2 - d3),            # d1 / (d2 - d3)
    "o": d1 + d2 + d3 / 3,          # d1 + d2 + d3 / 3
    "p": (d1 + d2 + d3) / 3,        # (d1 + d2 + d3) / 3
    "q": d1 + d2 + (d3 / 3),        # d1 + d2 + (d3 / 3)
    "r": 3 * (d1 + d2) * (d1 - d3)  # 3 * (d1 + d2) * (d1 - d3)
}

# In kết quả các biểu thức với i1, i2, i3
print("Kết quả các biểu thức với i1, i2, i3:")
for key, value in results_i.items():
    print(f"Biểu thức ({key}): {value}")

# In kết quả các biểu thức với d1, d2, d3
print("\nKết quả các biểu thức với d1, d2, d3:")
for key, value in results_d.items():
    print(f"Biểu thức ({key}): {value}")