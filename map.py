# Python dasturlash tilida map funksiyasidan foydalanish.

# ! Python3 dasturlash tilida qanday qilib bitta qatorda foydalanuvchi tomonidan kiritilgan qiymatlarni olish mumkin?

# 1 - usul
vars = input().split()
a = int(vars[0])
b = int(vars[0])
print(a + b)

# 2 - usul (map yordamida)
a, b = map(int, input().split())
print(a + b)

# Berilgan listdagi harflarni, agar kichik harf bo'lsa(s.islower()) katta harfga, aksincha bo'lsa kichik harfga o;zgartirib beradigan dastur map yordamida.
letters = ["a", "L", "i", "s", "H", "E", "r", "R", "U", "s", "T", "e", "R"]

# 1 - usul

def update_letter(letter: str) ->str:
    if letter.isupper():
        return letter.lower()
    if letter.islower():
        return letter.upper()

updated_letters = list(map(update_letter, letters))
print(letters)
print(updated_letters)

# 2 - usul (lambda yordamida)

updated_letters2 = list(map(lambda l: l.lower() if l.isupper() else l.upper(), letters))

print(letters)
print(updated_letters2)
