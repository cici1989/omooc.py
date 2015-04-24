import user39_JBubUS5f1b_1 as cici
import simplegui
import random

canvas_width = 300
canvas_height = 300
#WDOTS = [] 这个要放到class中，否则报错 WDOTS 是无效的。
n_color = 0


# Event Handlers
        
def wdraw(canvas):
    for d in list(cici.WDOTS):
        d.draw(canvas)
    return None    

def click(pos):
    if n_color == 1:
        new_color = cici.RGBcolor(256, 0, 0)
    elif n_color == 2:
        new_color = cici.RGBcolor(0, 200, 0) 
    elif n_color == 3:
        new_color = cici.RGBcolor(0, 0, 256)         
    else:    
        new_color = cici.RGBcolor(random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))
    print new_color
    print "HTML color is " + new_color.make_html()
    print
    cici.WDOTS.append(cici.WDot(pos, new_color, 3, 150))
    
def click_red():
    global n_color
    n_color = 1

def click_green():
    global n_color
    n_color = 2
    
def click_blue():
    global n_color
    n_color = 3

def click_random():
    global n_color
    n_color = 0


    
# Frame

frame = simplegui.create_frame("Fading Dots", canvas_width, canvas_height) 

# Register Event Handlers
frame.add_button("红色\n",click_red,100)
frame.add_button("绿色\n",click_green,100)
frame.add_button("蓝色\n",click_blue,100)
frame.add_button("随机颜色\n",click_random,100)

frame.set_draw_handler(wdraw)
frame.set_mouseclick_handler(click)
frame.set_canvas_background("White")

# Start
frame.start()
