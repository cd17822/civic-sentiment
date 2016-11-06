from Tkinter import *
from PIL import ImageTk, Image
from flask import Flask, jsonify, request
import thread
import random
import time
import os
import glob

app = Flask(__name__)
root = Tk()

#delete all past uploads
files = glob.glob('cuploads/*')
for f in files: os.remove(f)
files = glob.glob('tuploads/*')
for f in files: os.remove(f)
#delete all past votes
open("votes.txt", "w").close()

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

#OVERRIDES
#screen_width = 1184
#screen_height = 624


canvas = Canvas(root, width = screen_width, height = screen_height, highlightthickness=0)
canvas.pack()

def middle_pixel(filename):
	with Image.open(filename) as im:
		width, height = im.size
	mid_height = (height / 2)
	mid_width = (width / 2)
	return [mid_width, mid_height]

usa_path = "public/images/flagbg"
donald_path = "public/images/trumpgood.png"
hillary_path = "public/images/hillgood.png"
donaldqr_path = "public/images/trumpqr.png"
clintonqr_path = "public/images/clintonqr.png"
scroll_path = "public/images/scroll.png"

usa = PhotoImage(file=usa_path)
donald = PhotoImage(file=donald_path)
hillary = PhotoImage(file=hillary_path)
donaldqr = PhotoImage(file=donaldqr_path)
hillaryqr = PhotoImage(file=clintonqr_path)
scroll = PhotoImage(file=scroll_path)

canvas.create_image(middle_pixel(usa_path)[0], middle_pixel(usa_path)[1],image=usa)

def drawForeground():
        canvas.create_image(middle_pixel(hillary_path)[0]-230, screen_height - middle_pixel(hillary_path)[1] + 230,image=hillary)
        canvas.create_image((screen_width - middle_pixel(donald_path)[0])+200, screen_height - middle_pixel(donald_path)[1]+450, image=donald)
        canvas.create_image(115, screen_height-115,image=hillaryqr)
        canvas.create_image(screen_width-115, screen_height-115, image=donaldqr)
        canvas.create_image(screen_width/2, 100, image=scroll)

def getVotes():
        file = open("votes.txt", 'r')
        string = ""
        clints = 0
        trumps = 0
        for line in file.readlines():
                string = line
                break
        
        for c in string:
                if c == '1': clints += 1
                if c == '2': trumps += 1
        file.close()
        return clints, trumps

def drawMeter():
        clints, trumps = getVotes()
        total = clints + trumps
        midw = screen_width/2
        midh = screen_height/2
        start = midw - 150
        end = midw + 150
        mid_real = start + 150
        try:
                mid_real = (clints*1.0 / total)*300 + start
        except:
                pass
        canvas.create_rectangle(start, midh-30, mid_real, midh+30, fill="blue", width=0)
        if clints > 0 or trumps == 0:
                canvas.create_oval(midw-180, midh-30, midw-120, midh+30, fill="blue", width=0)
        else:
                canvas.create_oval(midw-180, midh-30, midw-120, midh+30, fill="red", width=0)
        canvas.create_rectangle(mid_real, midh-30, end, midh+30, fill="red", width=0)
        if trumps > 0 or clints == 0:
                canvas.create_oval(midw+130, midh-30, midw+180, midh+30, fill="red", width=0)
        else:
                canvas.create_oval(midw+130, midh-30, midw+180, midh+30, fill="blue", width=0)
        clint_pct = "50%"
        trump_pct = "50%"
        print "feawfa"
        print total
        if total != 0:
                clint_pct = str(int(round((clints*1.0/total)*100))) + "%"
                print clint_pct
                trump_pct = str(int(round((trumps*1.0/total)*100))) + "%"
                print clint_pct
        
        canvas.create_text(midw-140, midh, text=clint_pct, fill="white", font=("Courier", 18))
        canvas.create_text(midw+140, midh, text=trump_pct, fill="white", font=("Courier", 18))

drawForeground()
drawMeter()

