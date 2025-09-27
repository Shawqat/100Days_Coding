# Create a file called grade_checker.py.
# Write a program that:
# Asks the user for a test score (0–100).
# Prints the corresponding grade:
# 90–100: A
# 80–89: B
# 70–79: C
# 60–69: D
# Below 60: F

# Sample Output:
# Enter your test score: 85
# Your grade is: B

score = int(input("Enter your test score: "))
sentence = "Your grade is:"

if score > 100:
    score = int(input("Please Enter your test score correctly: "))
elif score >= 90:
    print(sentence, "A")
elif score >= 80:
    print(sentence, "B")
elif score >= 70:
    print(sentence, "C")
elif score >= 60:
    print(sentence, "D")
else:
    print(sentence, "F")