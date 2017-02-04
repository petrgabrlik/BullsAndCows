#!/usr/bin/python3

# Bulls and cows game
# Author: Petr Gabrlik
# Email: petrgabrlik@email.cz
# Date: 18.1.2017

import random


def main():
    # The game
    dn = 4
    print("""Hi there!
Let's play a bulls and cows game.""")

    while True:
        # Game loop
        rann = rngen(dn)
        print("(Secret number, for debugging only: " + str(rann) + ")")
        print("I've generated a random {:}-digit number for you.\nGuess that number".format(dn))

        guess = 1
        while True:
            # Guess loop
            usrn = usrinput(dn)
            if rann == usrn:
                print("Correct, you've guessed the right number in {:} {:}!".format(guess, 'guess' if guess == 1 else 'guesses'))
                print("That's {:}.".format(evaluation(guess)))
                name = input("Enter your name: ")
                saveresults(name, guess)
                print("\n**** RESULTS ****")
                print(open("results.txt", "r").read())
                break
            else:
                guess += 1
                bulls, cows = 0, 0
                for num in range(dn):
                    if str(usrn)[num] == str(rann)[num]: bulls += 1
                    elif str(usrn)[num] in str(rann): cows += 1
                print('{:} {:}, {:} {:}'.format(bulls, 'bull' if bulls == 1 else 'bulls', cows, 'cow' if cows == 1 else 'cows'))

        # Play again?
        again = ''
        while not (again == 'Y' or again == 'N'):
            again = input('Do you want to play again? (Y/N) ').upper()
        if again == 'N':
            print('Thank you for playing! Bye bye.')
            break


def rngen(n):
    # Generates n-digit integer, without repeating numbers
    rn = []
    while len(rn) < n:
        newnum = ( str(random.randint(0,9)) )
        if newnum not in rn and not (len(rn) == 0 and int(newnum) == 0): rn.append(newnum)
    return int(''.join(rn))


def usrinput(n):
    # Reads user's 4-digit integer, repeating numbers is not allowed
    while True:
        try:
            usrn = abs(int(input(">>> ")))
            if len(str(usrn)) > n: print('Too long. Please enter {:}-digit integer.'.format(n))
            elif len(str(usrn)) < n: print('Too short. Please enter {:}-digit integer.'.format(n))
            elif True in [True for num in str(usrn) if str(usrn).count(num) > 1] : print('Numbers must not be repeated.')
            else : break
        except:
            print('Invalid number. Please enter {:}-digit integer.'.format(n))
    return usrn

def evaluation(n):
    # Evaluates results
    return {1<=n<4: 'amazing', 4<=n<10: 'really good', 10<=n<20: 'average', 20<=n: 'not so good'}[1]

def saveresults(name, guess):
    # Saves results to file
    try:
        open("results.txt", "r")
    except:
        print("NAME", "GUESSES", sep="\t", file=open("results.txt", "a"))
    print(name, guess, sep="\t", file=open("results.txt", "a"))

if __name__ == "__main__":
    main()