def draw_slider():
        total = TRUMP_UPS + CLINTON_UPS
        canvas.create_rectangle(0,0,100,100)

def flaskThread():
        app.run()

fireworkses = []
def trumpFireworks():
        r1 = random.randint(200, screen_width/2 -50)
        r2 = random.randint(50, screen_height/2)
        
        for i in xrange(10):
                format = "gif -index " + str(i)
                fireworks = PhotoImage(file="public/images/fireworks.gif", format=format)        
                fireworkses.append(fireworks)
                canvas.create_image(screen_width/2 + r1, r2, image=fireworks)
                time.sleep(.1)
                fireworkses.remove(fireworks)

def clintonFireworks():
        r1 = random.randint(50, screen_width/2 -200)
        r2 = random.randint(50, screen_height/2)
        
        for i in xrange(10):
                format = "gif -index " + str(i)
                fireworks = PhotoImage(file="public/images/fireworks.gif", format=format)
                fireworkses.append(fireworks)
                canvas.create_image(r1, r2, image=fireworks)
                time.sleep(.1)
                fireworkses.remove(fireworks)

def  writeVote(indexOfVote): # (hill is 1, trump is 2)
        print "lets"
        file = open("votes.txt", 'r')
        print "opened"
        string = ""
        for line in file.readlines():
                string = line
                break
        clints = 0
        trumps = 0
        for c in string:
                if c == '1':
                        clints += 1
                elif c == '2':
                        trumps += 1
        file.close()
        print "read"
        file = open("votes.txt", 'a')
        file.write(str(indexOfVote))
        file.close()
        print "written"
        return clints, trumps

def getNumPics(x): # c for clinton, t for trump
        for file in os.listdir(x+"uploads"):
                print file
                if not (file.endswith(".PNG") or file.endswith(".png")):
                        print file
                        os.remove(x+"uploads/"+file)
                        print "removed"
        print "looped"
        path, dirs, files = os.walk(x+"uploads").next()
        print len(files)
        return len(files)

voter_pics = [] # just so they dont get fucking garbage collected like honestly fuck tkinter
def drawClintonPhoto(pic):
        voter_pics.append(pic)
        print "lolkilme"
        pic_potential = screen_width/2/128 - 1
        print "shit"
        
        clint_pics = getNumPics('c')
        print "rly"
        canvas.create_image((clint_pics % pic_potential)*100-50, (clint_pics / pic_potential)*100+50, image=pic)
        
def drawTrumpPhoto(pic):
        voter_pics.append(pic)
        print "lolkilme"
        pic_potential = screen_width/2/128 - 1
        print "shit"
        
        trump_pics = getNumPics('t')
        print "rly"
        canvas.create_image(screen_width-(trump_pics % pic_potential)*100+50, (trump_pics / pic_potential)*100+50, image=pic)

@app.route('/trump')
def trumpx(*args):
        clints, trumps = writeVote(2)
        thread.start_new_thread(trumpFireworks, ())
        drawMeter()
        return ""

@app.route('/clinton')
def clintonx(*args):
        clints, trumps = writeVote(1)
        thread.start_new_thread(clintonFireworks, ())
        drawMeter()
        return ""

@app.route('/clintonpic')
def clintonp(*args):
        print "picccc"
        all_args = request.args.to_dict()
        print all_args
        filename = all_args['filename']
        print filename
        pic = PhotoImage(file="cuploads/"+filename)
        print "gotdamn"
        drawClintonPhoto(pic)
        drawForeground()

        return "hilled"

@app.route('/trumppic')
def trumpp(*args):
        print "tpicccc"
        all_args = request.args.to_dict()
        print all_args
        filename = all_args['filename']
        print filename
        pic = PhotoImage(file="tuploads/"+filename)
        print "gotdamn"
        drawTrumpPhoto(pic)
        drawForeground()

        return "trumped"

thread.start_new_thread(flaskThread,())
#OVERRIDES 
root.attributes("-fullscreen", TRUE)
root.mainloop()


