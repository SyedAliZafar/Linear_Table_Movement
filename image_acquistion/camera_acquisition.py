#!/usr/bin/env python
# coding: utf-8

# In[50]:

import os
from datetime import datetime
import cv2

#os.chdir('D:\VIMBAPYTHON\VimbaPython')

import sys

sys.path.append("D:\VIMBAPYTHON\VimbaPython")
print("Current working directory: {0}".format(os.getcwd()))
from vimba import *

### directory change##





### current time in hour month second format
#now = datetime.now()
#current_time = now.strftime("%H:%M:%S")

now = datetime.now()
current_time = now.strftime("%H-%M-%S")

print("Current Time =", current_time)


# import time
# ts = time.time()
# st = datetime.fromtimestamp(ts).strftime('%d-%m-%Y_%H-%M-%S')

# In[53]:






with Vimba.get_instance() as vimba:
    cams = vimba.get_all_cameras()
    with cams[0] as cam:
        frame = cam.get_frame()
        frame.convert_pixel_format(PixelFormat.Bgr8)
        
        #cv2.imwrite((st+'.jpg'), frame.as_opencv_image())
        path='D:\VIMBAPYTHON\VimbaPython\image_acquistion'
        cv2.imwrite(os.path.join(path , 'frame'+ ' ' +current_time+'.png'), frame.as_opencv_image())
        #cv2.imshow(("frame_"+current_time),frame.as_opencv_image())
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

#os.chdir('D:\Hardware_Implementation\XIMC_SOFTWARE\XIMC_Software_package-2022.04.25-win32_win64\libximc-2.13.5-all\examples\test_Python\standardtest')
# In[ ]:




