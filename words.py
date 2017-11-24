words = {
  'тетрадь': 'copybook',
  'книга' : 'book',
  'ручка' : 'pen',
  'карандаш' : 'pencil',
  'яблоко' : 'apple',
  'цвет' : 'colour',
}

print(" "* 5,"Словарь")
for key in words:
  print(key, words[key])

while True:
  print("Вы хотите добавить новое слово? да -1, нет - 2")
  answer =  input("> ")
  if answer == "1":
    print("Добавьте слово на")
    eng = input("Английском:")
    print("Напишите перевод на") 
    ru = input("Русском:")
    words[eng] = ru
  else:
    break
