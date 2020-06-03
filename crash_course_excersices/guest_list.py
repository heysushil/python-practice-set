guestlist = ['suraj','sangoo','sunil','surender','papa']
guestlist.append('mom')
guestlist.append('arti')
guestlist.append('preeti')

# out table is big and invide few more persons
guestlist.insert(0, 'shivang')
guestlist.insert(6, 'suyash')
j = 0
for i in guestlist:
    if j < 3:
        print('Mr. ' + i.title() + ', I\'m inviting you for dinner at eveining 8 PM.')

    if j > 2 and j <= 5 :
        print('Mr. ' + i.title() + ', I here that you are not comming for dinner.')
    if j > 5:
        print('Hello ' + i.title() + ', Welcome to familiy party.')
    j += 1

print('\n\n')
# remove all personas and invide only 2
j = 0
for i in guestlist:
    if j > 1:
        del guestlist[j]

    else:
        print('\nThis is final invitation to ' + i.title() + ', kindly join and enjoy.')
    
    print('Member ' + str(j) + ' Name: ',i)
    j += 1

del guestlist
print('No more patry')


# list append how to work
oldlist = ['heera','meeta','seela']
newlist = []

while oldlist:
        user = oldlist.pop()

        print('Verifining user: ',user.title())
        newlist.append(user)

# confirment user
print('\nTHeis is new list: ')
for confirms in newlist:
    print('\nConfirmuser: ',confirms.title())


