# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random
import math

global num_guess , num_secret , num_remain , num_range1 ,num_range2


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here  
    pass

# define event handlers for control panel

def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_guess , num_secret , num_remain , num_range1 ,num_range2
    num_secret = random.randint(0, 100) 
    num_range1 = 0 
    num_range2 = 100
    num_remain = 7
    print "可猜数字区间0到100\n"
    
    print num_remain,"次机会\n"
   
   
    return num_remain
  
    
    
    
  
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_guess , num_secret , num_remain , num_range1 ,num_range2
    num_secret = random.randint(0, 1000)
    num_range1 = 0 
    num_range2 = 1000
    num_remain = 10
    print "可猜数字区间0到100\n"
    
    print num_remain,"次机会\n"
    
    
    return num_remain
    
def input_guess(guess):
    # main game logic goes here	
    global num_guess , num_remain , num_range1 ,num_range2
    # if int(guess):
    #    print "Invalid literal"
    # else:
    num_guess = int(guess)
    print "您猜的数字是\n" , guess
    num_remain -=1 
    print num_remain,"次机会\n"
    if num_remain >= 0:
            if num_guess == num_secret:
                print "猜对了！\n"
            elif num_range1 < num_guess < num_secret:
                print "小了\n"
                num_range1 = num_guess
            elif num_secret < num_guess < num_range2:
                print "大了\n"
                num_range2 = num_guess
            else:     
                print "无效数字！\n"     
    else:
            print "游戏结束！\n"
    return num_remain
    return num_guess

def draw(canvas):
    global num_guess , num_secret , num_remain , num_range1 ,num_range2
#    canvas.draw_text('C', (80, 50), 12, 'Gray')
#    canvas.draw_text('A', (20, 20), 12, 'Red')
#    canvas.draw_text('B', [30, 50], 20, 'Blue')
#    canvas.draw_text('C', (80, 70), 12, 'Gray', 'serif')
    pass
    
# create frame
f = simplegui.create_frame("Guess the number",300,300)
f.set_canvas_background("White")

# register event handlers for control elements and start frame
f.add_button("猜数区间\n [0,100 )",range100, 200)
f.add_button("猜数区间\n [0,1000 )",range1000, 200)
f.add_input("猜一个数字\n",input_guess , 200)
f.set_draw_handler(draw)


# call new_game 
new_game()
f.start() 

# always remember to check your completed program against the grading rubric
