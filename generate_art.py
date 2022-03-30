from PIL import Image, ImageDraw, ImageChops
import random
import colorsys
# Picking up bringht colors in the form of HSV and then converting it into RGB
def random_color():
    h= random.random()
    # setting saturation and vibrance to 100% 
    s= 1
    v= 1

    # converting to HSC color to RGB format

    # first converting into RGB but in float
    float_rgb= colorsys.hsv_to_rgb(h,s,v)
    # converting float RGB into integer
    rgb= [int(x*255) for x in float_rgb]

    return tuple(rgb)

    # older method- producing random RGB colors
    # return (random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255))

def interpolate(start_color,end_color,factor:float):
    recip = 1- factor
    return(
        int(start_color[0]*recip+end_color[0]*factor),
        int(start_color[1]*recip+end_color[1]*factor),
        int(start_color[2]*recip+end_color[2]*factor),
    )



def creator(path:str):
    print('Generating...')
    #size and color should always be tuple 
    target_size= 256
    scale_factor=2
    size_px= target_size*scale_factor
    color=(0,0,0)
    start_color= random_color()
    end_color= random_color()
    #defining the padding number.
    padding_px= 16* scale_factor
    image= Image.new('RGB',size= (size_px,size_px),color= color)
    

    #Draw some lines
    draw= ImageDraw.Draw(image)

    points=[]
    #Generating the points. 
    for _ in range(10):
        random_points=(
            #adding the padding
            random.randint(padding_px,size_px - padding_px),
            random.randint(padding_px,size_px - padding_px),
        )
        points.append(random_points)

    #drawing bounding box
    # min_x= min([p[0] for p in points])
    # max_x= max([p[0] for p in points])
    # min_y= min([p[1] for p in points])
    # max_y= max([p[1] for p in points])
    # draw.rectangle((min_x,max_y,max_x,min_y), outline=(255,0,0))

    # Centering the image


        
    #joining all the points and then drawing them in order to form a particular shape.
    thickness=0
    n_points= len(points)-1
    for i, point in enumerate(points):

        # overlay canvas
        overlay_image= Image.new('RGB',size= (size_px,size_px),color= (0,0,0))
        #Draw some lines
        overlay_draw= ImageDraw.Draw(overlay_image)



        # joining the lines together using some cool programming :)
        
        p1= point
        if i== n_points:
            p2= points[0]
        else: 
            p2= points[i + 1]
        
        
        line_xy= (p1, p2)
        color_factor= i/ n_points
        line_color= interpolate(start_color,end_color,color_factor)
        thickness+= scale_factor
        overlay_draw.line(line_xy, fill=line_color,width=thickness )
        image= ImageChops.add(image, overlay_image)
        
    image=image.resize((target_size,target_size),resample=Image.ANTIALIAS)
    image.save(path)




for i in range(10):
    creator(f"test_imge_{i}.png")
