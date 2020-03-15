"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

def main():
    import random
    # score = float(input("Enter score: ")) ## User input score
    score = random.randint(0, 100) ## Randomly generated score
    print("You scored: {} ".format(score))
    print("Your score is {} ".format(score_check(score)))


def score_check(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    elif score <= 50:
        return "Bad"

main()