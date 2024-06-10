#EFRATA ARON
#Python Best Practices
"""_summary_
    =Follow PEP 8
    1. Indentation
    2. Maximum Line Length : Limit to 79 characters
    3. Blank Lines
    4. Use meaningful names
    """
    
    
#Example of Good meaningful name


# def calculate_area(radius):
#     pass
# total_price = 10000


# #Example of a lazy student with a bad meaningful name
# def calc(r):
#     pass


# tp = 10000



# Python operators
"""_summary_
    Name of the operator        Symbol with Example
    Addition                       x + y
    Subtraction                    x + y
    Multiplication                 x * y
    Division                       x / y
    Modulus                        x %% y
    Exponentiation                 x ** y
    Floor division                 x // y
    """
    
    #Example of Comparison operators
"""_summary_
    Name of the operator        Symbol with Example
    Equal                          x == y
    Not equal                      x != y
    Greater than                   x > y
    Less than                      x < y
    Greater than or equal to       x >= y
    Less than or equal to          x <= y
    
    """   
    
    # Example of Python Logical operators
"""_summary_
    Name of the operator        Example Symbol
    and                         and
    or                          or
    not                         not
   
    # Example of Membership operators
    Name                        Symbol with Example
    in                          x in y
    not in                      x not in y
    
    # Example of Python Bitwise operators
     Name                        Symbol with Example
    AND                           &
    OR                            |
    XOR                           ^
    NOT                           ~
    
    # Python cases
    
    1. snake_case
    2. camelCase
    3. PascalCase
    4. UPPERCASE
    5. kebab-case
    
    """
    
    
#Comprehensions (List, dictionary comprehensions)
"""_summary_
    Comprehensions provide a concise way to create lists and dictionaries
    what is the symbol for
    lists               [] square brackets used to store multiple items in asingle variable
    dictionaries        {} curly brackets used to store data values in key:value pairs
    
    """
    
# Example 1: Basic List Comprehensions
# create a list of squares in range of 10
print("Example 1")

list_of_squares = [x**2  for x in range(10)]
print(list_of_squares)

# Exercise 1: Create a list of even square in the range of 20
print()
print("Exercise 1 solution")
list_of_even_squares = [x**2 for x in range(20) if x**2 % 2 == 0]
print(list_of_even_squares)
print()
    
    
 # Example 2: Dictionary Comprehensions
 # Create a dictionary comprehension for favorites cars count the lengths of the characters
print()
print("Example 2")
favorite_cars = ["BMW", "Jeep", "Mercedes", "fordraptor"]
car_lengths = {car: len(car) for car in favorite_cars}
print(car_lengths) 
print()


# Exercise 2: Create a list of tuple where each tuple contains a number and its cube for numbers
# between 1 and 10 using a dictionary comprehension

print("Exercise 2 solution")
number_and_cubes_dictionary= {x: x**3 for x in range(1, 11)}

print()
print("numbers and their cubes")
print(list(number_and_cubes_dictionary.items()))

