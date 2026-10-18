
# PYTHON ASSIGNMENT 3
# While Loop, For Loop and Function



# PART 1: WHILE LOOP - NUMBER GUESSING GAME

# import random

print("\n--- NUMBER GUESSING GAME ---")

secret_number = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Guess the number (between 1 and 10): "))

    # Check whether the guess is within the valid range
    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue

    # Reduce the attempts for a valid guess
    attempts = attempts - 1

    # Check the guess
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break

    elif guess > secret_number:
        print("Too high. Try again.")

    else:
        print("Too low. Try again.")

else:
    print("Better luck next time!")
    print("The correct number was:", secret_number)



# PART 2: FOR LOOP - MULTIPLICATION TABLE


print("\n--- MULTIPLICATION TABLE ---")

number = int(input("Enter the number for which you want the multiplication table: "))

for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)



# PART 3: FUNCTION - BMI CALCULATOR


print("\n--- BMI CALCULATOR ---")

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

if weight > 0 and height > 0:
    bmi = calculate_bmi(weight, height)
    print("Your BMI is:", round(bmi, 2))
else:
    print("Weight and height must be greater than zero.")


