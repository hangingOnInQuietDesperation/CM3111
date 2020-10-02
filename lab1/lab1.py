# Simple maths and output formatting
x = 3
y =10.5
Msg = 'Result'
fx = x+y * 10 ** 2 
print("The Result is ", fx)
print(f'The {Msg} is {fx}')
print (f'The modulo operation in Python is %, so for e.g. 10%3 is {10%3}')

#Lists, sub lists, and slices
my_lst = [1,2,3,4,5,6,7,8,9,10]
print('First element in the list is ', my_lst[0])
print('List element in the list is ',my_lst[len(my_lst)-10])
sub_lst = my_lst[2:4]
sub_lst
my_lst[:1]
my_lst[1:]
my_lst[-1:]
my_lst[:-1]

#Strings
msg = 'Welcome to RGU'
print(msg[1])
print(f'first character of msg is {msg[0]}')

#Tuples
tuple_example = 1,2,4,10,24
print(tuple_example)
print(tuple_example[0])
print(tuple_example[:2])
print(tuple_example[:3])
print(tuple_example[1:])

#Dictionaries
module_dict = {
        "Code": "CM3111",
        "Name": "Big Data Analysis",
        "Year": 2020,
        "Stage": 3
        }
print(module_dict)

print(f'Module {module_dict["Code"]}')
print(f'Is {module_dict["Name"]}')
print(f'And will be taught to students of Stage {module_dict["Stage"]}')
print(f'And will be delivered in the year {module_dict["Year"]}')
print(module_dict.get('Code'))

for key, value in module_dict.items():
    print (key,':',value)


#Check type of objects
print(type(module_dict))
print(type(tuple_example))
print(type(my_lst))

#Casting
float_v = 1.1
int_v = 1
string_v = 'this is a string'

print(type(float_v))
print(type(int_v))
print(type(string_v))

int_v = float(int_v)
print('The value of int_v is ', int_v)
print('The Type of int_v after casting is ',type(int_v))

#logic
print(1==1)
print(10<9)
print(10>9)
print(10>=9)

small = 10
big = 100
results = ((small < big) and (big%small == 0))
results1 = ((small < big) and (big%small != 0))
results2 = ((small < big) or (big%small != 0))
results3 = ((small > big) or (big%small != 0))

print(f'({small} < {big}) and ({big}%{small} == 0)',result)
print(f'({small} < {big}) and ({big}%{small} != 0)',result1)
print(f'({small} < {big}) and ({big}%{small} != 0)',result2)
print(f'({small} > {big}) and ({big}%{small} != 0)',result3)

#loops
a = 33
b = 200
if b > a:
    print('b is greater than a because ', f"{b} is greater than {a}")
elif b == a:
    print(f"{a} and {b} are equal")
else:
    print(f"{a} is greater than {b}")

i = 1
while i < 10:
    print(f'{i} squared is {i**2}')
    i++




