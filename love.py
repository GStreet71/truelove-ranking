def calc_score(name1, name2):
    key1 = "TRUE"
    key2 = "LOVE"
    score1 = 0
    score2 = 0
    combined_name = (name1 + name2)

    for letter in key1:
        count = combined_name.count(letter)
        score1 += count
        print(letter, count)
    print(f"Total = {score1}")

    for letter in key2:
        count = combined_name.count(letter)
        score2 += count
        print(letter, count)
    print(f"Total = {score2}")

    concat = str(score1) + str(score2)
    return concat

def print_results(concat):
    score = int(concat)
    if score < 10 or score > 90:
        print("*************************************************************")
        print(f"Your score is {score}, you go together like coke and mentos.")
        print("*************************************************************")
    elif score > 40 and score < 50:
        print("*************************************************")
        print(f"Your score is {score}, you are alright together.")
        print("*************************************************")
    else:
        print("***********************")
        print(f"Your score is {score}.")
        print("***********************")


name1 = input("Enter name 1: ").upper()
name2 = input("Enter name 2: ").upper()
score = calc_score(name1, name2)

print_results(score)