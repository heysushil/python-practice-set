def qoutes(name, qoute):
    print('\n\n {} once said, "{}"'.format(name.lstrip(), qoute))
    print(2 + 3*4)


name = input('Enter Lengend\'s name: ')
qoute = input('Enter Qoute: ')
qoutes(name.title(), qoute.upper())

