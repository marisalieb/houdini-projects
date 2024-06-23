houdini python videos notes

- if you write in the python source editor you need the python shell to see it executed like eg. print statement 

- can create and automate shelf tool by writing code there and just clikcing on the shelf tool, create shelf. create tool, add code in script, click on tool to run it

Hou module: 
- find information by clicking help > contents > python scripting > hou > search node > click on node()

-  this hou.node("/obj").createNode("geo", 'testGeo') will create a geo node with the name testGeo, or this obj.createNode("geo", 'testGeo') if you specified obj = hou.node('/obj')

- you van create all kinds of nodes, just hover over the node and find the name of it in the inforamtion window in ()

Shelf tool example:
import hou
obj = hou.node('/obj')
myGeo = obj.createNode('geo','MYGEO')
box = myGeo.createNode('box', 'mybox')

print(box.asCode())

-print(box.asCode()) give you the code of the box that you just created with the code above



Python data types in Houdini

- numbers; integrers, floats, complex numbers; this print(type(10)) return the class of number in this case integer, 10.2 would be float, 2+5j would be complex 

-this print(type('test01')) returns str for string

- string in sinlge or double quotes

- lists are ordered items, like a storage container of data types so you can store a data type in them, they are in [] and separeted by comma, they can be a combination of data types like this print(type([10, 30.2, 'test02'])) or you can even store a list in a list, then it gets returned as a list

- same with tuples, just put () for tuples instead of [] for lists

- sets: unordered list adn are changeable, but no neccessary order like in lists or tuples, it's just a collection of data, type {} for sets instead of () or []

- dictionariesare a way to store inforamtion, they have a key and a value, you can search by key or look at the indey value, each key stores information for this

- this print(type({'key01' : 'value01'})) would return dict for dictionary

- variables can be used to store information like a = 10, can be numbers, strings ; just have to define a value like myString = 'this is a string'


Numbers in Houdini (more indepth):

- assigning variables x and y and using them with operator basics - addition +, subtraction -, multiplication *, division /, exponentation **, modulo (remainder) %

Like this in a new shelf tool:
# assigning variables
x = 6
y = 10

# operator basics -  +,  -,  *,  /, **, 
print(y % x)



- useful built in python functions for numbers: 

* converting strings to numbers, if x is a string like x = '5' (instead of x = 5, that would be integer) then use print(int(x)+y) to convert  string to integer or to float with float(x)

* rounding to the closest whole number: round(x); careful here to note that this rounds to the closest even number if it's right in the middle like any .5 number, so 3.5 and 4.5 both round to 4
* rounding to a specific decimal point: print(round(x, 1)), this rounds to the closest tenths spot as in one decimal point like 6.1 , closest hundreths sopt would be print(round(x, 2)) so two after decimal point like 6.13


- Math module:

* import math, use functions like math.floor(x) to   round down to the closest lower whole number; math.ceil is the opposite so it round up to the nearest whole number

* other function; abs for getting an absolute number so it gives you the absolute distance from 0, so negative numbers still get returned as positive ones, use the function like this print(abs(x))


Using numbers in Houdini with Python (use this basic script):

# basic example of using numbers with Houdini hou
import hou

#getting the obj context, so basic object/node tree window
obj = hou.node('/obj')

# create a geo node in /obj
myGeo = obj.createNode('geo', 'Geeo')
# the obj in this stands for the obj = defined above

# create a box inside of myGeo
box = myGeo.createNode('box', 'Boxx')

# create variables to use
height = 1
width = 4
depthh =6

# assigning variable to box parameters
box.parm('sizex').set(width)
box.parm('sizey').set(height)
box.parm('sizez').set(depthh)
# if you want to get the parameter names like sizex, hover over the printed name in paramter window

# assigning an expression to the box parameter like center of y (name: ty)
box.parm('ty').set(height/2)





Using strings in Houdini with Python:

- can use multi-line string like this >
"""
this is a multi-line string
"""

- concatention: putting strings together with +, anything inside ' ', like this: print('this' + ' ' + 'is' + 'concatentation'), you can even multiply string so they are printed more than once

- formatting strings with escape characters: 
* such as \n to create a new line, like this >
newLine = 'Line1 \nLine 2\nLine 3'
print(newLine)

* \t to indent string, like this >
tab = '\tIndentttt'
print(tab)

* there are more, like single and double quotes or the backslash escape character


- Formatting with f-strings >
var = 'value'
num = 5
print(f'var is {var} and num is {num}')
- you can use escape character like line break \n within f-strings


- Built-in string functions 

* like convert an object to a string >
number = 1464
print(str(number)) #output is 1464

