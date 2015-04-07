# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
# 遇到第一个问题，回放不是逐步的

import simplegui
import random
import math

global num_guess , num_secret , num_remain  ,num_range2 ,num_auto 
num_range1 = 0 
list = []
list_num = 0
review_list = []
step = 0
order = 0
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here  
    pass

# define event handlers for control panel

def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_guess , num_secret , num_remain , num_range1 ,num_range2 , list_num
    num_secret = random.randint(0, 100) 
    num_range2 = 100
    num_remain = 7
    #print '可猜数字区间0到100\n',num_remain,'次机会\n'
    list.append('可猜数字区间0到100\n'+str(num_remain)+'次机会\n')
    print list[list_num]  
    list_num += 1  
    review_list = list
    return num_remain

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_guess , num_secret , num_remain , num_range1 ,num_range2 , list_num
    num_secret = random.randint(0, 1000)
    num_range2 = 1000
    num_remain = 10
    #print "可猜数字区间0到100\n",num_remain,"次机会\n"
    list.append('可猜数字区间0到1000\n'+str(num_remain)+'次机会\n')
    print list[list_num]  
    list_num += 1 
    review_list = list
    return num_remain
    
def input_guess(guess):
    # main game logic goes here	
    global num_guess , num_remain , num_range1 ,num_range2 , list_num
    # if int(guess):
    #    print "Invalid literal"
    # else:
    num_guess = int(guess)
    print "您猜的数字是\n" , guess
    num_remain -=1 
    print num_remain,"次机会\n"
    if num_remain > 0:
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


def draw(canvas):
    global num_guess , num_secret , num_remain , num_range1 ,num_range2 , list_num
    canvas.draw_text('C', (80, 50), 12, 'Gray')
    canvas.draw_text('A', (20, 20), 12, 'Red')
    canvas.draw_text('B', [30, 50], 20, 'Blue')
    canvas.draw_text('C', (80, 70), 12, 'Gray', 'serif')
    pass

def auto():
    global num_guess , num_secret , num_remain , num_range1 ,num_range2 , list_num
    #if num_remain == 7
    auto_num = num_range1 + num_range2/2
    pass

def stop():
    global num_guess , num_secret , num_remain , num_range1 ,num_range2 , list_num
    pass

def review():
    timer.start()

def timer():
    global num_guess , num_secret , num_remain , num_range1 ,num_range2 , list_num , step ,order
    list = []
    order = len(review_list)
    if step < len :
        step += 1 
        for review_step in list(0,list_num):
            if review_step <len(review_list):
                 list.append(review_list[review_step])             
    else:
        step = 0
        
    pass
# create frame
f = simplegui.create_frame("Guess the number",300,300)
f.set_canvas_background("White")

timer = simplegui.create_timer(2000, timer)

# register event handlers for control elements and start frame
f.add_button("猜数区间\n [0,100 )",range100, 200)
f.add_button("猜数区间\n [0,1000 )",range1000, 200)
f.add_input("猜一个数字\n",input_guess , 200)

f.set_draw_handler(draw)
f.add_button("自动猜数字\n",auto, 200)
f.add_button("停止\n",stop, 200)
f.add_button("回放\n",review, 200)

# call new_game 
new_game()
f.start() 

# always remember to check your completed program against the grading rubric
