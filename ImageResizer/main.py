import cv2


# Configurable parameters
source = 'img.png'
destination = 'newImg.jpeg'
scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

#calculate 50 percent of the original dimensions
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

#resize img
output = cv2.resize(src, (new_width,new_height))

cv2.imwrite(destination,output)

cv2.waitKey(0)

