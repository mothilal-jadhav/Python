from PIL import Image, ImageFilter
img = Image.open('/Users/mothilaljadhav/Desktop/Projects/Python/Scripting/image_processing/cricketers/virat_kohli.jpg')




img.thumbnail((858,600))

img.save('virat_kohli_imax_ratio.png','png')