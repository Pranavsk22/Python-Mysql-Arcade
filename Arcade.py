import sys
sys.path.append('D://RPS project')
import tkinter as tk
from tkinter import *
import mysql.connector
login=True
def submitact():
        global user
        user = Username.get()
        passw = password.get()
        l=[user,passw]
        import csv
        f=open(r'C:\Users\Adarsh\Desktop\user_data.txt.txt','r')
        w=csv.reader(f)
        
        for i in w:
                if i[0]==user:
                        if i[1]==passw:
                                box.showinfo('info','Correct Login')
                                continue
                        else:
                                box.showwarning('info','Inorrect Login')
                                login=False
                


        print(f"The name entered by you is {user} {passw}")

        logintodb(user, passw)


def logintodb(user, passw):
        user=Username.get()
        passw=password.get()
        import csv
        f=open(r'C:\Users\Adarsh\Desktop\user_data.txt.txt','a')
        w=csv.writer(f)
        l=[user,passw]
        w.writerow(l)
        f.close()
        user = Username.get()
        passw = password.get()
        mycon = mysql.connector.connect(host ="localhost", user = "root", password = "varunchandar", database ="arcade")
        cursor = mycon.cursor()
        q="insert into userinfo(user,passw)values('{}','{}')".format(user,passw)
        cursor.execute(q)
        mycon.commit()
        mycon.close()

root = tk.Tk()
root.geometry("300x300")
root.title("Arcade Login Page")


# Defining the first row
lblfrstrow = tk.Label(root, text ="Username -", )
lblfrstrow.place(x = 50, y = 20)

Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)

lblsecrow = tk.Label(root, text ="Password -")
lblsecrow.place(x = 50, y = 50)

password = tk.Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)

submitbtn = tk.Button(root, text ="Login",
                                        bg ='white', command = submitact)
submitbtn.place(x = 150, y = 135, width = 55)

root.mainloop()

from tkinter import *
from tkinter import ttk
root1=Tk()
root1.title('ARCADE!')
root1.geometry('500x600')
root1.config(bg='white')

def go():
    global ch
    if first_choice.get()=="RPS":
        ch=1
    elif first_choice.get()=="Snake-Game":
        ch=3
    elif first_choice.get()=="Racing Game":
        ch=4
    return ch

first_choice=ttk.Combobox(root1,value=("RPS","Snake-Game","Racing Game"))
#first_choice.current(0)
first_choice.pack(pady=20)
arcadepic=PhotoImage(file='D:\\RPS project\\arcadepic.gif')
image_label=Label(root1,image=arcadepic,bd=0)
image_label.pack(pady=20)
ch=None
gobutton= Button(root1,text='GO!',command=go)
gobutton.pack(pady=10)
ch=go()
root1.mainloop()

