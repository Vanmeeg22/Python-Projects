from time import *
import random as r

def mistake(para_test, userinput_test):
    error = 0
    for i in range(len(para_test)):
        try:
            if para_test[i] != userinput_test[i]:
                error =+ 1
        except:
            error =+ 1
    return error

def speed_time(time_start, time_end, userinput):
    time_delay = time_end - time_start
    time_roundoff = round(time_delay, 2)
    speed = len(userinput) / time_roundoff
    return round(speed)

if __name__ == '__main__':
    while True:
        print()
        check = input("Are you ready to test your typing speed? Type: Yes / No :")
        if check == "Yes":
            test = ["Artificial intelligence (AI), in its broadest sense, is intelligence exhibited by machines, particularly computer systems.",
                    "It is a field of research in computer science that develops and studies methods and software that enable machines to perceive their environment and uses learning and intelligence to take actions that maximize their chances of achieving defined goals.[1] Such machines may be called AIs.",
                    "Alan Turing was the first person to conduct substantial research in the field that he called machine intelligence.[5] Artificial intelligence was founded as an academic discipline in 1956.",
                    "The field went through multiple cycles of optimism,[7][8] followed by periods of disappointment and loss of funding, known as AI winter."]

            test1 = r.choice(test)

            print()
            print("TEST YOUR TYPING SPEED BY TYPING THE TEXT GIVEN BELOW:")
            print()
            print(test1)
            print()

            time_1 = time()
            testinput = input(" Enter: ")
            time_2 = time()

            print()
            print("Speed: ", speed_time(time_1, time_2, testinput), "word/sec")
            print("Error: ", mistake(test1, testinput))
        elif check == "No":
            print()
            print("Thank you for testing yourself with us!")
            print()
            break
        else:
            print()
            print("Please enter either 'Yes' or 'No' only.")
            continue