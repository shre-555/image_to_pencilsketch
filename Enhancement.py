from PIL import Image, ImageEnhance, ImageFilter

def enhance_contrast(image, contrast_factor=1.2):
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(contrast_factor)
    return enhanced_image

def enhance_brightness(image, brightness_factor=1.2):
    enhancer = ImageEnhance.Brightness(image)
    enhanced_image = enhancer.enhance(brightness_factor)
    return enhanced_image

def enhance_sharpness(image, sharpness_factor=2.0):

    enhancer = ImageEnhance.Sharpness(image)
    enhanced_image = enhancer.enhance(sharpness_factor)
    return enhanced_image

def enhance_image(image, contrast_factor=1.2, brightness_factor=1.2, sharpness_factor=2.0):

    enhanced_image = enhance_contrast(image, contrast_factor)

    enhanced_image = enhance_brightness(enhanced_image, brightness_factor)

    enhanced_image = enhance_sharpness(enhanced_image, sharpness_factor)

    return enhanced_image

image_path = image

input_image = Image.open(image_path)

enhanced_image = enhance_image(input_image)

return image
# enhanced_image.show()
