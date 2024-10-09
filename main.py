''' so this is our sneak game you think it's easy noo think again my friend
1- you have timer from 10 to 0 the timer get faster after a period of time you will die at the end , i made sure to make you die LOL but you should collect the best score you can
2- if you eat the food faster will get better score reward than eating it late
3- if you didn't eat the food on the time , it will disappear and change the place and you will lose part of your body and your calculated score function will have a negative effect
4-if the sneak disappear you will lose , if you hit the borders you will lose , if you hit your body parts you will lose
5- timer and speed of the sneak increase over time, it will not be easy
6- control your sneak using Arrows or 'WASD', you can press contiunelly on the same button on the direction of the sneak to make it run faster temprorally or press any button except 'q'
7- you can press 'q' to quit
'''



import curses,time,random #the modules that we need or maybe that I used to make this
from curses.textpad import rectangle
from math import sqrt    # i use it to calculate the score i love math so i like to make a little complex score  function


# this should not be the beginning but shortly this is the function that make random food on the screen
def makefood():
    while(True):
        xfood= random.randrange(1,X-2)
        yfood= random.randrange(1,Y-2)
        food=[yfood,xfood]
        if food!=head:   # we check that the food didn't take a place where the sneak is located , if this condition correct we will return the coordination of the food if not the function will produce another random coordination and check them again till we have a valid coordination
            return food


# a function represent the counter in the game
def score_and_counter(j,score,eat1,eat2):
    if eat2>eat1:       # it will calculate score after eating food
        scoree= sqrt(len(sneak)*Nfood)+score +eat2*(Bonus +1)   #just a function i created to calculate the score
        scoree= round(scoree/3,3)       # make the score easier to read with only tree degit after the coma
        eat1=eat2
    else:
        scoree=0   #noo food eaten so the new additional score will be 0 and we will show on the screen the previous score

    screen.addstr(2,X//2,str(j), curses.A_BLINK)  #show the timer you should be quick!!!!
    if score<=scoree:                          # cheek if the new calculated score is bigger than the current score
        screen.addstr(2, 90, str(scoree))
        return j-1,scoree,eat1
    else:
        screen.addstr(2, 90, str(score))
        return j-1,score,eat1


# this function make the game harder
def level_UP(time_harder):
    global delay
    global speed
    global Bonus
    global checking
    Bonus+= speed // 100 + delay // 2   #harder mean more Bonus
    delay-=0.05*delay                   #changing delay will make the timer faster, the food will disappear faster
    speed-= 0.05*speed                   # the sneak will be faster
    return time_harder+0.1*time_harder             # the again variable just to make change on when this function will be called again


''' HERE WE GO 
                  
                  THE START OF OUR CODE
    '''




#make the main screen,
#ther is another way is to use wrapper function but I prefer this way
screen =curses.initscr()
'''take values of our main screen size
max_y for the Hight
max_x for the Length
'''
#activating colors and intialize them
curses.start_color()
curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_BLACK)
Red=curses.color_pair(1)
Yellow=curses.color_pair(2)
Green = curses.color_pair(3)
#get dimensions of the main screen
max_y , max_x = screen.getmaxyx()
#hide the curser
curses.curs_set(0)

#make our playable window inside our main screen
Y = max_y - 6
X= max_x-20
playsceen= curses.newwin(Y,X,4,8)
playsceen.border()  #make visible borders


