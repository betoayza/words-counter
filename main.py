words = input("-------\nWelcome to Words Counter!\nPlease, enter a phrase [-1 to exit]: ")

while words != "-1":
    try:
        int(words)        
        words = input("Not number allowed, try again... [-1 to exit]: ")

    except ValueError:

            counter = len(words.split()) 
            print("The phrase has:", counter, "words!")

            words = input("Very good, try other phrase [-1 to exit]: ")

print("Thanks, come back later!")
