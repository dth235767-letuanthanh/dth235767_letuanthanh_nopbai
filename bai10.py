rows = [
    1, 3, 7,   # tầng 1
    3, 5, 11   # tầng 2
]

max_width = max(rows)   # dòng dài nhất (11 *)

# In các tầng (canh giữa)
for n in rows:
    stars = "*" * n
    print(stars.center(max_width))

# In thân cây (2 dòng, 2 * rỗng, canh giữa)
for i in range(2):
    trunk = "*" + " " + "*"
    print(trunk.center(max_width))
