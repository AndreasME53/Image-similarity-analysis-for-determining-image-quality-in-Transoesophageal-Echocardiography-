import scipy.io as sio
import numpy as np
import cv2
import math 
#import skimage 

# function to overlay two images
def imshowpair(fixed, moving, figureTitle = ''):
    im_falsecolor = np.dstack((moving, fixed, fixed))
    cv2.imshow(figureTitle,im_falsecolor)
    cv2.waitKey(0)


# Import the TOE image dataset from the cw2.mat file attached to Coursework 2 material on Moodle
cw2_data = sio.loadmat('cw2.mat') # Change to the path of the cw2.mat file

# The test image of particpant 6 for the view 4 can be accessed as: 
test6_4 = cw2_data['test_img'][5][3]

# The gold image for the 7 view can be accessed as: 
gold_7 = cw2_data['gold_img'][0][6]


