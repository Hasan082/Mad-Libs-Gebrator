from tkinter import Tk, Label, Button


root = Tk()
root.geometry("300x300")
root.title("Mad Libs")
Label(root, text="Mad Libs", font="arial 20 bold").pack()
Label(root, text="Click any one", font="arial 15 bold").place(x=40, y=80)


def mediLab1():
    animals = input("Enter a animal: ")
    profession = input("Enter a profession: ")
    cloth = input("Enter a piece of cloth: ")
    things = input("Enter a thing: ")
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    verb = input("Enter a verb: ")
    food = input("Enter a food: ")
    print('say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place +' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')


def madlib2():
    adjactive = input('enter adjective : ')
    color = input('enter a color name : ')
    thing = input('enter a thing name :')
    place = input('enter a place name : ')
    person = input('enter a person name : ')
    adjactive1 = input('enter a adjactive : ')
    insect = input('enter a insect name : ')
    food = input('enter a food name : ')
    verb = input('enter a verb name : ')
    print('Last night I dreamed I was a ' + adjactive + ' butterfly with ' + color + ' splocthes that looked like ' + thing + ' .I flew to ' + place + ' with my bestfriend and ' + person + ' who was a ' + adjactive1 + ' ' + insect + ' .We ate some ' + food + ' when we got there and then decided to ' + verb + ' and the dream ended when I said-- lets ' + verb + '.')


def madlib3():
    person = input('enter person name: ')
    color = input('enter color : ')
    foods = input('enter food name : ')
    adjective = input('enter aa adjective name: ')
    thing = input('enter a thing name : ')
    place = input('enter place : ')
    verb = input('enter verb : ')
    adverb = input('enter adverb : ')
    food = input('enter food name: ')
    things = input('enter a thing name : ')

    print('Today we picked apple from ' + person + "'s Orchard. I had no idea there were so many different varieties of apples. I ate " + color + ' apples straight off the tree that tested like ' + foods + '. Then there was a ' + adjective + ' apple that looked like a ' + thing + '.When our bag were full, we went on a free hay ride to ' + place + ' and back. It ended at a hay pile where we got to ' + verb + ' ' + adverb + '. I can hardly wait to get home and cook with the apples. We are going to make appple ' + food + ' and ' + things + ' pies!.')


Button(root, text="The Photographer", font="arial 15", command=mediLab1, bg="ghost white").place(x=60, y=120)
Button(root, text="apple and orange", font="arial 15", command=madlib3, bg="ghost white").place(x=60, y=180)
Button(root, text="The Butterfly", font="araial 15", command=madlib2, bg="ghost white").place(x=60, y=240)


root.mainloop()
