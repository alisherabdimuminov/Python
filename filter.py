# filter in Python

# [filter] yordamida berilgan listdagi barcha juft/toq sonlarni chiraish

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1 - usul (funksiya yordamida)

def is_even(n: int) -> bool: # int turidagi n sonini argument sifatida qabul qiladi va bool turidagi qiymat qaytaradi
    return n % 2 == 0 # bu yerda n % 2 == 0 ifodasining natijasi qaytariladi. Misol: n = 4, 4 % 2 == 0 => True, demak funksiya True qiymat qaytaradi

def is_odd(n: int) -> bool: # int turidagi n sonini argument sifatida qabul qiladi va bool turidagi qiymat qaytaradi
    return n % 2 != 0 # bu yerda n % 2 != 0 ifodasining natijasi qaytariladi. Misol: n = 4, 4 % 2 != 0 => False, demak funksiya True qiymat qaytaradi

evens1 = list(filter(is_even, numbers))
odds   = list(filter(is_odd, numbers))

print(evens1)
print(odds)

# 2 - usul (lambda yordamida)

evens2 = list(filter(lambda n: n % 2 == 0, numbers))
odds2 = list(filter(lambda n: n % 2 != 0, numbers))

print(evens2)
print(odds2)
