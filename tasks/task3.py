# tasks/task3.py

def solve():
# Ниже пишите решение задачи
    n = int(input())
hundreds = n // 100
twentys = n % 100 // 20
tens = n % 20 // 10
fives = n % 10 // 5
units = n % 5 // 1
banknotes = hundreds + twentys + tens + fives + units
print(banknotes)


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()