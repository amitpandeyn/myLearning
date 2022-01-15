score = 0
# QUESTION 1 
answer1 = input ("Which of the following is a compound? \na. Sodium \nb. Iron\nc. Sand \nAnswer: ")
if answer1 == "c":
    score = score + 1 
    print("Correct!!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect!! The answer is Sand")
    print("Score: ", score)
    print("\n")
answer2 = input ("Which of the following is a metal? \na. Lithium \nb. Iron\nc. Both of these \nAnswer: ")
if answer2 == "c":
    score = score + 1 
    print("Correct!!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect!! The answer is both of these")
    print("Score: ", score)
    print("\n")
answer3 = input ("Which of the following is liquid at room temperature? \na.Lithium \nb.Mercury\nc.Both of these \nAnswer: ")
if answer3 == "b":
    score = score + 1 
    print("Correct!!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect!! The answer is Mercury")
    print("Score: ", score)
    print("\n")
answer4 = input ("Which is the force that is weakest and strongest simultaenously in the nature? \na. Gravitation \nb. Magnetism\nc. Kinetic \nAnswer: ")
if answer4 == "a":
    score = score + 1 
    print("Correct!!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect!! The answer is Gravitation")
    print("Score: ", score)
    print("\n")
answer5 = input ("Which of the following tissue is present in the husk of a coconut? \na. Sclerenchyma \nb. Parenchyma\nc. Stratified columnar epetheliumm \nAnswer: ")
if answer5 == "a":
    score = score + 1 
    print("Correct!!")
    print("Score: ", score)
    print("\n")
else:
    print("Incorrect!! The answer is sclerenchyma")
    print("Score: ", score)
    print("\n")
#FINAL MESSAGE
if score <= 1:
    print("Your total score is:", score, "- Try hard, you'll make it someday")
elif score == 2:
    print("Your total score is:", score,"Awesome try")
elif score == 3:
    print("Almost there")
elif score == 4:
    print("Your total score is:", score,"Now you know how it feels to lose by one run")
elif score == 5:
    print("Your total score is:", score,"Cheers!! You win the quest")
