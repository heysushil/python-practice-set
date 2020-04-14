# Solution of python_basic_excercise.py in Basic folder

1. Exercise 1 (and Solution)
> Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

        num = int(input("Please choose a number to divide: "))

        listRange = list(range(1,num+1))

        divisorList = []

        for number in listRange:
            if num % number == 0:
                divisorList.append(number)

        print(divisorList)


2. Exercise 2 (and Solution)
> Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

    wrd=input("\nPlease enter a word")
    wrd=str(wrd)
    rvs=wrd[::-1]
    print('\nRiverse: ',rvs)
    if wrd == rvs:
        print("\nThis word is a palindrome")
    else:
        print("\nThis word is not a palindrome")


![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)