# Built-in Data Types


# Questions to learn
'''
1. what is librarys and what is librarys in python?
2. what is framwork? Why we use it?
3. Few tranding python framworks?
4. Few javascript framworks?
'''

'''
Text type:
    str - yaha sirf string type hi hota hai text ke liye
        c and c++ me char bhi hota hai jo sirf single character ko store karta hai
        but python me sab kuch string me store hota hai

Example:
'''
name = "Subham"
print('Name: ',name)

'''
Numeric Type:
    int - accept interger value
    float - accept decimal
    complex - use j to make the number complex like a = 1j

Example:
'''
intvalue = 5
flotvalue = 5.5
print('\nIntiger value: ',intvalue)
print('Float value: ',flotvalue)

'''
Sequence Types:
    list - [] - list store values in index form. Always store single values in each index.
    tuple - 
    range - 

    Note: Array - 
        index array (single dimetion array)
        associative array (two dimetion array)
            Exampel of Assoc - array('name'=>'Raja')
        multi dimention array

Example:
'''

# List - It's hold index orderd values. It's changable
listvalue = ['Subham','Raja','Pawan']
print('\n',type(listvalue))
print('Index value of listvalue: ',listvalue[1]) # listvalue[1] shows a index 1 postion value
print('Listvalue : ',listvalue)

# Tuple - It's also holds index orderd values. It's not changable
'''
PHP Loop Case:

    intialization;condition;increment/decrement

    for($i=0; $i<=10; $i++){
        print($i);
    }

Python Loop Case:

    intialization;condtion+increment/decrement
    
    for i in listvalue:
        print(i)
'''
tuplevalue = ('Tuple 1','Tuple 2','Tuple 3')
print('\n',type(tuplevalue))
print('Tuplevalues 0 index postion: ',tuplevalue[0])
print('Values to tuple: ',tuplevalue)

# Range - It's proide range from start inter value to stop integer value
rangevalue = range(0,6)
print('\n',type(rangevalue))
print(rangevalue)

# Dictonary - It's a collection of key and value pares
dictonaryvalue = {'Name':'Subham','Course':'B.Tech','Location':'India'}
print('\n',type(dictonaryvalue))
print('Name of candidate is: ',dictonaryvalue['Name'])
print('Dictonary values :',dictonaryvalue)

# SET - It's collection of data and unordered form
# setvalue = {1,2,3,4,5}
setvalue1 = {'a','e','i','o','u'}
print('\n',type(setvalue1))
# print('Set values: ',setvalue)
print('Set values: ',setvalue1)

# Homwwork
'''
1. convet int,float values
2. print multiline string
3. slice stirng
4. string value postion output
5. Using list print 5 cars, 5 car companys and 5 car brands. Then use format in print to show the output like - 'My car is 'carname' and its belong to 'companyname' and the brand of my car is 'carbrand'.'
6. Using dictonary create your details like - name,mobile,email,cours,address,mothername,fathername. Then show output using format in print as a paragraph with dictonary values.
'''