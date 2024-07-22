from PIL import Image, ImageOps
import numpy as np
import pickle

# Function to check if the majority of the image is white
def is_majority_white(image, threshold=0.5):
    # Convert image to numpy array
    img_array = np.array(image)
    # Calculate the fraction of white pixels
    white_pixels = np.sum(img_array > 128)
    total_pixels = img_array.size
    return (white_pixels / total_pixels) > threshold

def invert_image(image):
    if is_majority_white(image):
        return ImageOps.invert(image)
    return image

# Load and preprocess the image
def load_image(image_path):
    # Load image in grayscale mode
    img = Image.open(image_path).convert('L')
    img = invert_image(img)
    # Resize to 28x28
    img = img.resize((28, 28))
    # Convert to numpy array
    img = np.array(img)
    return img

def preprocess_image(image):
    img = image.convert('L')
    img = invert_image(img)
    img = img.resize((28, 28))
    img = np.array(img)
    return img


def predict_character(image):
    with open('first_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Preprocess the input image
    image = image.reshape(1, 28, 28, 1)
    image = image / 255.0

    # Predict the character
    prediction = model.predict(image)
    character = chr(np.argmax(prediction) + 65)  # Convert to corresponding character

    return character

