# a = 8
# b = 10
# print("The sum is: ", a + b)


# function
# declaration /Definition (def)
# function name (sum())
# parameters (a,b)
# function body
# def sum(a, b):
#     return round(a + b)


# print(sum(5, 6))  # function call
# print("the sum is", sum(26, 25))
# print(sum(60.755555, 75.222284))


# default values
# def driving_test(name, age, car="Innova"):
#     if age >= 18:
#         return f"{name}, you are eligible for driving. you will tested with {car}"
#     else:
#         return "Try when you will get 18 years"


# print(driving_test("Sai Ganesh", 22))

# Types of Arguments
# 1. Positional arguments
# 2. Keyword arguments
# print(driving_test(age=20, name="Poojitha"))
# print(driving_test("Samar", car="kwid", age=21))

library_list = [
    {
        "title": "Python Programming",
        "author": "Eric Matthes",
        "year": 2019,
        "available": True,
    },
    {
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "year": 2020,
        "available": True,
    },
    {
        "title": "Learning Python I",
        "author": "Mark Lutz",
        "year": 2013,
        "available": False,
    },
    {
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "year": 2015,
        "available": True,
    },
    {
        "title": "Adavance Python",
        "author": "Mark Lutz",
        "year": 2015,
        "available": False,
    },
]


# Task 1 -
# Add book function: write a function add_book(library, new_book)
""" def add_book(library):
    new_book = {}
    new_book["title"] = input("Enter the title of the book: ")
    new_book["author"] = input("Enter the author of the book: ")
    new_book["year"] = int(input("Enter the publication year of the book: "))
    new_book["available"] = (
        input("Is the book available? (True/False): ").lower() == "true"
    )
    library.append(new_book)


add_book(library_list)
print(library_list)

"""


# # task 2 -
# def search_by_author(library):
#     return [book for book in library if book["author"] == "Luciano Ramalho"]


# # Task 3 - check out function check_out_book(library, title) that marks a book as not available
# # if it exists and is available in the library
# # .format -> f""
# # return and function body completes


# def check_out_book(library, title):
#     for book in library:
#         if book["title"] == title and book["available"]:
#             book["available"] = False
#             print(f"Book '{title}' has been checked out.")
#             return
#     print(f"Book '{title}' is not available.")


# check_out_book(library_list, "Learning Python I")

# list = [1, 2, 3, 4, 5]
# print(sum(list))
# print(max(list))
# print(min(list))
# print(len(list))

movies = [
    {"title": "Inception", "ratings": [5, 4, 5, 4, 5]},
    {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4]},
    {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4]},
    {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5]},
    {"title": "Memento", "ratings": [4, 5, 4, 5, 4]},
]
# function
# task 1 -  add_avg_settings
# import package - inbuilt
# from package_name import function_name
# from pprint import pprint


# def avg_movie_rating(movie):
#     title = movie["title"]
#     ratings = movie["ratings"]
#     avg_rating = sum(ratings) / len(ratings)
#     return title, ratings, avg_rating


# def get_rating(movies):
#     return {
#         [
#             movie["title"],
#             movie["ratings"],
#             sum(movie["ratings"]) / len(movie["ratings"]),
#         ]
#         for movie in movies
#     }


# avg_ratings = get_rating(movies)
# pprint(avg_ratings)


# def own_max(*nums):
#     # implement max logic
#     print(nums, type(nums))


# arbitary postional arguments
def own_max(*nums):
    lmax = nums[0]
    for n in nums:
        if n > lmax:
            lmax = n
    return lmax


print(own_max(5, 6, 10))
print(own_max(5, 6, 10, 7, 80, 60))


# arbitary keyword arguments
def party(**people):
    # print(people, type(people))
    print(",".join(people.values()))


party(p1="Abhishek", p2="Amisha", p3="Ganesh", p4="Poojitha")


# lambda functions
class Car:
    def __init__(
        self, name, engine, wheels, doors
    ):  # creating object calls init (constructor)
        self.name = name
        self.engine = engine
        self.wheels = wheels
        self.doors = doors


ferrari = Car("Ferrari", "v8", 4, 2)  # object
alto = Car("Alto", "v4", 4, 4)  # object

print(ferrari.name, ferrari.wheels)
