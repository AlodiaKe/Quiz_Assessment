import random

# Questions and answers stored in dictionary
q_and_a = {
    "maths": {
        1: "What is the sum of angles on a straight line: ",
        2: "The vertex form formula for a parabola?  a) y = a(x-b)(x-c)  b) y = a(x-b)^2 + c: ",
        3: "If the function passes through the point (1,14), what is the value of 'c'? y = (x+2)^2 + c: ",
        4: "What is the sum of angles in any triangle: ",
        5: "What is the rule for Co-interior angles? a) Co-int. angles are equal b) Co-int. angles add to 180: ",
        6: "What is the rule for corresponding angles? a) Corr. angles are equal  b) Corr. angles add to 180: ",
        7: "What's the 'vertex' of a parabola? a) The point for the axis of symmetry  b) the point on the x-axis: ",
        8: "What is the y-intercept of the line given by the equation y = 3x + 2: ",
        9: "What number does the gradient represent in the equation y=5x+11: ",
        10: "Opposite angles in a cyclic quadrilateral add up to ___: ",
        11: "A radius and a tangent form a... a) 45° angle  b) 90° angle: ",
        12: "Extra hard question! What is the shape of this loci? |z+2| <= 3: ",
        "answers": {
            1: 180,
            2: "b",
            3: 5,
            4: 180,
            5: "b",
            6: "a",
            7: "a",
            8: 2,
            9: 5,
            10: 180,
            11: "b",
            12: "circle"
        }

    },
    "science": {
        1: "What is the name of the 6th element on the periodic table: ",
        2: "What gas is produced when a metal reacts with an acid: ",
        3: "In written form, what is the first diatomic element: ",
        4: "What is the name of a substance that enables a chemical reaction to proceed at a faster rate: ",
        5: "What is the powerhouse of the cell: ",
        6: "What is the name for the ion CO₃²⁻: ",
        7: "What is the chemical formula for water: ",
        8: "Name the process by which plants make their food: ",
        9: "What gas is tested in the 'pop' test: ",
        10: "What liquid is produced when an acid reacts with a base: ",
        "answers": {
            1: "carbon",
            2: "hydrogen",
            3: "hydrogen",
            4: "catalyst",
            5: "mitochondria",
            6: "carbonate",
            7: "h2o",
            8: "photosynthesis",
            9: "hydrogen",
            10: "water"
        }
    },
    "english": {
        1: "What is the Samoan name for a white person (Dawn Raids Study): ",
        2: "What is the name of this language feature: Bob was as tall as a tree: ",
        3: "What language feature is in this example: The snake hissed and slithered:  ",
        4: "What is the name for a paragraph in poetry: ",
        5: "What is the name of this language feature: I'm so hungry I could eat an elephant: ",
        6: "Which language feature is referencing a historical event, person, place etc? a) allusion  b) illusion: ",
        7: "Which example is a simile? a) fat as a cow  b) CRUNCH! SLAM!: ",
        8: "Which repeated sound is found in assonance? a) 's'  b) 'i': ",
        9: "what language feature is about exaggerating something: ",
        "answers": {
            1: "palangi",
            2: "simile",
            3: "sibilance",
            4: "stanza",
            5: "hyperbole",
            6: "a",
            7: "a",
            8: "b",
            9: "hyperbole"
        }
    },
    "double science": {
        1: "What is the name (plural) of the finger-like projections that increase the SA of absorption: ",
        2: "What is the other name for chewing: ",
        3: "How many parts of the small intestine are there: ",
        4: "The name for muscle contractions that move food and fluids through the digestive tract: ",
        5: "Name the first part of the small intestine: ",
        6: "What is the range for the pH of the mouth? a) 1-2  b) 7-8: ",
        7: "What is the range for the pH of the stomach? a) 1-2  b) 7-8: ",
        8: "What is the range for the pH of the small intestine? a) 1-2  b) 7-8: ",
        9: "Which respiration produces 38 ATPs? a) Aerobic Respiration  b) Anaerobic Respiration: ",
        10: "Which respiration will result in an 'oxygen debt'? a) Aerobic Respiration  b) Anaerobic Respiration: ",
        11: "What is the name of the universal energy currency in the body: ",
        12: "What molecule does Amylase break down (in the small intestine): ",
        13: "Many Herbivores don't have canines, and instead have a large gap behind the incisors. What is it called: ",
        14: "True or False? Antibiotics only work on viruses: ",
        "answers": {
            1: "villi",
            2: "mastication",
            3: 3,
            4: "peristalsis",
            5: "duodenum",
            6: "b",
            7: "a",
            8: "b",
            9: "a",
            10: "b",
            11: "atp",
            12: "maltose",
            13: "diastema",
            14: "false"
        }
    },
    "digi tech": {
        1: "What is the index of the first item in a list: ",
        2: "What is the index of the fifth item in a list: ",
        3: "What module would you use to generate random numbers: ",
        4: "What symbols would you use to make a dictionary? a) {}  b) []: ",
        5: "What does .pop() do? a) removes the first value of the list  b) removes the last value of the list: ",
        6: "What does .append() do? a) adds a value onto the end of the list  b) removes a value from the list: ",
        7: "What symbols are used to indicate commenting? a) %  b) #: ",
        8: "What symbol is used for exponents? a) *  b) **: ",
        9: "Which comes first? a) if  b) elif: ",
        "answers": {
            1: 0,
            2: 4,
            3: "random",
            4: "a",
            5: "b",
            6: "a",
            7: "b",
            8: "b",
            9: "a"
        }
    },
    "history": {
        1: "What was the last name of the president that gave the Gettysburg address: ",
        2: "What year was Harriet Tubman born: ",
        3: "What year was the Fugitive Slave Act created: ",
        4: "Which New Zealand money note has the leading woman in the woman suffrage on (in $) (value only): ",
        5: "What is the name of the rugby team that's tour resulted in protests in the 1980's: ",
        6: "What is the name of the Maori chief that was Hone Heke's main ally during the Northern Wars: ",
        "answers": {
            1: "lincoln",
            2: 1822,
            3: 1850,
            4: 20,
            5: "springboks",
            6: "kawiti"
        }
    }
}