#ch=int(input("What would you like to play ?\n(1):Rock Paper Scissors\n(2):Tic Tac Toe\n"))
if ch==1:
    
    from tkinter import *
    from random import randint
    from tkinter import ttk
    root=Tk()
    root.title('Rock Paper Scissors')
    root.geometry("500x600")
    #changing background colour to white
    root.config(bg="white")

    #define our images
    Rock=PhotoImage(file='D:\\RPS project\\rockgif.gif')

    Paper=PhotoImage(file='D:\\RPS project\\papergif.gif')

    Scissors=PhotoImage(file='D:\\RPS project\\scissornewgif.gif')



    #add Images to a List
    imagelist=[Rock,Paper,Scissors]

    

    #Pick random number between 0 and 2(for rps)
    picknumber=randint(0,2)


    #throw up an image when program starts
    image_label=Label(root,image=imagelist[picknumber],bd=0)
    image_label.pack(pady=20)


    #spin function
    def spin():
        #picking random number
        picknumber=randint(0,2)
        #show image
        image_label.config(image=imagelist[picknumber])
        

        #0=Rock
        #1=Paper
        #2=Scissors

        #convert dropdown choice to number
        if userchoice.get()=="Rock":
            userchoicevalue=0
        elif userchoice.get()=="Paper":
            userchoicevalue=1
        elif userchoice.get()=="Scissors":
            userchoicevalue=2

        #determine if we won or not
        if userchoicevalue==0: #rock
            
            if picknumber==0: #rock
                resultlabel.config(text="It's a tie! Spin Again....")
                


            elif picknumber==1: #paper
                resultlabel.config(text="Paper Crumples Rock! YOU LOSE!")
                


            elif picknumber==2: #Scissors
                resultlabel.config(text="Rock Crushes Scissors! YOU WIN!")

                root.mainloop()
                
                import tkinter
                trial=tkinter.Tk()
                trial.title('MEME')
                trial.geometry("600x600")
                trial.config(bg='white')

                #meme images
                meme1=PhotoImage(file='D:\\RPS project\\meme1new.gif')
                
                meme2=PhotoImage(file='D:\\RPS project\\meme2new.gif')

                meme3=PhotoImage(file='D:\\RPS project\\meme3new.gif')

                meme4=PhotoImage(file='D:\\RPS project\\meme4new.gif')

                meme5=PhotoImage(file='D:\\RPS project\\meme5new.gif')

                #meme6=PhotoImage(file='H:\\RPS project\\meme6new.gif')

                meme7=PhotoImage(file='D:\\RPS project\\meme7new.gif')

                meme8=PhotoImage(file='D:\\RPS project\\meme8new.gif')

                meme9=PhotoImage(file='D:\\RPS project\\meme9new.gif')

                meme10=PhotoImage(file='D:\\RPS project\\meme10new.gif')

                meme11=PhotoImage(file='D:\\RPS project\\meme11new.gif')

                meme12=PhotoImage(file='D:\\RPS project\\meme12new.gif')

                meme13=PhotoImage(file='D:\\RPS project\\meme13new.gif')

                #meme14=PhotoImage(file='H:\\RPS project\\meme14new.gif')

                meme15=PhotoImage(file='D:\\RPS project\\meme15new.gif')



                #imagelist for memes
                imagelist2=[meme1,meme2,meme3,meme4,meme5,meme7
                            ,meme8,meme9,meme10,meme11,meme12,meme13,meme15]

                #random number
                picknumber2=randint(0,12)

                imglabel2=Label(trial,image=imagelist2[picknumber2],bd=0)
                imglabel2.pack(pady=20)

                trial.mainloop()
                



                
        if userchoicevalue==1: #paper
            
            if picknumber==1: #paper
                resultlabel.config(text="It's a tie! Spin Again....")
                


            elif picknumber==0: #rock
                resultlabel.config(text="Paper Crumples Rock! YOU WIN!")

                root.mainloop()
                
                import tkinter
                trial=tkinter.Tk()
                trial.title('MEME')
                trial.geometry("500x500")
                trial.config(bg='white')

                #meme images
                meme1=PhotoImage(file='D:\\RPS project\\meme1new.gif')
                
                meme2=PhotoImage(file='D:\\RPS project\\meme2new.gif')

                meme3=PhotoImage(file='D:\\RPS project\\meme3new.gif')

                meme4=PhotoImage(file='D:\\RPS project\\meme4new.gif')

                meme5=PhotoImage(file='D:\\RPS project\\meme5new.gif')

                #meme6=PhotoImage(file='H:\\RPS project\\meme6new.gif')

                meme7=PhotoImage(file='D:\\RPS project\\meme7new.gif')

                meme8=PhotoImage(file='D:\\RPS project\\meme8new.gif')

                meme9=PhotoImage(file='D:\\RPS project\\meme9new.gif')

                meme10=PhotoImage(file='D:\\RPS project\\meme10new.gif')
                meme11=PhotoImage(file='D:\\RPS project\\meme11new.gif')

                meme12=PhotoImage(file='D:\\RPS project\\meme12new.gif')

                meme13=PhotoImage(file='D:\\RPS project\\meme13new.gif')

                #meme14=PhotoImage(file='H:\\RPS project\\meme14new.gif')

                meme15=PhotoImage(file='D:\\RPS project\\meme15new.gif')



                #imagelist for memes
                imagelist2=[meme1,meme2,meme3,meme4,meme5,meme7
                            ,meme8,meme9,meme10,meme11,meme12,meme13,meme15]

                #random number
                picknumber2=randint(0,12)

                imglabel2=Label(trial,image=imagelist2[picknumber2],bd=0)
                imglabel2.pack(pady=20)

                trial.mainloop()



                
            elif picknumber==2: #Scissors
                resultlabel.config(text="Scissor Cuts Paper! YOU LOSE!")
                
                


        if userchoicevalue==2: #Scissors
            
            if picknumber==2: #Scissors
                resultlabel.config(text="It's a tie! Spin Again....")
                
                
            elif picknumber==0: #Rock
                resultlabel.config(text="Rock Crushes Scissors! YOU LOSE!")
                

            elif picknumber==1: #Paper
                resultlabel.config(text="Scissor Cuts Paper! YOU WIN!")

                root.mainloop()
                
                import tkinter
                trial=tkinter.Tk()
                trial.title('MEME')
                trial.geometry("500x500")
                trial.config(bg='white')

                #meme images
                meme1=PhotoImage(file='D:\\RPS project\\meme1new.gif')
                
                meme2=PhotoImage(file='D:\\RPS project\\meme2new.gif')

                meme3=PhotoImage(file='D:\\RPS project\\meme3new.gif')

                meme4=PhotoImage(file='D:\\RPS project\\meme4new.gif')

                meme5=PhotoImage(file='D:\\RPS project\\meme5new.gif')

                #meme6=PhotoImage(file='H:\\RPS project\\meme6new.gif')

                meme7=PhotoImage(file='D:\\RPS project\\meme7new.gif')

                meme8=PhotoImage(file='D:\\RPS project\\meme8new.gif')

                meme9=PhotoImage(file='D:\\RPS project\\meme9new.gif')

                meme10=PhotoImage(file='D:\\RPS project\\meme10new.gif')

                meme11=PhotoImage(file='D:\\RPS project\\meme11new.gif')

                meme12=PhotoImage(file='D:\\RPS project\\meme12new.gif')

                meme13=PhotoImage(file='D:\\RPS project\\meme13new.gif')

                #meme14=PhotoImage(file='H:\\RPS project\\meme14new.gif')

                meme15=PhotoImage(file='D:\\RPS project\\meme15new.gif')



                #imagelist for memes
                imagelist2=[meme1,meme2,meme3,meme4,meme5,meme7
                            ,meme8,meme9,meme10,meme11,meme12,meme13,meme15]

                #random number
                picknumber2=randint(0,12)

                imglabel2=Label(trial,image=imagelist2[picknumber2],bd=0)
                imglabel2.pack(pady=20)

                trial.mainloop()


                




    #make our choice
    userchoice=ttk.Combobox(root,value=("Rock","Paper","Scissors"))
    userchoice.current(0)
    userchoice.pack(pady=20)

    #spin button
    spinbutton= Button(root,text='Spin!',command=spin)
    spinbutton.pack(pady=10)

    
    #label for showing result

    resultlabel=Label(root,text='',font=("Helvetica",20))
    resultlabel.pack(pady=50)




    root.mainloop()

