# tasks/task5.py

def solve():
# Ниже пишите решение задачи
n = int(input())
h = n // 3600
n = n % 3600
m = n // 60
n = n % 60
print(f'{h:02}:{m:02}:{n:02}')

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()