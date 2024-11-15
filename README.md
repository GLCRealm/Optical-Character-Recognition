
# Optical Character Recognition (OCR) Application

This repository contains an interactive OCR application built with Python, Tesseract OCR, and a custom-trained deep learning model. The application provides a GUI for users to upload images and extract text.

## Features
- **Interactive GUI**: Built using `customtkinter` for a modern, user-friendly interface.
- **OCR Capabilities**: Extracts and recognizes characters from images, handling spaces and line breaks effectively.
- **Custom Preprocessing**: Enhances OCR accuracy with advanced image processing techniques.
- **Deep Learning Integration**: Utilizes a trained neural network for character recognition (`first_model.pkl`).

## File Structure
- `compleat.py`: Main application script with the GUI implementation.
- `ocr6.py`: Backend for OCR tasks, including text extraction and character segmentation.
- `firstuse.py`: Contains helper functions for image preprocessing and character prediction.
- `first_model.pkl`: Serialized file of the trained neural network used for character recognition.
- `requirements.txt`: List of required Python dependencies.

## Requirements
- Python 3.x
- Tesseract OCR
- Required Python libraries: `numpy`, `Pillow`, `customtkinter`, `pytesseract`, `tensorflow`, `pickle`.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/GLCRealm/Optical-Character-Recognition.git
   cd Optical-Character-Recognition
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up Tesseract OCR by downloading and installing it. Update its path in `ocr6.py`:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'path_to_tesseract'
   ```

## Usage
1. Start the application:
   ```bash
   python compleat.py
   ```
2. Use the GUI to:
   - Import an image.
   - Click "Predict" to extract text and display it in the text box.
   - Clear the display with the "Cancel" button.

## Model Information
The file `first_model.pkl` contains a trained neural network:
- **Input**: Preprocessed character images resized to 28x28 pixels.
- **Output**: Predicted English capital letters (A-Z).
- **Framework**: Built and saved using TensorFlow/Keras.

## How It Works
1. **Preprocessing**: Images are processed to enhance visibility using thresholding, inversion, and resizing.
2. **Segmentation**: Characters are isolated using bounding boxes.
3. **Prediction**: Segmented characters are predicted using the trained model in `first_model.pkl`.

## Example
### Input:
An image containing handwritten or printed text.

### Output:
Recognized text displayed in the GUI text box.

## Contributing
Contributions are welcome! Fork the repository and submit pull requests for new features or bug fixes.

## License
This project is licensed under the MIT License.