elif ch==3:
    import turtle
    import time
    import random

    delay = 0.1

    # Score
    score = 0
    high_score = 0

    # Set up the screen
    wn = turtle.Screen()
    wn.title("Snake Game")
    wn.bgcolor("green")
    wn.setup(width=600, height=600)
    wn.tracer(0) # Turns off the screen updates

    # Snake head
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("black")
    head.penup()
    head.goto(0,0)
    head.direction = "stop"

    # Snake food
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0,100)

    segments = []

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

    # Functions
    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":
            head.direction = "down"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def go_right():
        if head.direction != "left":
            head.direction = "right"

    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)

        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)

        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)

        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)
    def quit():
        global running
        running=False

    # Keyboard bindings
    wn.listen()
    wn.onkeypress(go_up, 'Up')
    wn.onkeypress(go_down, 'Down')
    wn.onkeypress(go_left, 'Left')
    wn.onkeypress(go_right, 'Right')
    wn.onkeypress(quit,'q')

    running=True

    # Main game loop
    while running:
        wn.update()

        # Check for a collision with the border
        if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


        # Check for a collision with the food
        if head.distance(food) < 20:
            # Move the food to a random spot
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x,y)

            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)

            # Shorten the delay
            delay -= 0.001

            # Increase the score
            score += 10

            if score > high_score:
                high_score = score
            
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

        # Move the end segments first in reverse order
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)

        move()    

        # Check for head collision with the body segments
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"
            
                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)
            
                # Clear the segments list
                segments.clear()

                # Reset the score
                score = 0

                # Reset the delay
                delay = 0.1
            
                # Update the score display
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        time.sleep(delay)
    

    wn.mainloop()
    
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='varunchandar',database='arcade')
    cursor=mycon.cursor()
    q="insert into snake(user,high_score) values('{}',{})".format(user,high_score)

    cursor.execute(q)
    r="Select * from snake where username='{}'".format(user)
    print('Hello ',user,'!','\n These are your scores : ')
    data=cursor.fetchall()
    for i in data:
        print(i)
    w="select * from snake order by high_score desc"
    cursor.execute(w)
    print('Here is where you stand in the leaderboard : ')
    data1=cursor.fetchall()
    for j in data1:
        print(j)
    mycon.commit()
    mycon.close()

        

