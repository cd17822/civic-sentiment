from PIL import Image
import sys
import os

def main(filename):
    needs_rotation = False
    if len(filename.split(".jp")) > 1:
        needs_rotation = True

    img = Image.open(filename)
    half_the_width = img.size[0] / 2
    half_the_height = img.size[1] / 2
    m = min(img.size)/2
    img = img.crop(
        (
            half_the_width - m,
            half_the_height - m,
            half_the_width + m,
            half_the_height + m
        )
    )
    img.thumbnail((100,100), Image.ANTIALIAS)
    new_name = filename.split('.')[0] + ".png"
    if needs_rotation:
        img = img.rotate(270)
    img.save(new_name, "PNG")
    
    print "processed"
    sys.stdout.flush()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