#make our character:  the sneak
head = [Y//2,X//2]
body = [Y//2 +1, X//2]
tail = [Y//2 +2,X//2]
sneak=[head,body,tail]


#actevating complex keys input
playsceen.keypad(1)
screen.keypad(1)


#make the no_Direc that's mean we can't move down at the beginning of the game
no_Direc= (curses.KEY_DOWN,ord('s'))



playsceen.addstr(1,1,f"\t Welcome to sneak game \n 1- you have timer from 10 to 0 the timer get faster after a period of time you will die at the end , i made sure to make you die LOL but you should collect the best score you can\n2- if you eat the food faster will get better score reward than eating it late\n3- if you didn't eat the food on the time , it will disappear and change the place and you will lose part of your body and your calculated score function will have a negative effect\n4-if the sneak disappear you will lose , if you hit the borders you will lose , if you hit your body parts you will lose\n5- timer and speed of the sneak increase over time, it will not be easy\n6- control your sneak using Arrows or 'WASD', you can press contiunelly on the same button on the direction of the sneak to make it run faster temprorally or press any button except 'q'\n7- you can press 'q' to quit\n\t\t Enjoy , press any key to continue")
playsceen.getch()
#our start for the game
playsceen.addstr(Y-5,X//2,"Get Ready",Yellow)
playsceen.refresh()
time.sleep(2)
playsceen.clear()
for sni in sneak:
    playsceen.addch(sni[0],sni[1],curses.ACS_BOARD,Red)
    playsceen.refresh()
    time.sleep(0.5)


# some set up for the food creation
food= makefood()


''' so we have two loops:
1- is the general loop of the game in general, it control the game after losing or after pressing q to quit,
      that's mean after losing we will have small menu and we can choose if we want to play again or not and we can see our score and our best score
2- we have the game loop, the most important and all the game things go inside this second loop (control and sneak places, food places .... 
    everything consider the game  and speed of the sneak, all inside this loop , and we can get out of it using 'q' to quit or simply after losing '''

Continue= True    # this variable declare if we are going to play again or not after losing
best_score=0     # this variable save the best store the player can get
while(Continue):    # our general loop


    ''' those are some variables that i will use in several steps in my code to make thing easier i will explain them '''
    t=0   #in purpose to colorize the sneak at the end of the code
    j=10                # that's the counter start
    time_start=time_start2=time.time()     # that's will help me on making the counter
    delay=2  #delay of our counter we can change it to make game harder
    score=0   # the first score
    Nfood= 0    # a factor that i will need when i will calculate score
    eat1=0      # another factor help me now if the player eat the food or not yet
    eat2=0      # same as the pervious factor
    speed=200   # the speed of the sneak
    Bonus= 0     # so this is Bonus when the game get harder you will get some Bonus to your global score
    knife=sneak[-1]    # knife this variable will get every body get out of the sneak and when it will get the head the sneak will die and you will lose !! don't let my knife get your sneak!!
    time_harder = 7# this variable decide how much time need to make the game harder
    '''  at was the end of the variables that i will use to make some calculation or make timer or other things'''

    #make the game control and the game loop
#here all the actions

    while True:

        # our control with Arrow or with 'WASD', 'q' for quiting the game
        inputss = (curses.KEY_LEFT,curses.KEY_RIGHT,curses.KEY_UP,curses.KEY_DOWN,ord('q'),ord('w'),ord('s'),ord('a'),ord('d'))

        #waiting 0.1 second for the input if not code will continue
        playsceen.timeout(int(speed))
        k = playsceen.getch()        # get input
        playsceen.clear()
        screen.clear()#clear the screen


        #this is the part that we make our counter wait one second before change
        time_current=time.time()
        if time_current-time_start>=delay:
            j,score,eat1=score_and_counter(j,score,eat1,eat2)
            time_start=time_current
        else:
            score_and_counter(j,score,eat1,eat2)

        #edeting sneak after eating or after the timer reach 0
        if food==head or j==0 :
            if food==head and j!=0:
                extra = [0, 0]
                extra = tail.copy()   # the addition body if the sneak eats
                sneak.append(extra)   #add it to the sneak
                Nfood=Nfood+j        # the reward will be calculated when changing the score the faster you get the food the bigger will be
                eat2+=1              # just to check that the sneak eat the food
            if j==0:
                knife=sneak.pop()     # if the time up and the sneak couldn't reach the food it will lose one part of her body
                Nfood=Nfood//2
            food = makefood()   # food coordinations
            # to restart the timer if the sneak eat the food
            j=10                 # repeating the timer
            time_start = time_current


        # so if the sneak hit herself it will be the end of the game or if all the sneak disappears
        if knife==head:
            break
        for i in range(len(sneak)-1):
            Lose=False
            if head == sneak[i+1]:
                Lose=True
                break
        if Lose:
            break


        playsceen.addch(food[0], food[1], curses.ACS_DIAMOND)   # show the food on the screen


        if k in no_Direc:         # to avoid moving when the user press the other side key
            time.sleep(0.1)

        if k not in no_Direc and k!=-1 and k in inputss:   # if the input was valide

            #this is small explanation
            ''' the following is how we are going to make the sneak move
             by cheeking the inputs and coping the elements of the sneak except the head. to explain more when the sneak eat a diamond or our food,
             it will have an additional tail on the same tail that she has, after that in the following code one tail will copy the coordinate of the other tail, 
             in other world one tail will stay stable but the other tail will copy the coordinate of the body part so it will move '''



            if k == curses.KEY_RIGHT or k==ord('d') :
                for e in range(len(sneak)-1,0,-1):   #that's mean our element 'e' will take values from the length of our list 'sneak' to the element that follow the head directly, and we move each time one element '-1' back
                    sneak[e]=sneak[e-1].copy()
                head[1]+=1
                no_Direc = (curses.KEY_LEFT,ord('a'))
            if k == curses.KEY_LEFT or k==ord('a') :
                for e in range(len(sneak) - 1, 0, -1):
                    sneak[e] = sneak[e - 1].copy()
                head[1]-=1
                no_Direc = (curses.KEY_RIGHT,ord('d'))
            if k == curses.KEY_UP or k==ord('w') :
                for e in range(len(sneak) - 1, 0, -1):
                    sneak[e] = sneak[e - 1].copy()
                head[0]-=1
                no_Direc = (curses.KEY_DOWN, ord('s'))
            if k == curses.KEY_DOWN or k==ord('s') :
                for e in range(len(sneak) - 1, 0, -1):
                    sneak[e] = sneak[e - 1].copy()
                head[0]+=1
                no_Direc = (curses.KEY_UP, ord('w'))
            # if player press q that's mean he want quit the game but maybe he pressed by mistake so the game will ask him to confirm by pressing q again or to continue playing
            if k==ord('q'):
                screen.clear()
                screen.addstr(Y // 2, X // 2 - 5, "are you sure you want to quit!!", curses.A_BOLD)
                screen.addstr(Y // 2 + 1, X//6, "you will lose your process , press 'q' to confirm or press any key to continue playing", Yellow)
                screen.refresh()
                k=None
                quit=screen.getch()
                if quit==ord('q'):
                    Continue=False   #if the player confirm that he wants to quit it will break the game loop and the general loop
                    break
                else:
                    continue



        else:        # if no input was giving that's mean k will take '-1' value
            if no_Direc[0] == curses.KEY_LEFT:
                for e in range(len(sneak) - 1, 0, -1):
                    sneak[e] = sneak[e - 1].copy()
                head[1] += 1
            if no_Direc[0] == curses.KEY_RIGHT:
                for e in range(len(sneak) - 1, 0, -1):
                    sneak[e] = sneak[e - 1].copy()
                head[1] -= 1
            if no_Direc[0] == curses.KEY_DOWN:
                for e in range(len(sneak) - 1, 0, -1):
                    sneak[e] = sneak[e - 1].copy()
                head[0] -= 1
            if no_Direc[0] == curses.KEY_UP:
                for e in range(len(sneak) - 1, 0, -1):
                    sneak[e] = sneak[e - 1].copy()
                head[0] += 1


        if head[0] >= Y - 1 or head[0] <= 0 or head[1] >= X - 1 or head[1] <= 0:  # so if the sneak head reach our windows border it will be an ending game
            break


        playsceen.border() # we need to show our window border each time because we clear



        #show our snake after the changes that we made on her place
        for sni in sneak:
            if sni == sneak[0]:  #show the head of our sneak with yellow
                playsceen.addch(sni[0], sni[1], curses.ACS_BOARD, Yellow)
            elif sni==sneak[-1]:  #show the tail with red
                playsceen.addch(sni[0], sni[1], curses.ACS_BOARD, Red)
            else:   # we will show the body some parts will be white and some with green
                if t==0:
                    playsceen.addch(sni[0], sni[1], curses.ACS_BOARD)
                    if len(sneak)%2!=0 and sni == sneak[-2]:
                        t=0
                    else: # you can delete this else part if you want your sneak all white
                        t=1
                else:
                    playsceen.addch(sni[0], sni[1], curses.ACS_BOARD,Green)
                    t=0

        # this part describe how will the game get harder with time 'time_harder'
        if(time_current-time_start2 >=time_harder):
            again = level_UP(time_harder)
            time_start2=time_current
        knife=sneak[-1]
        screen.addstr(0,0,time.ctime(time_current)) # just to show date and time nothing else
        screen.refresh() # OFF COURSE WE NEED TO REFRESH OUR WINDOW SO WE CAN SEE THE CHANGES BEFORE CLEAR THE SCREEN.


    #this is the finsh of the game so it will be a choice , the you want play again or maybe no
    if(Continue):   # if he want to quit 'q' , this finishing menu will not appear at all

        playsceen.clear()  # clear everything
        if score>best_score:  # check if the new score bigger than the best score
            best_score=score

            # show some messages on the screen if he reachs new high score
            playsceen.addstr(Y // 2, X // 2 - 2, f"Congratulation !!! New high Score: {best_score}", curses.A_BOLD)
            playsceen.addstr(Y // 2 + 1, X // 2 - 5, "want to play again? press 'x' to choose", Yellow)
        else:   # else we will show other messages
            playsceen.addstr(Y//2-1,X//2-2,f"You Lose and your score is: {score}",curses.A_BOLD)
            playsceen.addstr(Y//2,X//2-2,f"your best score is {best_score}",Green)
            playsceen.addstr(Y//2+1,X//2-5,"want to play again? press 'x' to choose",Yellow)
        choose=None    # thi variable will take the input from the player so we can now that he press the correct key 'x' to choose if he want to play or no
        choose_factore=0    # this variable to know if he chooses yes or no so yes :will be even numbers and no the odd numbers
        while(choose!= ord('x')):     # our loop and of yes or no choice
            if choose in (curses.KEY_RIGHT,curses.KEY_LEFT, ord('a'),ord('d'),None):
                choose_factore+=1
            if choose_factore%2==0:
                playsceen.attron(Green)
                rectangle(playsceen,Y//2+2 ,X//2-1,Y//2+4,X//2+3)
                playsceen.attroff(Green)
                playsceen.addstr(Y//2+3,X//2,"Yes",curses.A_BLINK)

                playsceen.attron(Red)
                rectangle(playsceen,Y//2+2 ,X//2+9,Y//2+4,X//2+12)
                playsceen.attroff(Red)
                playsceen.addstr(Y // 2 + 3, X // 2 + 10, "No")
            else:
                playsceen.attron(Green)
                rectangle(playsceen, Y // 2 + 2, X // 2 - 1, Y // 2 + 4, X // 2 + 3)
                playsceen.attroff(Green)
                playsceen.addstr(Y // 2 + 3, X // 2, "Yes")

                playsceen.attron(Red)
                rectangle(playsceen, Y // 2 + 2, X // 2 + 9, Y // 2 + 4, X // 2 + 12)
                playsceen.attroff(Red)
                playsceen.addstr(Y // 2 + 3, X // 2 + 10, "No",curses.A_BLINK)
            choose= playsceen.getch()


            playsceen.refresh()  # refresh to see the player input

        # we need to make new sneak ready if the player chooses to play agin
        head = [Y // 2, X // 2]
        body = [Y // 2 + 1, X // 2]
        tail = [Y // 2 + 2, X // 2]
        sneak = [head, body, tail]
        no_Direc = (curses.KEY_DOWN, ord('s'))

       # check our variable odd or even that's mean yes or no
        if choose_factore%2==0:
            Continue=True
        else:
            Continue=False
        playsceen.refresh()

''' Thank you for reading all this , i know it wasn't so organized, but i tried to make a good documentation and explain everything
                                thank you and enjoy '''