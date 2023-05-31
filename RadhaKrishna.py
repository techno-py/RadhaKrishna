import turtle

#keeping the background color dark blue
turtle.bgcolor('#ffc233')

#Defining title of program
turtle.title("Radhe Krishna")

#Creating turtle screen
screen= turtle.Screen()
#Defining height and width of screen
screen.setup(650,580)

radhaKrishna = turtle.Turtle()

#keeping the fasted speed for now, you can keep the speed as needed
#'fastest' : 0
#'fast' : 10
#'normal' : 6
#'slow' : 3
#'slowest' : 1

radhaKrishna.speed(4)

#Let's move down and go the position from where we will start to draw
radhaKrishna.right(90)
radhaKrishna.pu()
radhaKrishna.forward(180)
radhaKrishna.left(90)
#Now, the turtle is pointing positive x-axis

#Let's keep the pen down and start to draw the base
radhaKrishna.pd()
#Here we have dipped our turtle brush in a shade of blue color
radhaKrishna.fillcolor("#ff99d1")
radhaKrishna.begin_fill()
radhaKrishna.forward(400)
radhaKrishna.right(90)
radhaKrishna.forward(100)
radhaKrishna.right(90)
radhaKrishna.forward(800)
radhaKrishna.right(90)
radhaKrishna.forward(100)
radhaKrishna.right(90)
radhaKrishna.forward(400)
radhaKrishna.end_fill()
#Now, we have drawn the base which is rectangular in shape
#end_fill will fill blue color (selected above), in the shape formed by turtle

#Now, we will start to draw moon,I have selected a very light shade of blue to color moon
radhaKrishna.fillcolor("#CDEEF1")
radhaKrishna.begin_fill()
radhaKrishna.forward(160)
radhaKrishna.left(40)
#this method will draw the moon's border  
radhaKrishna.circle(250,280)
radhaKrishna.left(40)
radhaKrishna.forward(160)
radhaKrishna.end_fill()
#Now, we have drawn the moon as well as filled color in it

#Now, we will start drawing Radha Krishna
#We will draw Radha on our right side and Krishna on left side
#We will start with Radha
radhaKrishna.fillcolor("#012427")
radhaKrishna.begin_fill()
#We will start with the duppata
radhaKrishna.forward(160)
radhaKrishna.left(130)
radhaKrishna.circle(-300,30)
radhaKrishna.forward(95)
#This will draw the shoulder
radhaKrishna.circle(50,40)
radhaKrishna.right(40)
#This will draw the head
radhaKrishna.forward(43)
radhaKrishna.circle(80,25)
radhaKrishna.circle(50,30)
radhaKrishna.left(10)
radhaKrishna.circle(35,28)
#Now, we have completed drawing Radha

#Now, let's draw krishna's turban
radhaKrishna.right(160)
radhaKrishna.circle(10,100)
radhaKrishna.right(100)
radhaKrishna.circle(10,80)
radhaKrishna.forward(20)
radhaKrishna.left(80)
radhaKrishna.circle(100,15)
radhaKrishna.right(90)
radhaKrishna.forward(6)
radhaKrishna.left(65)
radhaKrishna.circle(60,55)

#Following code will draw Krishna's morpankh
radhaKrishna.right(160)
radhaKrishna.circle(20,100)
radhaKrishna.forward(10)
radhaKrishna.circle(-20,25)
radhaKrishna.left(170)
radhaKrishna.circle(-20,40)
radhaKrishna.forward(10)
radhaKrishna.circle(20,80)
#morpankh done

#We will continue to draw rest part of turban
radhaKrishna.right(135)
radhaKrishna.circle(60,15)
radhaKrishna.left(70)
radhaKrishna.forward(6)

radhaKrishna.right(110)
radhaKrishna.forward(9)

radhaKrishna.left(80)
radhaKrishna.circle(70,24)

radhaKrishna.right(60)
radhaKrishna.circle(65,30)
radhaKrishna.circle(-5,110)

#Below lines of code will draw the right hand of Krishna
radhaKrishna.circle(5,120)
radhaKrishna.right(90)
radhaKrishna.circle(5,60)
radhaKrishna.forward(10)
radhaKrishna.circle(10,5)
radhaKrishna.right(80)
radhaKrishna.forward(15)
radhaKrishna.circle(-5,160)
#Now, we will draw the first open finger of right hand
radhaKrishna.forward(6)
radhaKrishna.circle(2,180)
radhaKrishna.forward(6)
radhaKrishna.circle(20,30)

#Below lines will draw fingers holding bansuri
radhaKrishna.right(140)
radhaKrishna.circle(3,150)
radhaKrishna.right(110)
radhaKrishna.circle(4,80)
radhaKrishna.forward(2)
radhaKrishna.right(100)

#Here, we will draw second open finger of krishna
radhaKrishna.forward(6)
radhaKrishna.right(60)
radhaKrishna.forward(9)
radhaKrishna.circle(2,180)
radhaKrishna.forward(10)
radhaKrishna.left(30)
radhaKrishna.forward(15)

#We will now start to draw bansuri
radhaKrishna.right(85)
radhaKrishna.forward(40)
radhaKrishna.right(60)
radhaKrishna.circle(5,310)
radhaKrishna.right(80)
radhaKrishna.forward(3)
radhaKrishna.right(90)

#dor on bansuri
radhaKrishna.forward(42)
radhaKrishna.right(30)
radhaKrishna.forward(10)
radhaKrishna.left(90)
radhaKrishna.circle(20,60)
radhaKrishna.left(95)
radhaKrishna.forward(12)
radhaKrishna.right(29)
radhaKrishna.forward(42)

#We will draw the rest part of bansuri
radhaKrishna.right(90)
radhaKrishna.forward(34)
radhaKrishna.right(85)

#left hand of Krishna
radhaKrishna.forward(2)
radhaKrishna.circle(60,25)

#Now, we will draw Krishna's duppata
radhaKrishna.right(80)
radhaKrishna.circle(10,40)
radhaKrishna.forward(45)
radhaKrishna.left(10)
radhaKrishna.forward(130)

#Below lines will draw the plates of duppata
radhaKrishna.left(90)
radhaKrishna.forward(20)
radhaKrishna.right(90)
radhaKrishna.forward(10)
radhaKrishna.left(90)
radhaKrishna.forward(10)
radhaKrishna.right(90)
radhaKrishna.forward(5)
radhaKrishna.left(90)
radhaKrishna.forward(25)

#This will complete drawing duppata
radhaKrishna.left(100)
radhaKrishna.forward(120)

radhaKrishna.right(175)
radhaKrishna.circle(50,50)

#Now, we will tilt turtle towards required direction and draw Krishna's dhoti
radhaKrishna.right(80)
radhaKrishna.circle(110,15)
radhaKrishna.forward(75)

#The turtle will now reach to the rectangular base we had drawn in the beginning
radhaKrishna.left(97)
radhaKrishna.forward(260)
radhaKrishna.end_fill()
#At this point, we have completed drawing Radhe Krishna

radhaKrishna.pu()
radhaKrishna.right(90)
radhaKrishna.forward(100)
radhaKrishna.right(90)
radhaKrishna.forward(420)

#Lets also write their holy name in our drawing 
radhaKrishna.color("#00a606")
radhaKrishna.write("Radhe Krishna....", font=("Script",45, "bold"))

radhaKrishna.hideturtle()

turtle.done()