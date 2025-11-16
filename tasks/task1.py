# tasks/task1.py

def solve():
# Ниже пишите решение задачи
n=int(input())
hundreds=n // 100
tens=(n // 10) % 10
units=n % 10
result=hundreds + tens + units
print(result)
    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()