#Midterm exam:
#Question 1:
a = 6
a = a - 2
print(a*2)
a = a * 2
print(a+1)
a = a // 3

#Question 2:
print((2+3)*6/2 and 18.0)

#Question 3:
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

#Question 4:
def palindrome (word):
    word = str(word)
    if word == word [::-1]:
        return True
    else:
        return False
numbers = [
    4257304920394478392772938744930294037524,
    97410160773314967677676941337706101479,
    2704702208931031198668911301398022074072,
    7798338247658278460338648728567428338977
]

for number in numbers:
    if palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")

#Question 5:
def find_pattern_occurrences(text):
    """
    Finds occurrences of words that start with 'Un' and end with 'an'.

    Args:
        text (str): The input text to search in.

    Returns:
        int: Number of matches found.
    """
    words = text.split()  # Split text into a list of words
    count = 0

    for word in words:
        if word[:2]=="Un" and word[-2:]=="an":
            count += 1  # Increase count if the word matches the pattern

    return count

text = input("Enter the text to search in: ")
print(find_pattern_occurrences(text))

#Question 6:
#lists are mutable
my_list = [1, 2, 3, 4]
print("Original List:", my_list)

# Changing the second element
my_list[1] = 99
print("Modified List:", my_list)

# Adding a new element
my_list.append(5)
print("List after appending:", my_list)

# Removing an element
my_list.pop(2)  # Removes the element at index 2
print("List after removing an element:", my_list)

#strings are immutable:
my_string = "Hello world"
print("Original string:", my_string)
#Now trying to change string like we did with list:
#my_string[1] = "J"
new_string = "J" + my_string[1:]
print("New String:", new_string)
new_string_2 = my_string[0] + "a" + my_string[2:]
print("2nd New String:", new_string_2)

#Question 7:
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
print("Original random numbers:", random_numbers)

# Step 2: Modify the list (removing the numbers greater than 50 from the list and replacing them with a random number that is between 20 and 30. Also replace the number lower than 50 with "XX")
modified_numbers = []

for number in random_numbers:
    if number > 50:
        # Replace numbers greater than 50 with a random number between 20 and 30
        modified_numbers.append(random.randint(20, 30))
    else:
        # Replace numbers lower than or equal to 50 with "XX"
        modified_numbers.append("XX")

# Print the modified list
print("Modified numbers:", modified_numbers)





#Question 8:
def is_Valid_Url(URL):
    """
    Checks if the URL is valid.
    :param URL:
    :return:
    """
    if not URL[0:8]== "https://":
        return("not a valid URL")
    if " " in URL:
        return ("not a valid URL")
    else:
        return ("Well Done! This is a great URL.")

URL = input("Give me an URL that is valid: ")
print(is_Valid_Url(URL))

#Question 9:
def days_since_birthday():
    # Prompt the user to input their birthday in "DD-MM-YYYY" format
    birthday = input("Enter your birthday (DD-MM-YYYY): ")
    # Split the birthday string into day, month, and year
    day, month, year = map(int, birthday.split('-'))
    # Placeholder for the current year
    current_year = 2025
    # Calculate the number of full years since the birth year
    full_years = current_year - year - 1
    # Initialize the count of leap years
    leap_years = 0
    # Count how many leap years in the range from the year after the birth year to last year
    for y in range (year + 1, current_year):
        if (y % 4 == 0 and y % 100 != 0) or (y% 400 == 0):
            leap_years += 1
    # Calculate the number of days: leap years have 366 days, others have 365
    total_days = leap_years * 366 + (full_years - leap_years) * 365

    return total_days

print(days_since_birthday())