from PIL import Image, ImageFilter
img = Image.open('/Users/mothilaljadhav/Desktop/Projects/Python/Scripting/image_processing/cricketers/blurred.jpeg')

filtered_image = img.filter(ImageFilter.EMBOSS)

filtered_image.save('emboss.png','png')