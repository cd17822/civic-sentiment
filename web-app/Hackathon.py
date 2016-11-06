from Tkinter import *
from PIL import ImageTk, Image
from flask import Flask, jsonify, request
import thread
import random
import time

app = Flask(__name__)
root = Tk()

def toggle_fullscreen(event=None):
	root.attributes("-fullscreen", True)
	return "break"

def end_fullscreen(event=None):
	root.attributes("-fullscreen", False)
	return "break"

root.title("Donald Trump vs Hillary Clinton")
root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", end_fullscreen)
screen_height = root.winfo_screenheight()
print("Screen Height:", screen_height)
screen_width = root.winfo_screenwidth()
print("Screen Width:", screen_width)
canvas = Canvas(root, width = screen_width, height = screen_height)
canvas.pack()


TRUMP_UPS = 0
CLINTON_UPS = 0
TRUMP_PICS = 0
CLINTON_PICS = 0

def middle_pixel(filename):
	with Image.open(filename) as im:
		width, height = im.size
	mid_height = (height / 2)
	mid_width = (width / 2)
	return [mid_width, mid_height]

def draw_initial(): pass
usa_path = "public/images/flagbg"
donald_path = "public/images/trumpgood.png"
hillary_path = "public/images/hillgood.png"
donaldqr_path = "public/images/trumpqr.png"
clintonqr_path = "public/images/clintonqr.png"

usa = PhotoImage(file=usa_path)
donald = PhotoImage(file=donald_path)
hillary = PhotoImage(file = hillary_path)
donaldqr = PhotoImage(file=donaldqr_path)
hillaryqr = PhotoImage(file = hillaryqr_path)
                                                                                        
canvas.create_image(middle_pixel(usa_path)[0], middle_pixel(usa_path)[1],image=usa)
canvas.create_image(middle_pixel(hillary_path)[0]-150, screen_height - middle_pixel(hillary_path)[1],image=hillary)
canvas.create_image((screen_width - middle_pixel(donald_path)[0])+100, screen_height - middle_pixel(donald_path)[1]+250, image=donald)
canvas.create_image(300, screen_height-300,image=hillaryqr)
canvas.create_image(screen_width-300, screen_height-300, image=donaldqr)

def getVotes():
        file = open("votes.txt")
        string = ""
        for line in file.readlines():
                string = line
                break
        
        for c in string:
                if c == '1': CLINTON_UPS += 1
                if c == '2': TRUMP_UPS   += 1

def draw_slider():
        total = TRUMP_UPS + CLINTON_UPS
        canvas.create_rectangle(0,0,100,100)

def flaskThread():
        app.run()

def trumpFireworks():
        r1 = random.randint(50, screen_width/2 -50)
        r2 = random.randint(50, screen_height-50)
        
        for i in xrange(25):
                format = "gif -index " + str(i)
                fireworks = PhotoImage(file="public/images/fireworks.gif", format=format)        
                canvas.create_image(screen_width/2 + r1, r2, image=fireworks)
                time.sleep(.01)

def clintonFireworks():
        r1 = random.randint(50, screen_width/2 -50)
        r2 = random.randint(50, screen_height-50)
        
        for i in xrange(25):
                format = "gif -index " + str(i)
                fireworks = PhotoImage(file="public/images/fireworks.gif", format=format)        
                canvas.create_image(r1, r2, image=fireworks)
                time.sleep(.01)

@app.route('/trump')
def trumpx(*args):
        #TRUMP_UPS += 1
        thread.start_new_thread(trumpFireworks, ())
        
@app.route('/clinton')
def clintonx(*args):
        #CLINTON_UPS += 1
        thread.start_new_thread(clintonFireworks(), ())

@app.route('/clintonpic')
def clintonp(*args):
        print "picccc"
        all_args = request.args.to_dict()
        print all_args
        filename = all_args['filename']
        print filename
        pic = PhotoImage(file="uploads/"+filename)
        print "gotdamn"
        pic_potential = screen_width/2/128
        print "shit"
        canvas.create_image((CLINTON_PICS % pics_potential)*128, (CLINTON_PICS / pics_potential)*128,
                            ((CLINTON_PICS % pics_potential)+1)*128, ((CLINTON_PICS / pics_potential)+1)*128)
        print "um"
        CLINTON_PICS += 1
        print "no"
        canvas.create_image(middle_pixel(hillary_path)[0]-150, screen_height - middle_pixel(hillary_path)[1],image=hillary)

root.bind("<<TRUMP>>", trumpx)
root.bind("<<CLINTON>>", clintonx)

draw_initial()
getVotes()
#draw_slider()
thread.start_new_thread(flaskThread,())
#root.attributes("-fullscreen", TRUE)
root.mainloop()


