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

# Collect the moods for each day
for day in days_of_the_week:
    mood = input(f"What is your mood for {day}? ")
    moods[day] = mood

print("\nyour moods for the week:")
for day, mood in moods.items():
    print(f"{day}: {mood}")

mood_counts = {}

# Count how many times each mood appeared
for mood in moods.values():
    if mood in mood_counts:
        mood_counts[mood] += 1
    else:
        mood_counts[mood] = 1

total_days = len(days_of_the_week)
print("\nMood percentages for the week:")
for mood, count in mood_counts.items():
    percentage = (count / total_days) * 100
    print(f"{mood}: {percentage:.2f}%")

# Predict the most frequent mood for the next week
predicted_mood = max(mood_counts, key=mood_counts.get)
print(f"\nPrediction for your mood next week: {predicted_mood}")
