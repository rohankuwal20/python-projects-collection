#quiz game
questions=("Q1. Which is the only country in the world that borders both the Caspian Sea and the Persian Gulf?",
           "Q2. Which ancient civilization constructed the architectural wonder known as Machu Picchu?",
           "Q3. What is the most abundant gas in Earth's atmosphere?",
           "Q4. Who is the author of the classic dystopian novel 1984?",
           "Q5. In which city can you visit the famous Louvre Museum?",
           "Q6. How many pockets are there on a standard, professional snooker table?",
           "Q7. From which plant is traditional Japanese wasabi paste made?"
           )
options= (("A)Iraq"," B)Iran", "C)Saudi Arabia","D)Turkmenistan"),
          ("A)The Aztecs ","   B)The Mayans ","  C)The Incas ","   D)The Olmecs"),
          ("A)Oxygen ","   B)Carbon Dioxide ","  C)Hydrogen ","    D)Nitrogen"),
          ("A)George Orwell "," B)Aldous Huxley ","    C)Ray Bradbury","  D)H.G. Wells"),
          ("A)Rome ","  B)Paris ","    C)London ","   D)Amsterdam"),
          ("A)4","  B)6 ","    C)8  ","   D)10"),
          ("A)Horseradish root ","  B)Mustard seed "," C)Wasabia japonica stem ","    D)Green chili pepper")
)
answers=["B","C","D","A","B","B","C"]
guesses=[]
score=0
question_num=0

for question in questions:
    print("-----------------------------------")
    print(question)
    for option in options[question_num] :
        print(option,end=" ")
    print()
    run=True
    while run:
        guess=input("Answer with (A,B,C,D):").upper()
        if guess=="A" or guess=="B" or guess== "C" or guess=="D" :  
            guesses.append(guess)
            run=False

            if guess==answers[question_num]:
                print("your guess is correct")
                score += 1
            else:
                print("your guess is wrong")
                print(f"correct answer is {answers[question_num]}")
                score -+1
            question_num +=1
        else :
            print("invalid choice")
print("----------------result-----------------")
print("ANSWERS :")
for answer in answers:
    print(answer,end=" ") 
print()
print("-----------------------------------")
print()
print("GUESSES :")
for guess in guesses:
    print(guess,end=" ")      
score = int((score/len(questions))*100)
print()
print("-----------------------------------")
print()
print(f"your score is {score}% !")
