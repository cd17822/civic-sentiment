from PIL import Image
import sys

def main(filename):
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
    img.thumbnail((128,128), Image.ANTIALIAS)
    img.save(filename)

    print "processed"
    sys.stdout.flush()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
