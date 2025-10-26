# tasks/task2.py

def solve():
# Ниже пишите решение задачи
n = int(input("Введите количество минут: ")) 
n = n % 1440
hours = n // 60  
minutes = n % 60  
print(f"{hours:02}:{minutes:02}")  
   

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()