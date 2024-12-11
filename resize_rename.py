import os
from PIL import Image

def resize_images_to_fixed_aspect_ratio(input_folder, output_folder, target_width=1080):
    # Calculate the target height based on the 4:3 aspect ratio
    target_height = int((3 / 4) * target_width)
    target_size = (target_width, target_height)

    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Counter for sequential naming
    counter = 1

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        # Only process image files (you can extend this for more image types)
        if filename.endswith('.jpg'):
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)

            # Resize the image while maintaining the aspect ratio
            image.thumbnail(target_size)

            # Create a new image with the desired size and black background
            new_image = Image.new('RGB', target_size, (0, 0, 0))

            # Calculate position to center the resized image
            x_offset = (target_size[0] - image.width) // 2
            y_offset = (target_size[1] - image.height) // 2

            # Paste the resized image onto the new image
            new_image.paste(image, (x_offset, y_offset))

            # Generate sequential name
            new_filename = f"IMG_b{counter:03d}.jpg"
            counter += 1

            # Save the padded image to the output folder
            output_path = os.path.join(output_folder, new_filename)
            new_image.save(output_path)

            print(f"Resized and saved: {new_filename}")

# Usage
input_folder = 'D:/ODP2/image_collection/collected_imgs/3-12-24-R'
output_folder = 'D:/ODP2/image_collection/collected_imgs/Resized'
resize_images_to_fixed_aspect_ratio(input_folder, output_folder)

print ("\n \t\t\tDone")
