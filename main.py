import random

minimum_val = 1
maximum_val = 100

number_of_trys = 0

# Функция is_valid() проверяет введенное пользователем число
# проверяет, что 1 <= число <= 100, а также, что число не содержит
# букв и других нечисловых символов
def is_valid(text):
  # Проверка на цифры
  for c in text:
    if not c.isdigit():
      return False
      
  # Проверка на диапазон
  if not minimum_val <= int(text) <= maximum_val:
    return False

  return True
  
# Генеририруем случайное число
num = random.randint(minimum_val, maximum_val)

print("Добро пожаловать в числовую угадайку!")

while True:
  print("Введите число от 1 до 100 и нажмите Enter")
  user_string = input()
  if not is_valid(user_string):
    print("А может быть все-таки введем целое число от 1 до 100?")
    continue
  new_number = int(user_string)
  number_of_trys += 1
  if new_number < num:
    print("Ваше число меньше загаданного, попробуйте еще разок")
  elif new_number > num:
    print("Ваше число больше загаданного, попробуйте еще разок")
  else:
    print("Вы угадали, поздравляем!")
    print("Количество попыток:", number_of_trys)
    
    if input("Хотите сыграть снова? y - да, n - нет \n") == "y":
      # Генеририруем новое случайное число
      num = random.randint(minimum_val, maximum_val)
      # Обнуляем счётчик попыток
      number_of_trys = 0
    else:
      print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
      break
