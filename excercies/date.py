import datetime as dt

date = dt.datetime.now()
print('date: ',date)
print('year: ',date.year)
print('month: ',date.month)
print('day: ',date.day)
print('hours: ',date.hour)
print('Minut: ',date.minute)
print('sec: ',date.second)
print('micro sec: ',date.microsecond)


# datetime
datetime = dt.datetime(2020, 6, 1)
print(datetime)


# string 
'''
A reference of all the legal format codes:

Directive	Description	Example	Try it
%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
'''

week = date.strftime('%A')
print('Week: ',week)



'''
HW
1. create a funciton in which show user info like: name, email, address, course and also get current date and time seperatly of registraion and then after successfully registraed show all registraion detisl to use and at the last show thank you message for registraion

2. create a user admission with following parameters: name, father name, mother name, course, joining date, birthdate. for birthdate use datetime library. at the last using funciton recive all student registraion variables in singel argument and then show them.

3. create a function to ask for user birthday after that show user a proper formated birthday date like as: 
userinput: 1990-05-28
formate: Your Birthd Day is 28, Your birthday Month is May and Your birth year is 1990
'''


# print(dt.datetime.)

