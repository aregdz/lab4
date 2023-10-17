h = int(input("Введите часы "))
m = int(input("Введите минуты "))
s = int(input("Введите секунды "))
if h > 12:
    h = h - 12
riz = 360 * (h*3600 +m*60 +s) / (12*3600)
print(riz)