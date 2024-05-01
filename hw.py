numsList = [7, 6, 23, 8.18, 18, 8, 7.2, 85, 915, 12]

# Finding the biggest number, smallest number, and calculating the average
biggest = numsList[0]
smallest = numsList[0]
total = 0

for i in range(len(numsList)):
    if numsList[i] > biggest:
        biggest = numsList[i]
        biggest_position = i
    if numsList[i] < smallest:
        smallest = numsList[i]
        smallest_position = i
    total += numsList[i]

average = total / len(numsList)

# Outputting the results
print("Biggest number:", biggest)
print("Smallest number:", smallest)
print("Average:", average)

stringsList = ["abc", "123", "2332", "aBBA", "heelloo", "1212", "DcEfD"]

# Count of strings with the same start and end characters
count = 0

for string in stringsList:
    # Check if the first and last characters are the same, ignoring case
    if string[0].lower() == string[-1].lower():
        count += 1

# Output the result
print("Number of strings with the same start and end characters:", count)

# Initialize lists to store favorite foods
iLikePesto = []
otherFoods = []

# Iterate through each person to ask their favorite food
for _ in range(8):
    favorite_food = input("What\’s your favourite food?")
    if favorite_food.lower() == 'pesto':
        iLikePesto.append(favorite_food)
    else:
        otherFoods.append(favorite_food)

# Print the number of times "pesto" is mentioned and print "I like pesto" that many times
print("Pesto is loved by", len(iLikePesto), "person!")
for _ in range(len(iLikePesto)):
    print("I like pesto")

# Print the list of other foods
print("\nOther Foods:")
for food in otherFoods:
    print(food)



