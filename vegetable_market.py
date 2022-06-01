price_vegetables_kg = float(input())
price_fruits_kg = float(input())
vegetables_kgs = int(input())
fruits_kgs = int(input())

vegetables = price_vegetables_kg*vegetables_kgs
fruits = price_fruits_kg*fruits_kgs
sum = vegetables + fruits
sum_to_euro = sum/1.94
print(sum_to_euro)
