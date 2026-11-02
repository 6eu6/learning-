#Day one of returning, Short in Dictionries

Words = {"Hair": 4, "Pair": 4,"Chair": 5}

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C H G")

    while len(Words) > 0:
        print (f"{len(Words)} Words left!")
        guess = input("Guess a word:")
        
        #Check if guess in dictionary
        if guess in Words.keys():
            points = Words.pop(guess)
            print(f"Good job! You scord {points} points")
main()
