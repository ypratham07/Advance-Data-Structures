from PIL import Image, ImageFilter

# Open the image
image = Image.open("test_image.jpg")

# Resize the image (thumbnail method modifies the image in-place)
image.thumbnail((90, 90))

# Display the thumbnail
image.show()