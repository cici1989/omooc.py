
import simplegui
import random

canvas_width = 300
canvas_height = 300
dots = []
WDOTS = []


class RGBcolor:
    
    # create color with specified intensities
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    # make HTML color string
    def make_html(self):
        return "rgb(" + str(self.red) + ", " + str(self.green) + ", " + str(self.blue) + ")"
    
    # print out readable representation
    def __str__(self):
        return "Red: " + str(self.red) + ", Green: " + str(self.green) + ", Blue: " + str(self.blue)
    
    # brighten towards white
    def brighten(self):
        self.red += 1
        self.green += 1
        self.blue += 1


class WDot:
    def __init__(self, pos, color, radius, lifespan):
        # lifespan as color steps...
        self.pos = pos
        self.color = color
        self.radius = radius
        # Without lifespan, the number of dots would increase
        #	indefinitely, causing the program to slow down.
        self.life = lifespan
        self.dots = []
        self._gen_dots()
        
    def draw(self, canvas):
        for w in self.dots:
            #print w
            canvas.draw_circle(w[0]
                    , w[1]
                    , 1
                    , w[3]
                    , w[4]
                    )
        
    def _gen_dots(self):
        for d in range(self.life):
            #print d
            self.color.brighten()
            color_string = self.color.make_html()
            self.dots.append([self.pos
                       , (self.radius+(0.1*d))
                       , 1
                       , color_string, color_string
                 ])
        self.dots.reverse() #位置很重要
        #for i in self.dots : print i
    
    def update(self):
        self.life -= 1
        self.color.brighten()
        self.radius += 0.1

    def get_life(self):
        return self.life


# Event Handlers
        
def wdraw(canvas):
    for d in list(WDOTS):
        d.draw(canvas)
    return None    

def click(pos):
    new_color = RGBcolor(random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))
    print new_color
    print "HTML color is " + new_color.make_html()
    print
    WDOTS.append(WDot(pos, new_color, 7, 150))
# Frame

frame = simplegui.create_frame("Fading Dots", canvas_width, canvas_height) 

# Register Event Handlers

frame.set_draw_handler(wdraw)
frame.set_mouseclick_handler(click)
frame.set_canvas_background("White")

# Start
frame.start()
