from PIL import Image 
from PIL import ImageEnhance 
 
def pencil_enhancement(img):  
 
    curr_sharp = ImageEnhance.Sharpness(img) 
    new_sharp = 6
    img_sharped = curr_sharp.enhance(new_sharp)
    curr_con = ImageEnhance.Contrast(img_sharped) 
    new_con = 2.5
    img_contrasted = curr_con.enhance(new_con) 
    curr_bright = ImageEnhance.Brightness(img_contrasted)
    new_bright = 0.8
    img_bright = curr_bright.enhance(new_bright)
    curr_color = ImageEnhance.Color(img_bright)
    new_color = 1
    img_enhanced = curr_color.enhance(new_color)

    return img_enhanced


def color_enhancement(img):  
 
    curr_sharp = ImageEnhance.Sharpness(img) 
    new_sharp = 4.5
    img_sharped = curr_sharp.enhance(new_sharp)
    curr_con = ImageEnhance.Contrast(img_sharped) 
    new_con = 5
    img_contrasted = curr_con.enhance(new_con) 
    curr_bright = ImageEnhance.Brightness(img_contrasted)
    new_bright = 0.8
    img_bright = curr_bright.enhance(new_bright)
    curr_color = ImageEnhance.Color(img_bright)
    new_color = 1.5
    img_enhanced = curr_color.enhance(new_color)

    return img_enhanced

def texture_enhancement(img):  
 
    curr_sharp = ImageEnhance.Sharpness(img) 
    new_sharp = 3
    img_sharped = curr_sharp.enhance(new_sharp)
    curr_con = ImageEnhance.Contrast(img_sharped) 
    new_con = 1.5
    img_contrasted = curr_con.enhance(new_con) 
    curr_bright = ImageEnhance.Brightness(img_contrasted)
    new_bright = 1.7
    img_bright = curr_bright.enhance(new_bright)
    curr_color = ImageEnhance.Color(img_bright)
    new_color = 1.5
    img_enhanced = curr_color.enhance(new_color)

    return img_enhanced

def watercolor_enhancement(img):  
 
    curr_sharp = ImageEnhance.Sharpness(img) 
    new_sharp = 1.1
    img_sharped = curr_sharp.enhance(new_sharp)
    curr_con = ImageEnhance.Contrast(img_sharped) 
    new_con = 1.1
    img_contrasted = curr_con.enhance(new_con) 

    return img_contrasted