elif ch==4:
    import sys
    sys.path.append('D://RPS project')
    import Racing_Game
    
else:
from tkinter import messagebox
messagebox.showwarning("ERROR","It is against the creed to make an incorrect choice! Choose with HONOUR!\nThis is the Way...")

'''
    
        if winner==True:
            import tkinter
            from random import randint
            trial=tkinter.Tk()
            trial.title('MEME')
            trial.geometry("500x500")
            trial.config(bg='white')

            #meme images
            meme1=PhotoImage(file='H:\\Academic\\RPS project\\meme1new.gif')
            
            meme2=PhotoImage(file='H:\\Academic\\RPS project\\meme2new.gif')

            meme3=PhotoImage(file='H:\\Academic\\RPS project\\meme3new.gif')

            meme4=PhotoImage(file='H:\\Academic\\RPS project\\meme4new.gif')

            meme5=PhotoImage(file='H:\\Academic\\RPS project\\meme5new.gif')

            meme6=PhotoImage(file='H:\\Academic\\RPS project\\meme6new.gif')

            meme7=PhotoImage(file='H:\\Academic\\RPS project\\meme7new.gif')

            meme8=PhotoImage(file='H:\\Academic\\RPS project\\meme8new.gif')

            meme9=PhotoImage(file='H:\\Academic\\RPS project\\meme9new.gif')

            meme10=PhotoImage(file='H:\\Academic\\RPS project\\meme10new.gif')

            meme11=PhotoImage(file='H:\\Academic\\RPS project\\meme11new.gif')

            meme12=PhotoImage(file='H:\\Academic\\RPS project\\meme12new.gif')

            meme13=PhotoImage(file='H:\\Academic\\RPS project\\meme13new.gif')

            meme14=PhotoImage(file='H:\\Academic\\RPS project\\meme14new.gif')

            meme15=PhotoImage(file='H:\\Academic\\RPS project\\meme15new.gif')



            #imagelist for memes
            imagelist2=[meme1,meme2,meme3,meme4,meme5,meme6,meme7
                        ,meme8,meme9,meme10,meme11,meme12,meme13,meme14,meme15]

            #random number
            picknumber2=randint(0,14)

            imglabel2=Label(trial,image=imagelist2[picknumber2],bd=0)
            imglabel2.pack(pady=20)

            trial.mainloop()

'''

