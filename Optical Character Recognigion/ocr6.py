from PIL import Image, ImageOps, ImageFilter
import numpy as np
import pytesseract
from firstuse import preprocess_image, predict_character, is_majority_white

# Set the path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def segment_characters(image):
    # Convert the image to grayscale
    gray_image = image.convert('L')

    # Apply Gaussian blur to reduce noise
    blurred_image = gray_image.filter(ImageFilter.GaussianBlur(radius=1))

    # Check if the majority of the image is white
    if is_majority_white(blurred_image):
        # If majority is white, invert the image
        bw_image = blurred_image.point(lambda x: 0 if x < 128 else 255, '1')
    else:
        # If majority is black, don't invert the image
        bw_image = blurred_image.point(lambda x: 255 if x < 128 else 0, '1')

    # Use Pytesseract to get bounding boxes of each character
    char_images = []
    width, height = bw_image.size

    # Get bounding boxes
    boxes = pytesseract.image_to_boxes(bw_image)  # psm 10 is for single character recognition
    avg_char_width = 0
    num_chars = 0

    for box in boxes.splitlines():
        b = box.split(' ')
        char = b[0]
        x1, y1, x2, y2 = int(b[1]), height - int(b[2]), int(b[3]), height - int(b[4])

        # Filter out faulty images by setting a minimum size threshold
        if (x2 - x1) > 5 and (y1 - y2) > 5:  # Minimum width and height thresholds
            char_image = bw_image.crop((x1, y2, x2, y1))
            char_images.append((char_image, x1, x2, y2, y1))
            avg_char_width += (x2 - x1)
            num_chars += 1

    # Calculate the average character width
    avg_char_width = avg_char_width / num_chars if num_chars > 0 else width

    return char_images, avg_char_width


# Function to perform OCR on the given image
def ocr_image(image_path):
    # Load the image
    image = Image.open(image_path)

    # Segment the image into individual characters and calculate average character width
    char_images, avg_char_width = segment_characters(image)
    space_threshold = avg_char_width * 1.5  # Threshold for space detection
    line_threshold = avg_char_width  # Threshold for detecting a new line based on y-coordinate

    # Predict each character and form the sentence
    sentence = ''
    last_x = 0
    last_y = 0
    count = 0

    for i, (char_image, start_x, end_x, start_y, end_y) in enumerate(char_images):
        if i > 0:
            if (start_x - last_x) > space_threshold:
                sentence += ' '
            if abs(start_y - last_y) > line_threshold:
                sentence += '\n'

        char_image.save(f"{count}.jpg")
        count = count + 1
        img = preprocess_image(char_image)
        predicted_char = predict_character(img)
        sentence += predicted_char
        last_x = end_x
        last_y = start_y

    return sentence




