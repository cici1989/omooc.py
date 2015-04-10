# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
# 遇到第一个问题，回放不是一步一步的——已解决。
# 遇到第二个问题，不会同时添加多个 timer，
## 思路是 ai 猜数字回放、手动猜数字过程回放、ai 自动猜数字各一个timer。

import simplegui
import random
import math

# initialize global variables used in your code here  
global num_guess , num_secret , num_remain  ,num_range2 ,num_auto 
num_range1 = 0 
list1 = []
list2 = []
list_num = 0
review_list = []
step = 0
order = 0

# helper function to start and restart the game
def new_game():
    pass

# define event handlers for control panel
def num_range1(n):
    global num_range1 
    num_range1 = int(n)
    
def num_range2(n):
    global num_range1 , num_range2 ,num_guess , num_secret , num_remain , list_num
    num_range2 = int(n)  
    num_secret = random.randint(num_range1, num_range2) 
    print u"请在",num_range1,u"到",num_range2,"之间猜。\n"

#def range100():
#    # button that changes the range to [0,100) and starts a new game 
#    global num_guess , num_secret , num_remain , num_range1 ,num_range2 , list_num
#    num_range1
#    num_range2 = 100
#    num_secret = random.randint(num_range1, num_range2) 
#    
#    num_remain = 7
#    #print '可猜数字区间0到100\n',num_remain,'次机会\n'
#    list.append('可猜数字区间0到100\n'+str(num_remain)+'次机会\n')
#    print list[list_num]  
#    list_num += 1 
#    return num_remain
#    return review_list
#
#def range1000():
#    # button that changes the range to [0,1000) and starts a new game     
#    global num_guess , num_secret , num_remain , num_range1 ,num_range2 , list_num
#    num_secret = random.randint(0, 1000)
#    num_range2 = 1000
#    num_remain = 10
#    #print "可猜数字区间0到100\n",num_remain,"次机会\n"
#    list.append('可猜数字区间0到1000\n'+str(num_remain)+'次机会\n')
#    print list[list_num]  
#    list_num += 1 
#    review_list = list
#    return num_remain
    
def input_guess(guess):
    global num_guess , num_remain , num_range1 ,num_range2 , list_num
    num_guess = int(guess)
    if num_guess == num_secret:
                print u"您猜的数字是",guess,"，猜对了！\n"
                list1.append(u"您猜的数字是"+guess+"，猜对了！\n")
    elif num_range1 < num_guess < num_secret:
                print u"您猜的数字是",guess,"，猜小了！\n"
                list1.append(u"您猜的数字是"+guess+"，猜小了！\n")
                num_range1 = num_guess
                print u"请在",num_range1,u"到",num_range2,"之间继续猜。\n"
    elif num_secret < num_guess < num_range2:
                print u"您猜的数字是",guess,"，猜大了！\n"
                list1.append(u"您猜的数字是"+guess+"，猜大了！\n")
                num_range2 = num_guess
                print u"请在",num_range1,u"到",num_range2,"之间继续猜。\n"
    elif num_guess < num_range1 or num_guess > num_range2:     
                print u"您猜的数字是",guess,"，超出区间！\n"
                list1.append(u"您猜的数字是"+guess+"，超出区间！\n")
                print u"请在",num_range1,u"到",num_range2,"之间猜。\n"

def draw(canvas):
    global num_guess , num_secret , num_remain , num_range1 ,num_range2 , list_num
    pass

def auto():
    global num_guess , num_secret , num_remain , num_range1 ,num_range2 , list_num
    num_guess = (num_range1 + num_range2)/2
    if num_guess == num_secret:
                print u"ai猜的数字是",num_guess,"，猜对了！\n"
                list2.append(u"ai猜的数字是"+str(num_guess)+"，猜对了！\n")
    elif num_range1 < num_guess < num_secret:
                print u"ai猜的数字是",num_guess,"，猜小了！\n"
                list2.append(u"ai猜的数字是"+str(num_guess)+"，猜小了！\n")
                num_range1 = num_guess
                print u"请在",num_range1,u"到",num_range2,"之间继续猜。\n"
    elif num_secret < num_guess < num_range2:
                print u"ai猜的数字是",num_guess,"，猜大了！\n"
                list2.append(u"ai猜的数字是"+str(num_guess)+"，猜大了！\n")
                num_range2 = num_guess
                print u"请在",num_range1,u"到",num_range2,"之间继续猜。\n"
    elif num_guess < num_range1 or num_guess > num_range2:     
                print u"ai猜的数字是",num_guess,"，超出区间！\n"
                list2.append(u"ai猜的数字是"+str(num_guess)+"，超出区间！\n")
                print u"请在",num_range1,u"到",num_range2,"之间猜。\n"
    
#def stop():
#    global num_guess , num_secret , num_remain , num_range1 ,num_range2 , list_num
#    pass

def review1():
    print "手动猜数字过程回放：\n"
    step = 0
    if step < 1:
        step += 1
        for l in list1:
            print l


def review2():
    if timer.is_running() :
        timer.stop()
    else:
        print "ai猜数字过程回放：\n"
        timer.start()  
        
def count():
    print u'ai一共猜了', len(list2),'次\n'


def timer():
    global num_guess , num_secret , num_remain , num_range1 ,num_range2 , list_num , step ,order
    if step < len(list2):
        print list2[step]
        step+=1 
    else:
        timer.stop()
#    for l in list2:
#            print l
#    timer.stop()

    

#    if step < 1:
#        step += 1
#        for l in list1:
#            print l
#

#    list = []
#    order = len(review_list)
#    if step <= order :
#        step += 1 
#        for review_step in range(0,step):
#            if review_step <len(review_list):
#                 list.append(review_list[review_step])   
#            print list[step] 
#    else:
#        step = 0
#    
# create frame
f = simplegui.create_frame("Guess the number",400,500)
f.set_canvas_background("White")

timer = simplegui.create_timer(1000, timer)


# register event handlers for control elements and start frame
f.add_input("猜数区间下限，请填入不小于0的数字：\n",num_range1, 200)
f.add_input("猜数区间上限，请填入大于下限的数字：\n",num_range2, 200)

#f.add_button("猜数区间\n [0,100 )",range100, 200)
#f.add_button("猜数区间\n [0,1000 )",range1000, 200)
f.add_input("手动猜数字，请填入所猜数字：\n",input_guess , 200)

f.set_draw_handler(draw)
f.add_button("自动猜数字\n",auto, 200)
f.add_button("回放手动操作战况\n",review1, 200)
f.add_button("回放ai战况\n",review2, 200)
#f.add_button("停止\n",stop, 200)
f.add_button("统计ai能力\n",count, 200)


# call new_game 
new_game()
f.start() 

# always remember to check your completed program against the grading rubric
