import random
import matplotlib.pyplot as plotter # for piechart

def nums():
    print("Statistical analysis of Python's random number generator")
    print("We'll be running random numbers for a defined amount of times.")
    print("This is to see how often numbers from 1 to 5 are picked at random.")
    x = 0
    one = [] # creating empty lists
    two = []
    three = []
    four = []
    five = []
    q = int(input("How many cycles?: "))
    while q > 0:
        x = random.randint(1,5) # if you change this for more numbers you'll need to create new lists
        if x == 1:
            one.append(x) # apending each instance of the random number to a list
        if x == 2:
            two.append(x)
        if x == 3:
            three.append(x)
        if x == 4:
            four.append(x)
        if x == 5:
            five.append(x)
        q = q-1 # running through cycles
            
            
    one = len(one) # how long each list is will show how many times the numbers were drawn
    two = len(two)
    three = len(three)
    four = len(four)
    five = len(five)
    
    print("\n")
    print(f"One appeared {one} times") # print with f string literals
    print(f"Two appeared {two} times")
    print(f"Three appeared {three} times")
    print(f"Four appeared {four} times")
    print(f"Five appeared {five} times")
    print("\n")
    
    pieLabels = "% One","% Two","% Three","% Four","% Five" # creating the pie chart in %
    populationShare = [one, two, three, four, five]
    figureObject, axesObject = plotter.subplots()
    axesObject.pie(populationShare, labels=pieLabels, autopct='%1.2f',startangle=90)
    axesObject.axis('equal')
    plotter.show()
    
