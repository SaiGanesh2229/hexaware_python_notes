# # compile time error (Syntax error)
# # Errors
# # try, except, else, finally
# def math_divide(n1, n2):
#     try:
#         res = n1 / n2
#     except ZeroDivisionError:
#         return "OOPs, Error Occured"
#     else:
#         print("Division successful")
#     finally:
#         print("Operation Done")
#     return res


# # Run time error
# print(math_divide(15, 5))
# print(math_divide(10, 0))  # Execution stopped
# print(math_divide(15, 3))

# # How to handle errors


# from datetime import datetime

# print(datetime.now().weekday())
# print(datetime.now().day)

from datetime import datetime


def calculate_age(dob):
    try:
        dob_date = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.today()
        age = (
            today.year
            - dob_date.year
            - ((today.month, today.day) < (dob_date.month, dob_date.day))
        )
        return age
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD format."


# Test the calculate_age function
print(calculate_age("2001-12-22"))
