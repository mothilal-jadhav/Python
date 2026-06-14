from PIL import Image, ImageFilter
img = Image.open('/Users/mothilaljadhav/Desktop/Projects/Python/Scripting/image_processing/cricketers/blurred.jpeg')

filtered_image = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

filtered_image.save('smoothen.png','png')