* or length of a string (including white spaces) like this >
string = "    today is a sunny day   "
print(len(string)) # returns a number, thats the number of characters in that string

* you can remove white spaces of a string like this >
string = string.strip() #add this after your previously defined string, it will stripp all the whitespaces

* make everything lowercase/uppercase/capitalise/title (as in each first letter of a word is capitablised) like this
string = string.lower()
string = string.upper()
string = string.capitalize() #caps first letter of the string
string = string.title()

* replace a word in a string >
string = string.replace("sunny", "rainy")

* split up string based on something inside that string like ' ', like this >
string = string.split(' ') #returns a list with each item separately by what is separated by ' ' so each word in this case

- [0] that is how you get a single object?


- More string functions >

import hou

#get the currently selected node
node = hou.selectedNodes()[0]

# get name of selected node
name = node.name()

#rename with prefix
prefix = 'Out_'

#assign a new name
newName = "myOutNode"

#node.setName(f'{newName}')
node.setName(f'{prefix}{name}')

print(name)


- if you wanted to uppercase the selected node it would look like this > 

import hou

node = hou.selectedNodes()[0]

name = node.name()

prefix = 'Out_'
fullName = f'{prefix}{name}'
nameCaseFix = fullName.upper()

newName = "myOutNode"

node.setName(nameCaseFix)

print(name)





Lists in Houdini:

#create a list of numbers, strings, mixed datat types, etc.

numbers = [1, 3, 5, 7, 9]
print(numbers)
print(numbers[0]) # to get the first item in the list

#to get the last item in the list use [-1]

get length of the list use > (len(numbers))

get smallest number with > print(min(numbers))
get biggest number with > print(max(numbers))

get the sum of the numbers so they are all added together with > print(sum(numbers))

to sort the numbers by numerical value use > sorted(numbers)

to reverse that order > numbers.reverse()

to add to the list > numbers.append() #insert in () what you want to add, like a number or a string, or more?

to remove things from the list (it only removes the first instance of that item in the list) > numbers.remove() #insert in () what you want to remove



connect nodes with python > 

import hou

#get selected objects
selected = hou.selectedNodes()
#at this point it's still a tuple

#convert to list
selected = list(selected)

#set inputs, this connects the nodes, but two items have to be selected in the window
selected[0].setInput(0, selected[1], 0)
#this connects the first item that is selected, connects this one's first input with the secondly selected node and conncets it with this one's first output 

selected[1].setInput(0, selected[2], 0)


print(selected)





Condition Statements:

- there are true/false statements, then only are executed if something is true/false

- using operators with conditions >
x = 5
y = 10

#Greater than 
if x > =:
	print('x is positive')

same with less than <
same with less than/greater than or equal >= <=

a single = sign assigns a value
double == signs actually checks if its equal, so its a comparison

!= means not equal to


- using keyword operators such as 'and' 'or' 'in' 'not in' > 
if x < 0 and y < 0:
	...

#create a list or a string
if 3 in list:
	...


- if, elif, else:
if I understand correctly you use if with else if there are only those two options but you can add a bunch of elif statements but the program will stop at the first elif whose condition has been met so if there are any more elif or else statements they will be ignored, so if there are two or more conditions true it will only return the first one it encounters, but the order is important if you have more than one if statement you need to have all your elif and else statements before you write the next if statement


- easy Houdini example >
import hou

#get selected nodes

selected_nodes = hou.selectedNodes()
selected_nodes = list(selected_nodes)

if len(selected_nodes) > 0:
#print selected nodes
    print(selected_nodes)

else:
    print('No nodes selected')







Loops:

- for loops: takes a list or object that has a range of items/values like numbers in a list
you can create a new item with a for loop so >
number = [1,3,4,5,8,9]
for number in numbers:
	...
#you created number here in the for loop, it represents each of the numbers in the list
this loops over each item/value and exectures whatever is specified for each item (if the conditions apply to this item)

- there is also range, this means you cen specify the start and end and the increments like this > 
for number in range(3, 14, 1)
	print(number)
#this would be the range of 3 to 14 in increments of 1 (excluding 14 though), it breaks the loop at 14 and doesn't run again

if you just say range(6) then it will just start at 0 including 0 but excluding 6

- while loops:
you have a condition and as long as it is met/it is true, it will lop over and execute whatever specified, important is that you have something that breaks this, like this >

number = 1
while number <= 6:
	print(number)
	number += 1
#this means it will increment in each iteration by 1 so you get to the number, in this case 6 that break the loop



simple loop example >

import hou

#get selection,this create a list of nodes which you can later use items from
selection = hou.selectedNodes()

#create variable for x position
x = 0

