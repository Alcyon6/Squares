import os
import sys
from PIL import Image, ImageOps

# Get the path to the source directory from the command line argument
# If no argument is provided, use the current directory as the source
src_dir = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.getcwd()

# Path to the destination directory where the processed images will be saved
# If the source is a single file, the destination will be the same directory as the source
# If the source is a directory, the destination will be a subdirectory named "processed" inside the source directory
if os.path.isdir(src_dir):
    dest_dir = os.path.join(src_dir, 'processed')
else:
    dest_dir = os.path.dirname(src_dir)

# Make sure the destination directory exists, create it if it doesn't
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Check if the source is a directory or a single file
if os.path.isdir(src_dir):
    # If the source is a directory, loop through all the files in the directory
    for filename in os.listdir(src_dir):
        # Check if the file is a JPEG image
        if filename.endswith(".jpg"):
            # Open the image using the Pillow library
            image = Image.open(os.path.join(src_dir, filename))

            # Get the dimensions of the image
            width, height = image.size

            # Calculate the size of the shortest side of the image
            min_side = min(width, height)

            # Create a new image that is a square with the shortest side being 512 pixels
            new_image = Image.new('RGB', (512, 512), (255, 255, 255))

            # Calculate the starting position of the crop
            x_pos = int((width - min_side) / 2)
            y_pos = int((height - min_side) / 2)

            # Crop the image
            cropped_image = image.crop((x_pos, y_pos, x_pos + min_side, y_pos + min_side))

            # Resize the cropped image to 512x512 pixels
            resized_image = ImageOps.fit(cropped_image, (512, 512), method=Image.Resampling.LANCZOS)

            # Paste the resized image onto the new image
            new_image.paste(resized_image, (0, 0))

            # Save the new image to the destination directory
            new_image.save(os.path.join(dest_dir, filename))
else:
    # If the source is a single file, open the image using the Pillow library
    image = Image.open(src_dir)

    # Get the dimensions of the image
    width, height