exit = False
EMPTY_STRING = ""
total_score = 0
lives = 10
MINIMUM_SCORE = 1
LOSE_GAME = 0
CHOICE_OPTIONS = ["a", "b"]
MAX_QUESTIONS_ASKED = 10
BAD_RATING = range(1, 4)
AVERAGE_RATING = range(4, 7)
GOOD_RATING = range(7, 11)

# Explaining the rules
print("Welcome to the MAGS quiz! \n")
print("Before you start, please read the rules CAREFULLY: \n")
print("Answer multichoice answers with the letter option, not the actual answer")
print("Each round, 10 questions will be asked, and you will get a score out of 10.")
print("You will start with 10 lives, and every time you answer incorrectly you lose a life")
print("You will be kicked from the quiz once all 5 lives are lost")
print("Type 'exit' to leave")
print("READ QUESTIONS PROPERLY... \n")
print("Enjoy the quiz :) \n")

# Program asks and stores what subject the user wants to be quizzed on
while not exit and lives > LOSE_GAME:
    questions_asked = 0
    round_score = 0
    print("You have " + str(lives) + " lives")
    print("Your current score is " + str(total_score))
    print("The subjects to play are: Maths, Science, English, Double Science, Digi Tech, and History.")
    subject_choice = input("Please choose a subject to be quizzed on, or type exit to exit quiz: ").lower()

    # If an empty string is given
    while subject_choice.strip() == EMPTY_STRING:
        print("\nPlease provide an answer.\n")
        subject_choice = input("Please choose a subject to be quizzed on, or type exit to exit quiz: ").lower()

    # If the player chose a subject that can be quizzed
    if subject_choice in q_and_a:
        question_exit = False
        print("\nTYPE EXIT AT ANYTIME TO LEAVE THE QUESTION \n")

        while not question_exit and lives > LOSE_GAME:

            # The minimum and maximum number for randomly generated questions
            MIN_QUESTIONS = 1
            max_questions = len(q_and_a[subject_choice]) - 1

            # Randomly generating a question
            valid_input = False
            question_num = random.randint(MIN_QUESTIONS, max_questions)
            question = q_and_a[subject_choice][question_num]
            answer = input(question).lower()

            # Question asked and answer given
            if answer != "exit":
                correct_answer = q_and_a[subject_choice]["answers"][question_num]

                # Handling invalid input when an integer is expected
                if type(correct_answer) == int:
                    while not valid_input:
                        if not answer.isdigit():
                            print("\nInvalid input. Please enter an integer.\n")
                            answer = input(question).lower()
                        elif answer.isdigit():
                            answer = int(answer)
                            valid_input = True

                # Handling invalid input when a string or a multichoice option is expected
                elif type(correct_answer) == str:
                    while not valid_input:
                        if not answer.isalpha():
                            print("\nInvalid input. Please enter a string.\n")
                            answer = input(question).lower()
                        elif correct_answer in CHOICE_OPTIONS and answer not in CHOICE_OPTIONS:
                            print("\nInvalid input. Please enter a multichoice option (a or b).\n")
                            answer = input(question).lower()
                        elif correct_answer in CHOICE_OPTIONS and answer in CHOICE_OPTIONS:
                            valid_input = True
                        elif answer.isalpha():
                            valid_input = True

                # Checks whether the answer is correct or incorrect
                if answer == correct_answer:
                    print("\nThat's correct! Well done!\n")
                    total_score += 1
                    round_score += 1
                    questions_asked += 1
                else:
                    print("\nThat's wrong! The answer was " + str(correct_answer) + "\n")
                    lives -= 1
                    questions_asked += 1

            # Exiting round
            elif answer == "exit":
                while not question_exit:
                    print("\nAre you sure you would like to exit? (y/n)")
                    exit_question = input().strip().lower()
                    if exit_question == "y":
                        print("You have left this question \n")
                        question_exit = True
                    elif exit_question == "n":
                        print("Continuing with questions... \n")
                        break
                    else:
                        print("Error, please enter y or n.")

            # Displaying round score and exiting round
            if questions_asked == MAX_QUESTIONS_ASKED:
                print("Congrats you scored " + str(round_score) + "/10! \n")
                question_exit = True

    # Exiting quiz and displaying final score
    elif subject_choice == "exit":
        while not exit:
            print("\nAre you sure you would like to exit? (y/n)")
            exit_quiz = input().strip().lower()

            # If the user exits
            if exit_quiz == "y":
                exit = True
                print("Your final score was " + str(total_score) + " points!")
                if total_score < MINIMUM_SCORE:
                    print("Better luck next time \n")
                elif total_score >= MINIMUM_SCORE:
                    print("Well done! \n")

                # Rating the quiz
                valid_rating = False
                while not valid_rating:
                    try:
                        quiz_rating = int(input("On a scale of 1-10, how much did you enjoy this quiz? "))

                        if quiz_rating in BAD_RATING:
                            print("Oh no, I'm sorry to hear you had a bad experience! Hope you have fun next time!")
                            valid_rating = True
                        elif quiz_rating in AVERAGE_RATING:
                            print("Ok.. at least you didn't HATE the quiz. Have a nice day.")
                        elif quiz_rating in GOOD_RATING:
                            print("Nice that you enjoyed the quiz! Have a good day!")
                            valid_rating = True
                        else:
                            print("Sorry, that value is out of range. Please enter an integer between 1-10\n")

                    except ValueError:
                        print("Sorry, that wasn't an integer. Please enter an INTEGER between 1-10\n")

                break

            # If the user doesn't exit
            elif exit_quiz == 'n':
                print("Continuing with questions... \n")
                break

            else:
                print("Error, please enter y or n.")

    # If the player's subject choice isn't a subject that can be quizzed
    else:
        print("\nError, that wasn't a subject option that can be quizzed on. \n")

# If the player lost all 5 lives
if lives <= LOSE_GAME:
    print("\nOh no! You have lost all your lives!")
    print("Your final score was " + str(total_score) + " points!")
    print("Better luck next time!")
