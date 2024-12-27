#Users input their mood (happy, sad, stressed, etc.) each day, and the program calculates the percentage of each
#mood over a week.

while True:
    name = input("Hello Trainee please enter your name: ")
    age = int(input("Enter your age too: "))
    print(f"to be sure your name is {name} and you are {age} years old ")

    confirmation = input("If you confirm, enter yes if not enter anything else: ")

    if confirmation == "yes":
        break

    else:
        print("please reenter your name and age")

days_of_the_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
moods = {}

for day in days_of_the_week:
    mood = input(f"What is your mood for {day}? ")
    moods[day] = mood

print("\nyour moods for the week:")
for day, mood in moods.items():
    print(f"{day}: {mood}")

mood_counts = {}

# Iterate through the moods in the dictionary values
for mood in moods.values():
    if mood in mood_counts:
        mood_counts[mood] += 1  # Increment count if the mood is already in the dictionary
    else:
        mood_counts[mood] = 1  # Initialize count if the mood is not in the dictionary

total_days = len(days_of_the_week)
print("\nMood percentages for the week:")
for mood, count in mood_counts.items():
    percentage = (count / total_days) * 100
    print(f"{mood}: {percentage:.2f}%")
