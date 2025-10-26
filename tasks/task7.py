
number=int(input())
if not (1000 <= number <= 9999):  
        raise ValueError("Число должно быть четырёхзначным")
 digits = str(number) 
 replacement = {  
        '0': '5', '1': '6', '2': '7', '3': '8', '4': '9',  
        '5': '0', '6': '1', '7': '2', '8': '3', '9': '4'  
    }  
ncrypted_digits = [replacement[digit] for digit in digits]
return int(''.join(encrypted_digits)) 
print(f"Исходное число: {number}")  
print(f"Зашифрованное число: {encrypted}") 