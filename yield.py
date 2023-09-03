# Python dasturlash tilida generatorlar bilan ishlash yield

# ? 1 dan n gacha bo'lgan kvadrat sonlar to'lamini hosil qiling.
n = 1000000000 # 😱
# 1 - usul (oddiy for)

squares = [x*x for x in range(1, n+1)] # kompyuterimiz qishki uyquga ketadi 😂

for i in squares:
    print(i)


# 2 - usul (optimized) ✅

def squares(n):
    for i in range(1, n + 1):
        yield i*i

my_squares = squares(n)
for i in my_squares:
    print(i)
