# Question NO 1
# def divisble():
#     count=1500
#     while(count<=2700):
#         count=count+1
#         if count%5==0 and count%7==0:
#             print(count)


# divisble()


# Question No 2

# def temp():
#     y = int(input("If you want to convert Celsius to Fahrenheit press 1, and if you want to convert Fahrenheit to Celsius press 2\n"))
#     if y == 1:
#         temperature = float(input("Enter temperature in Celsius\n"))
#         print((9/5) * temperature + 32) 
#     elif y == 2:
#         temperature = float(input("Enter temperature in Fahrenheit\n"))
#         print((5/9) * (temperature - 32))
#     else:
#         print("Invalid input. Please press 1 or 2.")

# temp()


#Question No 3

# def game():
#     y = int(input("Guess the number"))
#     if y not in range(2,9):
#         game()
#     else:
#         print("Well Guessed")
# game()


# Question#4

# def pattern():
#     for i in range(1,6):
#         for j in range(1,i+1):
#               print("*",end=" ")
#         print()   
#     for i in range(5,0,-1):
#         for j in range(1,i+1):
#               print("*",end=" ")
#         print()       
# pattern()

# Question#5

# def reverse():
#     y = input("Enter the word\n")
#     x =""
#     for j in range(len(y)-1,-1,-1):
#         x+=y[j]
#     print("Reverse is",x)

# reverse()

# y = input("Enter the word\n")
# x=''.join(reversed(y))
# print(x)

     

# Question No 6

# numbers =(1,2,3,4,5,6,7,8,9)
# even=0
# odd=0

# for i in numbers:
#     if i%2==0 :
#         even=even+1
#     else :
#         odd =odd+1

# print("Number of even number",even)
# print("Number of odd number",odd)


# Question No 7

# datalist=[1452,11.23,1+2j,True,'w3resource',(0,1),[5,12],{"class":'V',"section":'A'}]

# for i in datalist:
#     print(i,"The type is",type(i))

# Question No 8


# for i in range(0, 7):
#     if i == 3 or i == 6:
#         continue
#     else:
#         print(i)

#Question No 9 (fibonacci)
# a = 0
# b = 1
# c = 0
# print(a, end=", ")
# print(b, end="")

# while c < 50:
#     c = a + b
#     if c > 50:
#         break
#     a = b
#     b = c
#     print(", ", c, end="")

# Question No 10

# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0 :
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else :
#         print(i)

# Question NO 11

# rows, cols = 3, 4
# array = [[0 for _ in range(cols)] for _ in range(rows)]

# for i in range(rows):
#     for j in range(cols):
#         array[i][j] = i * j

# for row in array:
#     print(row)

# Question NO 12


# def read_lines():
#     lines = []
#     while True:
#         line = input("Enter a line (blank line to terminate):\n")
#         if line == "":
#             break
#         lines.append(line.lower())  # Convert to lowercase and append to list
    
#     for line in lines:
#         print(line)  # Print each line in lowercase

# read_lines()


# Question No 13
# def binary_to_decimal():
#     string = input("Enter the sequence of binary numbers separated by comma: ")
#     binaries = string.split(',')
#     output = ""
#     for binary in binaries:
#         decimal = int(binary, 2)  # Convert binary string to decimal
#         if decimal % 5 == 0:
#             output += binary + ","
#     if output:  # Check if there's any output to print
#         print("Binary numbers divisible by 5:", output[:-1])  # Remove the last comma
#     else:
#         print("No binary numbers divisible by 5 found.")

# binary_to_decimal()


# Question No 14
# def count_letters_digits():
#     input_string = input("Enter a string: ")
#     letters = 0
#     digits = 0
    
#     for char in input_string:
#         if char.isalpha():  # Check if character is a letter
#             letters += 1
#         elif char.isdigit():  # Check if character is a digit
#             digits += 1
    
#     print(f"Letter count: {letters}")
#     print(f"Digit count: {digits}")

# count_letters_digits()



# Question No 15
def check_password_valid(password):
    # Define rules
    min_length = 6
    max_length = 16
    special_chars = ['$','#','@']
    
    # Check length
    if len(password) < min_length or len(password) > max_length:
        print(f"Password length should be between {min_length} and {max_length} characters")
        return False
    
    # Check for required characters
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in special_chars for char in password)
    
    # Validate based on rules
    if not has_lower:
        print("Password should contain at least one lowercase letter")
        return False
    if not has_upper:
        print("Password should contain at least one uppercase letter")
        return False
    if not has_digit:
        print("Password should contain at least one digit (0-9)")
        return False
    if not has_special:
        print("Password should contain at least one of the following special characters: $, #, @")
        return False
    
    # All criteria met
    return True

password = input("Enter your password: ")
if check_password_valid(password):
    print("Password is valid")
else:
    print("Password is invalid")

