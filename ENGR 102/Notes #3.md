# Notes



\n - prints the spring after that symbol in a new line

\t - prints a tab

## Different data types
- string   Ex. "True"
- Floating- point   Ex. "3.0 or 2/3"
- Integer    Ex: "3"

## Floor division
will always give the whole number and no remainder

    print(3//2)
    print(The answer will equal only 1")

## Type and behavoir - putting strings together
1. adding two strings together

When adding two strings together, python will place two of the string number and place them next to each other

    x = "1" + "1"
    print (x)

Output 

    11

2. multiplying integer with a string

When

    x = "1" * 2
    print(x)

Output: 

    11

## Converting types of data
1. Float to integers
2. Integer to float

### Float to integer
- the value will be truncated when going from float to integer

The function `int()`will convert whatever is inside to be to a integer. There will be no decimal

    x = int(2.0)
    y = int(-1.9 )
    print()
Output: 
    2

### Converting from strings to ints or Float

    int('3')
    float('3.14')
    float('2)
    int('2.5')
    int(float('2.5'))

output: 

    3
    3.14
    2.0
    error
    2


The `int('2.5')` function will produce an error message because it cannot do two steps at the same time

### Number to String

The command to convert number to string is `str()`

    str(1)
    str(2.5)
    str(1/2)
    str(2*10)

Output: 
    '1'
    '2.5'
    '0.5'
    '20'

3. Python will compute the decimal value of 1/2 and them print 0.5 in a string, with quotation marks

### Boolean Conversion 
Boolean: it is a true or false word

    x = True
    y = int(x)
    print(y)

Output: 
    1

True in the Boolean world almost always equal 1 in the python world

The `bool()` function can be used to convert an integer to a boolean

    x = 1
    y = bool(x)
    print(y)

Output: 
    True


*The only instance will x will produce a false is when a string has empty quotation marks or x = 0 *

Code: 
    x = ""
    y = bool(x)
    print(y)

    x = 0
    y = bool(x)
    print(y)

Output: 
    false
    false

Similarity, if you con

Example (Quiz Question):

    str(float(str(3/2) + str(int(3/2))))* int(int(str(2) + str(7)/int(10.3)))

Output: 

    '1.511.51'


## Basics of Print Function
Switching from printing number to strings or strings to numbers, use a `,` comma

<b> Commas will automatically print a space</b>

Code: 

    print(5, "is spelled five.")

Output: 

    5 is spelled five.

Example:
    x = 3
    y =4
    print( str(x), "is not", str(y))

Output: 

    3 is not 4

## Seps = '' and End = ''
- stand for separation 
- tells when the print statement ends

    print("Test", 2, 3, sep = ',', end = ':')
    print(15)

Output

    Test 2 3, : 15

## f strings (slide 36)
- print number in varying degree of precision

Code: 
    print(f'Test {3} {5}')
    print(f' Test, {3} {5}')
    print(f' Test, {3}, {5}: {3*5'})

Output: 

    Test 3 5
    Test, 3, 5
    Test, 3, 5: 15


## Input and Output

`input()` will allow the user to input whatever value they want

Code: 

    x = input()
    print(x)

Output: 

    # ask for input, put in 2
    2

Including a string in the input functionm

    x = input("Please Enter a number:, ")
    y = 2*x
    print("Double you number is", y)

Output: 

    Please Enter a number: # 3
    Double your number is 6


Converting your input as to an integer

Code: 

     x = int(input("Enter a number: "))
     y = 2*x
     print("Double your number is", y)

Output: 

    Enter a number: # 2.4
    Double your number is 4

Converting your input to a float 


## Functions: 
Defining a function in python and giving it a name require a `def`

code: 

    def name (parament):
    #function and stuff under

Code Example: 

    def howdy():
        print("Howdy!")


Output:

       # it print nothing

Inorder to use the function, you must call the function from outside the function

Code: 
    def howdy():
        print("Howdy!")

    Howdy()

Output: 

    Howdy!

To print a statement multiple times:

Code:
 
    def howdy(a):
        print("Howdy!")
    Howdy(3)

Output: 

    Howdy!Howdy!Howdy!

Overriding a default set paramenter: 
If you set the default of the number of howdys you want to produce (2), you can override that default by inputing another number when calling the function 

Code:

    def howdy(a = 3):
        print("Howdy!")

    Howdy(2)

Output: 

    HowdyHowdy
