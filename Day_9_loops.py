# Repeat set of steps - loops
# while vs for
# DRY - Don't Repeat Yourself
# WET - write everything twice
# number=1
# while condition:
# while number<11:
#   print(number)
#  number+=1
"""
n = int(input("Enter number of rows : "))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print("✨", end=" ")
        j += 1
    print()
    i += 1
"""
# range starts from 0
# range(<start>,<end>,<skip>)
""" for i in range(1, 6, 2):
    print(i)

num = int(input("No of stars: "))
for i in range(1, num + 1):
    print("✨" * i)
"""
""" player_stats = [10, 20, 30]
values = []
for i in player_stats:
    i = i * 2
    values.append(i)
print(values)

# List comprehension - copy of the result
power_up_stats = [stat * 2 for stat in player_stats]
print(power_up_stats)
print(player_stats)
"""
avenger = ["hulk", "iron man", "black widow", "captain america", "spider man", "thor"]
val_count = []
# using for loop
for string in avenger:
    val_count.append(len(string))
print(val_count)
# list comprehension
length = [len(string) for string in avenger]
print(length)

big_names = []
for avng in avenger:
    if len(avng) > 10:
        big_names.append(avng)
        print(avng)

books = [
    {"title": "Infinite Jest", "rating": 4.5, "genre": "Fiction"},
    {"title": "The Catcher in the Rye", "rating": 3.9, "genre": "Fiction"},
    {"title": "Sapiens", "rating": 4.9, "genre": "History"},
    {"title": "A Brief History of Time", "rating": 4.8, "genre": "Science"},
    {"title": "Clean Code", "rating": 4.7, "genre": "Technology"},
]
result_books = []
for book in books:
    if book["rating"] >= 4.7:
        result_books.append(book["title"])

print(result_books)

_books = [book["title"] for book in books if book["rating"] >= 4.7]
print(_books)
