# The code imports the remove function from the rembg module
# and the Image module from the Python Imaging Library (PIL)


from rembg import remove
from PIL import Image 

# Below line opens an image file using the Image.open() method 
# and stores it in the img variable. 
img = Image.open("birds-pet-parrot.jpg")
# Remove argument to remove the background of the image
R = remove(img)
# Save the image
R.save("img1.png")
