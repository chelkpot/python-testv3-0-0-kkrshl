# tasks/task1.py

def solve():
# Ниже пишите решение задачи
a = int(input())
x = a // 100
y = a %100 //10
z = a % 10
print(x + y + z)

    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()