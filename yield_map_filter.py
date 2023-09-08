# Python dasturlash tilida yield yordamida o'zimizning map va filter funksiyamizni yasaymiz.

# my own filter

def FILTER(func, sequence):
    for i in sequence:
        if func(i):
            yield i

def is_str(i):
    if type(i) == str:
        return True
    return False

# o'zimizning filter funksiyamizni tekshirib ko'ramiz
a = list(FILTER(is_str, ["a", 4, "f", 45, "t", "g", "q", 8, 90]))
print(a)

# my own map

def MAP(func, sequence):
    for i in sequence:
        yield func(i)

# o'zimizning map funksiyamizni tekshirib ko'ramiz
a, b = MAP(int, input().split())
print(a + b)
