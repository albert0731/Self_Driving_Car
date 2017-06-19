import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


# Read in the image and print out some stats
image = mpimg.imread('Color_Selection_Test_Input.jpg')
print('This image is: ', type(image), 'with dimensions:', image.shape)

# Grab the x and y size and make a copy of the image
ysize = image.shape[0]
xsize = image.shape[1]
# Note: always make a copy rather than simply using "="
color_select = np.copy(image)


# Define our color selection criteria
# Note: if you run this code, you'll find these are not sensible values!!
# But you'll get a chance to play with them soon in a quiz
red_threshold = 200
green_threshold = 200
blue_threshold = 200
rgb_threshold = [red_threshold, green_threshold, blue_threshold]

# Identify pixels below the threshold
# Note: image [x, y, (r,g,b)], thresholds is an array of true/false values
thresholds = (image[:, :, 0] < rgb_threshold[0]) \
           | (image[:, :, 1] < rgb_threshold[1]) \
           | (image[:, :, 2] < rgb_threshold[2])

color_select[thresholds] = [0, 0, 0]

# Display the image
plt.imshow(color_select)
plt.imsave('01_Color_Selection.png', color_select)
plt.show()