#start loop, it wil go through the items in the list and they will be held in node as specified
for node in selection:
    #set parameter, txyz is the parameter for the center as you can see if you hover over them
    node.parm('tx').set(x)
    node.parm('ty').set(0)
    node.parm('tz').set(0)
     
    #increment x by 3
    x += 3

#this will make you objects like a bunch of spheres be separate out on the x axis by increments of 3, you need to be able to see all like with a merge node and have them selected



Functions:

- you are creating a blueprint of something to do

- def is how you start of a function, then the name of the function and then any arguments in () and a : to end line; then the indent for the function, and then you unindent to call the function name with any or no arguments and then it will run

basic example >
#function definition
def greet(name):
	print(f'Hello {name}!')

#call function
greet('Marisa')
greet('Tom')

variation would be with a default value as name >

#function definition
def greet(name = 'Lisa'):
        print(f'Hello {name}!')

#call function
greet()
greet('Marisa')
greet('Tom')

#this will execute it with al three names in order


- encapsulation with functions:
anything that is created inside the function stays there, you cant access it from the outside basically


- return:

example >
#Return values
def add(x, y):
    result = x + y
    return(result) # result here holds it as a variable
    
#call the function and print the result
resultt = add(2, 3) #add now has a value which is now equal to the variable we just created (resultt) and then we are printing that value

print(resultt)

you can also run it with default values specified in def add(x =  , y = ) and then run it with an empty result = add(), or you can overwrite it later in the last add()
but carefult here, the positional arguments will run first and then the ones defined with = so add(x = 0, 13) wouldnt work wil with othe way around would




function example >
stage 1, gives you the file names of the textures you want to apply

#automatically apply textures to a material based off of a folder

import hou
import os #acces to operating system

# you need an argument for a path and a material since i defined a path
def apply_textures(path, material):
    files = os.listdir(path) #this will go to where we specified the path below and list every object/file in there
    for image in files:
        print(image)



material = hou.selectedNodes()[0] #you need a list, so even if just one object is selected you get a list and select the first item in the list with [0]
path = ('D:/Git/tutorial_materials/textures') # insert in () the pathway to a material file on your pc, IMPORTANT here: make sure the slashes / are this way round
apply_textures(path, material) # need this line to call the function, everything previous is just the blueprint but you stil need to call the function


stage 2, if you have differnt file formats for the same textur map like jpg and png and you want to limit to only one >

#automatically apply textures to a material based off of a folder

import hou
import os #acces to operating system

# you need an argument for a path and a material since i defined a path
def apply_textures(path, material):
    files = os.listdir(path) #this will go to where we specified the path below and list every object/file in there
    for image in files:
        if 'diff_1k.jpg' in image:
            material.parm('basecolor_useTexture').set(True)
            material.parm('basecolor_texture').set(path + '/' + image)
        if '_ao_1k.jpg' in image:
            material.parm('occlusion_useTexture').set(True)
            material.parm('occlusion_texture').set(path + '/' + image)
        if 'rough_1k.exr' in image:
            material.parm('rough_useTexture').set(True)
            material.parm('rough_texture').set(path + '/' + image)
        #add more for metal, glossiness, reflection, etc.
        if 'nor_gl_1k.exr' in image:
            material.parm('baseBumpAndNormal_enable').set(True)
            material.parm('baseNormal_texture').set(path + '/' + image)
            material.parm('baseNormal_scale').set(-.01)
        if 'disp_1k.png' in image:
            material.parm('dispTex_enable').set(True)
            material.parm('dispTex_texture').set(path + '/' + image)
            material.parm('dispTex_scale').set(.05)



material = hou.selectedNodes()[0] #you need a list, so even if just one object is selected you get a list and select the first item in the list with [0]
path = ('D:/Git/tutorial_materials/textures') # insert in () the pathway to a material file on your pc, IMPORTANT here: make sure the slashes / are this way round
apply_textures(path, material) # need this line to call the function, everything previous is just the blueprint but you still need to call the function

#end stage 2







Classes and Windows:

- example code with explanations >

#defining a class
class FXArtist: #naming convention > name is capitalised; anything afterwards thats indented is part of  class
    # the initialising method, everytime the class is called this method runs
    def __init__(self, name, position, location): #self there is a convention, it doesnt have to be self
    #anytime you are referencing the particular instance of a class you are gong to call self
        #instance variables
        self.name = name
        self.position = position
        self.location = location 
    #method
    def nameAndPosition(self):
        print(self.name + ' is a ' + self.position + ' at ' + self.location + '.')
      
        
#when we create an instance of a class it's called an object
#objects
marisa = FXArtist('Marisa', 'graphic designer', 'Aura')

#calling methods
marisa.nameAndPosition()