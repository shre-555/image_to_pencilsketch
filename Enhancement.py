from PIL import Image, ImageEnhance

def enhance_image(img, sharpness=1, contrast=1, brightness=1, color=1):
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(sharpness)

    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)

    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(brightness)

    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(color)

    return img
