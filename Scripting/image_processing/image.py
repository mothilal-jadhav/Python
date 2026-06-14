from PIL import Image, ImageFilter
img = Image.open('/Users/mothilaljadhav/Desktop/Projects/Python/Scripting/image_processing/cricketers/virat_kohli.jpg')

filtered_image = img.convert('L')

box = (150,150,900,900)
region = filtered_image.crop(box)



region.save('virat_kohli_cropped.png','png')