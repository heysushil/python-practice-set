import re

x = 'hello sushil how are you'
print(re.search('^hello.*youa$',x))

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

x = re.split('i',txt, maxsplit=1)
print(len(x))
for i in x:
    print(i)

# try exception 

try:
    print(n)
except NameError:
    print('n is not defined')
except:
    print('something else happend')
else:
    print('No probelm on code')
finally:
    print('try except bloack ended')


# tring to use try with file

try:
    f = open('doc.txt')
    f.write('hello sushil')
except:
    print('problem arrise when tring to write on file')
else:
    print('files work done')
finally:
    # f.close()
    print('finish file work finally')

#  rise error
z = -1
if z < 5:
    raise Exception('no less than zero allow')
    

