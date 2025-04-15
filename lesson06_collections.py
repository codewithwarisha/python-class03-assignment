# -----------------------------------------
# Lesson 06: Working with Lists, Tuples, and Dictionary
# -----------------------------------------

# List: Grocery Items
grocery_list = ["Milk", "Eggs", "Bread"]
print("🛒 Grocery List:", grocery_list)
grocery_list.append("Butter")
print("Updated List:", grocery_list)

# Tuple: Days of the Week (Immutable)
days = ("Monday", "Tuesday", "Wednesday")
print("\n📅 First Day of the Week:", days[0])

# Dictionary: Student Information
student = {
    "name": "Ayesha",
    "roll_no": 42,
    "course": "Python Programming"
}
print("\n🎓 Student Info:")
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")

