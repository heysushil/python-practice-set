# Solution of BASIC FOLDER'S Questions

## 1. Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

    num = int(input("Please choose a number to divide: "))

    listRange = list(range(1,num+1))

    divisorList = []

    for number in listRange:
        if num % number == 0:
            divisorList.append(number)

    print(divisorList)


## 2. Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

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


## 3. Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [number for number in a if number % 2 == 0]

    print('\n',b)


        

![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)