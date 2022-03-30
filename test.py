from PIL import Image, ImageDraw
import random
# size_px= 128
import colorsys

# points=[]
# for _ in range(10):
#     random_points=( 
#         random.randint(0,size_px),
#         random.randint(0,size_px),
#     )
#     points.append(random_points)
    
# #Drawing the points
# for i, point in enumerate(points):
#     # points len= 10
#     # points len -1 =9 
#     # 1= 1-9
#     # points[0]= first tuple in points list
    
#     print(len(points))
#     print(points)
#     f=(points)[0]
#     print(f)



h= random.random()
# setting saturation and vibrance to 100% 
s= 1
v= 1

# converting to HSC color to RGB format

# first converting into RGB but in float
float_rgb= colorsys.hsv_to_rgb(h,s,v)
# converting float RGB into integer
print(float_rgb)
for x in float_rgb:
    print(x * 255)
#     return (random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255))
# print(random_color(),random_color()[0])
