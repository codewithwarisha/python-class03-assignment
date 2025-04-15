# ----------------------------
# Lesson 05: 
# 
# Control Flow & Loops Example
# ----------------------------

# If-Else: Voting Eligibility Check
age = 17
if age >= 18:
    print("✅ You are eligible to vote.")
else:
    print("❌ You are not eligible to vote.")

# For Loop: Print square of numbers
print("\n🔁 Squares from 1 to 5:")
for num in range(1, 6):
    print(f"{num}² = {num**2}")

# While Loop: Countdown
print("\n⏳ Countdown:")
count = 3
while count > 0:
    print(count)
    count -= 1
print("🚀 Lift off!")
