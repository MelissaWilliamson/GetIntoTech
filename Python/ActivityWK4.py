## list of fave fruits
## longest fruit and the number of characters
## sort the list using key and len (length)
favefruits = ['raspberries', 'strawberries', 'mango', 'watermelon']
favefruits.sort(key=len)
print(favefruits)
print(favefruits[-1])
print(len(favefruits[3]))

fruits = ["apple", "banana",  "watermelon", "pineapple"]
longest_fruit = ""
max_characters = 0
for fruit in fruits:
    if len(fruit) > max_characters:
        longest_fruit = fruit
        max_characters = len(fruit)
print("Fruit with the longest name:", longest_fruit)
print("Number of characters:", max_characters)

foods = ['Pizza', 'Kebab', 'Burger', 'Chips', 'Salad', 'Chocolate']
most_letters = 0
most_letters_item = None
for letters in foods:
    if len(letters) > most_letters:
        most_letters = len(letters)
        most_letters_item = letters
print(most_letters_item)
print(most_letters)




