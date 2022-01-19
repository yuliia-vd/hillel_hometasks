from PIL import Image

my_image = Image.open('milie-sobaki-i-koshki.jpg')
width, height = my_image.size

new_width = int(input('Enter new_width: '))
new_height = int(input('Enter new_height: '))

if new_height == 0:
    new_height = int(new_width*height/width)
elif new_width == 0:
    new_width = int(new_height*width/height)

my_image2 = my_image.resize((new_width, new_height), Image.ANTIALIAS)
my_image2.show()