'''
about itern and next:

1. __iter__ and __next__ are using by default and also when using the for loop using list, tuple, dic or set all are iteration and for loop are using these two methos to iterate the loop.
2. also impiment the class and method to do the same work by these methods
'''

class Iter:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = Iter()
myiter = iter(myclass)

for i in myiter:
    print(i)
