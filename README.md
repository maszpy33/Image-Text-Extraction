# Image Text Extraction

Image Text Extraction is a project aimed at extracting text from images using optical character recognition (OCR) techniques. It provides a simple and straightforward way to process images containing textual information and convert that text into machine-readable format.

## Features

- Extract text from images: The project utilizes OCR algorithms to extract text from images and convert it into digital text.
- Multiple image formats supported: Images in common formats like JPEG, PNG, and GIF can be processed for text extraction.
- Preprocessing capabilities: The project includes preprocessing techniques to enhance the image quality and improve OCR accuracy.
- Command-line interface (CLI): An easy-to-use CLI is provided for running the text extraction process on the command line.
- Text output options: Extracted text can be saved to a text file for further analysis or processing.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/maszpy33/Image-Text-Extraction.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Navigate to the project directory:

   ```bash
   cd Image-Text-Extraction
   ```

2. Run the CLI to extract text from an image:

   ```bash
   python extract_text.py --image <path_to_image>
   ```

   Replace `<path_to_image>` with the path to the image file you want to process.

3. The extracted text will be displayed in the console and saved to a text file named `output.txt`.

## License

This project is licensed under the [MIT License](LICENSE).
