"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = int(input("Enter score: "))
while score < 0 or score > 100:
    score = int(input("Invalid score. Enter score: "))
if score > 49:
    print("Passable")
elif score > 89:
        print("Excellent")
else:
    print("Bad")
