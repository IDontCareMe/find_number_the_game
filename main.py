import random

minimum_val = 0
maximum_val = 100


# Функция is_valid() проверяет введенное пользователем число
# проверяет, что 1 <= число <= 100, а также, что число не содержит
# букв и других нечисловых символов
def is_valid(text):
  # Проверка на цифры
  for c in text:
    if not c.isdigit():
      return False
      
  # Проверка на диапазон
  if not minimum_val < int(text) <= maximum_val:
    return False

  return True


# Генеририруем случайное число
num = random.randint(1, 100)

print("Добро пожаловать в числовую угадайку!")

while True:
  print("Введите число от 1 до 100 и нажмите Enter")
  user_string = input()
  if not is_valid(user_string):
    print("А может быть все-таки введем целое число от 1 до 100?")
    continue
  new_number = int(user_string)
  print(new_number)
  break
