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
canvas = Canvas(root, width=screen_width, height=screen_height)
canvas.pack()
usa_path = "flagbg.png"
usa = ImageTk.PhotoImage(file=usa_path)
canvas.create_image(middle_pixel(usa_path)[0],middle_pixel(usa_path)[1],image=usa)

donald_path = "trumpok.png"
hillary_path = "hillgood.png"

donald = ImageTk.PhotoImage(file=donald_path)
#donald = donald.zoom(3,3)
hillary = ImageTk.PhotoImage(Image.open(hillary_path))
#hillary = hillary.zoom(5,5)
#hillary = hillary.subsample(2,2)
#canvas.create_image(middle_pixel(donald_path)[0] * 2, screen_height - middle_pixel(donald_path)[1] * 3,image=donald)
#canvas.create_image(screen_width - middle_pixel(hillary_path)[0] * 1.5, screen_height - middle_pixel(hillary_path)[1] * 2.5, image=hillary)
canvas.create_image(0, 0, image=donald)
canvas.create_image(0,0, image=hillary)

root.attributes("-fullscreen", TRUE)
root.mainloop()

