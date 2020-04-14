# Solution of BASIC FOLDER'S Questions

### 1. Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

    num = int(input("Please choose a number to divide: "))

    listRange = list(range(1,num+1))

    divisorList = []

    for number in listRange:
        if num % number == 0:
            divisorList.append(number)

    print(divisorList)


### 2. Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

    wrd=input("\nPlease enter a word")
    wrd=str(wrd)
    rvs=wrd[::-1]
    print('\nRiverse: ',rvs)
    if wrd == rvs:
        print("\nThis word is a palindrome")
    else:
        print("\nThis word is not a palindrome")


> A sample solution using for loops

    def reverse(word):
        x = ''
        for i in range(len(word)):
            x += word[len(word)-1-i]
        return x

    word = input('give me a word:\n')
    x = reverse(word)
    if x == word:
        print('This is a Palindrome')
    else:
        print('This is NOT a Palindrome')


### 3. Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [number for number in a if number % 2 == 0]

    print('\n',b)

> For a solution that uses the random library to generate test lists, check this out:

    import random

    numlist = []
    list_length = random.randint(5,15)


    while len(numlist) < list_length:
        numlist.append(random.randint(1,75))
        

    evenlist = [number for number in numlist if number % 2 == 0] 

    print('\n',numlist)
    print('\n',evenlist)


### 4. Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

    Remember the rules:

            Rock beats scissors
            Scissors beats paper
            Paper beats rock
        
        Try to use:
            
            While loops
            Infinite loops
            Break statements

> Code start from here

    import sys

    user1 = input("Enter Your Nmae: ")
    user2 = input("Enter Your Friends Name: ")
    user1_answer = input("%s, do yo want to choose rock, paper or scissors? " % user1)
    user2_answer = input("%s, do you want to choose rock, paper or scissors? " % user2)

    def compare(u1, u2):
        if u1 == u2:
            return("It's a tie!")
        elif u1 == 'rock':
            if u2 == 'scissors':
                return("Rock wins!")
            else:
                return("Paper wins!")
        elif u1 == 'scissors':
            if u2 == 'paper':
                return("Scissors win!")
            else:
                return("Rock wins!")
        elif u1 == 'paper':
            if u2 == 'rock':
                return("Paper wins!")
            else:
                return("Scissors win!")
        else:
            return("Invalid input! You have not entered rock, paper or scissors, try again.")
            sys.exit()

    print('\n',compare(user1_answer, user2_answer))        

> Another sample solution uses a clever way of checking the winner:

    print('''Please pick one:
                rock
                scissors
                paper''')

    while True:
        game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
        player_a = str(input("Player a: "))
        player_b = str(input("Player b: "))
        a = game_dict.get(player_a)
        b = game_dict.get(player_b)
        dif = a - b

        if dif in [-1, 2]:
            print('\nPlayer a wins.')
            if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                continue
            else:
                print('\nGame over.')
                break
        elif dif in [-2, 1]:
            print('\nPlayer b wins.')
            if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                continue
            else:
                print('\nGame over.')
                break
        else:
            print('\nDraw.Please continue.')
            print('')


### 5. Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

    import random

    number = random.randint(1,9)
    guess = 0
    count = 0


    while guess != number and guess != "exit":
        guess = input("What's your guess?")
        
        if guess == "exit":
            break
        
        guess = int(guess)
        count += 1
        
        if guess < number:
            print("\nToo low!")
        elif guess > number:
            print("\nToo high!")
        else:
            print("\nYou got it!")
            print("\nAnd it only took you",count,"tries!")

> And another:

    import random

    rd = random.randint(1,9)
    guess = 0
    c = 0
    while guess != rd and guess != "exit":
        guess = input("Enter a guess between 1 to 9")

        if guess == "exit":
            break

        guess = int(guess)
        c += 1

        if guess < rd:
            print("\nToo low")
        elif guess > rd:
            print("\nToo high")
        else:
            print("\nRight!")
            print("\nYou took only", c, "tries!")
    input()

> And another, with lots of helpful text!

    import random

    # Awroken

    MINIMUM = 1
    MAXIMUM = 9
    NUMBER = random.randint(MINIMUM, MAXIMUM)
    GUESS = None
    ANOTHER = None
    TRY = 0
    RUNNING = True

    print "Alright..."

    while RUNNING:
        GUESS = raw_input("What is your lucky number? ")
        if int(GUESS) < NUMBER:
            print "Wrong, too low."
        elif int(GUESS) > NUMBER:
            print "Wrong, too high."
        elif GUESS.lower() == "exit":
            print "Better luck next time."
        elif int(GUESS) == NUMBER:
            print "Yes, that's the one, %s." % str(NUMBER)
            if TRY < 2:
                print "Impressive, only %s tries." % str(TRY)
            elif TRY > 2 and TRY < 10:
                print "Pretty good, %s tries." % str(TRY)
            else:
                print "Bad, %s tries." % str(TRY)
            RUNNING = False
        TRY += 1





![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)