from Tkinter import *
from PIL import ImageTk, Image

root = Tk()

def toggle_fullscreen(event=None):
	root.attributes("-fullscreen", True)
	return "break"

def end_fullscreen(event=None):
	root.attributes("-fullscreen", False)
	return "break"

def middle_pixel(filename):
	with Image.open(filename) as im:
		width, height = im.size
	mid_height = (height / 2)
	mid_width = (width / 2)
	return [mid_width, mid_height]

	 

root.title("Donald Trump vs Hillary Clinton")
root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", end_fullscreen)
screen_height = root.winfo_screenheight()
print("Screen Height:", screen_height)
screen_width = root.winfo_screenwidth()
print("Screen Width:", screen_width)
canvas = Canvas(root, width = screen_width, height = screen_height)
canvas.pack()
usa_path = "public/images/flagbg.png"
#usa = PhotoImage(file=usa_path)
#canvas.create_image(middle_pixel(usa_path)[0],middle_pixel(usa_path)[1],image=usa)

"""TopRight = Canvas(canvas, width = (1/3 * screen_width), height = (1/3 * screen_height)
TopMiddle = Canvas(canvas, width = (1/3 * screen_width), height = (1/3 * screen_height)
TopLeft = Canvas(canvas, width = (1/3 * screen_width), height = (1/3 * screen_height)
TopRight.pack(side = RIGHT)
TopMiddle.pack(side = RIGHT)
TopLeft.pack(side = RIGHT)"""

#subsample(self, x = '', y='')
#Return a new photoimage based on the same image as this widget but use only every Xth or Yth pixel


donald_path = "public/images/trumpok.png"
hillary_path = "public/images/hillgood.png"

donald = PhotoImage(file=donald_path)
#donald = donald.zoom(3,3)
hillary = PhotoImage(file = hillary_path)
#hillary = hillary.zoom(5,5)
#hillary = hillary.subsample(2,2)
canvas.create_image(middle_pixel(hillary_path)[0]-50, screen_height - middle_pixel(hillary_path)[1],image=hillary)
canvas.create_image(screen_width - middle_pixel(donald_path)[0], screen_height - middle_pixel(donald_path)[1], image=donald)


root.attributes("-fullscreen", TRUE)
root.mainloop()

