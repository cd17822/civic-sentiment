from Tkinter import *
from PIL import ImageTk, Image
from flask import Flask

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


def middle_pixel(filename):
	with Image.open(filename) as im:
		width, height = im.size
	mid_height = (height / 2)
	mid_width = (width / 2)
	return [mid_width, mid_height]

def draw_initial():
        
        usa_path = "public/images/flagbg"
        donald_path = "public/images/trumpgood.png"
        hillary_path = "public/images/hillgood.png"

        usa = PhotoImage(file=usa_path)
        donald = PhotoImage(file=donald_path)
        hillary = PhotoImage(file = hillary_path)
        
        canvas.create_image(middle_pixel(usa_path)[0], middle_pixel(usa_path)[1],image=usa)
        canvas.create_image(middle_pixel(hillary_path)[0]-150, screen_height - middle_pixel(hillary_path)[1],image=hillary)
        canvas.create_image((screen_width - middle_pixel(donald_path)[0])+100, screen_height - middle_pixel(donald_path)[1]+250, image=donald)

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
        total = 0
        

draw_initial()
getVotes()
draw_slider()
app.run(debug=True, host='0.0.0')
root.attributes("-fullscreen", TRUE)
root.mainloop()

