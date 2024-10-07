# QR Code Generator & Reader Application

This is a PyQt6-based desktop application that allows users to **generate** and **read** QR codes. The application provides a user-friendly interface with options to customize QR code versions and error correction levels. It also supports reading QR codes from images and extracting the embedded information.

## Features

### 1. **QR Code Generation**
- **Input Field:** Enter the text you want to encode into the QR code.
- **Version Selection:** Choose the QR version (1-40), where higher versions allow more data to be stored in the QR code.
- **Error Correction Level:** Choose the error correction level (L, M, Q, H) to determine how much redundancy is embedded in the QR code. This affects how much of the QR code can be damaged and still be readable:
  - **L:** 7% of the code can be restored.
  - **M:** 15% of the code can be restored.
  - **Q:** 25% of the code can be restored.
  - **H:** 30% of the code can be restored.
- **QR Display:** The generated QR code is displayed in the application window.
- **Save Functionality:** Once generated, the QR code can be saved as a PNG file.

### 2. **QR Code Reading**
- **Open QR Code Image:** Read and decode the information from an existing QR code by opening an image (PNG, JPG, BMP).
- **Result Display:** The decoded data from the QR code is displayed in the application.

### 3. **Theming**
- The application uses a **dark theme** (with a teal accent) provided by the `qt_material` library.

---

## Installation

To run this application, you need to install the necessary dependencies. Follow the steps below to set up your environment.

### Prerequisites

Ensure you have Python installed. You can download Python from [here](https://www.python.org/downloads/).

### Required Libraries

Install the required libraries using `pip`. Run the following commands:

```bash
pip install pyqt6 qt_material qrcode pyzbar pillow opencv-python
```

### Clone the Repository

You can clone the repository (or create the Python file) using:

```bash
git clone <repository-link>
```

Alternatively, create a Python file (`qr_code_app.py`) with the code provided above.

---

## Running the Application

Once you have installed the dependencies and set up the Python file, run the following command in your terminal:

```bash
python main.py
```

The application window should open, allowing you to generate and read QR codes.

---

## How to Use

### **Generating QR Codes**
1. **Enter Text:** Type the text you want to encode into a QR code in the text field.
2. **Select Version and Error Correction:**
   - Choose the desired QR version from the dropdown menu. Versions range from 1 to 40, with higher versions capable of storing more data.
   - Select the error correction level to determine how much damage the QR code can withstand while still being readable.
3. **Click 'Generate':** Press the "Generate" button to create the QR code.
4. **Save QR Code:** Once generated, you can save the QR code as a PNG file by clicking the "Save" button.

### **Reading QR Codes**
1. **Click 'Read QR Code':** Press the "Read QR Code" button to select an image file (PNG, JPG, BMP) containing a QR code.
2. **Open Image:** Choose the image file from your system’s file explorer.
3. **View Decoded Data:** If a QR code is found in the image, the decoded text will be displayed at the bottom of the application. If no QR code is detected, you will be notified.

---

## File Structure

The application consists of a single Python file containing the following components:

- **QRCodeApp Class:** Handles both QR generation and reading functions.
- **UI Components:**
  - **QLineEdit:** Input field for the text to generate the QR code.
  - **QComboBox:** Dropdowns to select QR version and error correction level.
  - **QPushButton:** Buttons for generating, saving, and reading QR codes.
  - **QLabel:** Displays the generated QR code and the decoded result.

---

## Dependencies Breakdown

- **PyQt6:** Provides the GUI components for building the application window.
- **qt_material:** Adds a stylish material design theme to the application.
- **qrcode:** Generates the QR codes from the input text.
- **pyzbar:** Decodes the QR codes from images.
- **Pillow:** Used to handle image processing.
- **opencv-python (cv2):** Reads the QR code images for decoding.

---

## Customization

### Changing the Theme
You can change the theme of the application by modifying the theme file in the `apply_stylesheet` method. For example:

```python
apply_stylesheet(app, theme='dark_teal.xml')
```

To view available themes, refer to the [qt-material documentation](https://github.com/UN-GCPDS/qt-material).

### Adding More Features
Feel free to extend the functionality by adding more options, such as:
- Custom QR code colors.
- QR code image size adjustments.
- Support for different image formats when reading QR codes.

---

## Known Issues

- If no QR code is found in an image, the application will display "No QR code found." Ensure the QR code is clearly visible and properly scanned in the image.
- The error correction levels might not make a noticeable difference unless the QR code is physically damaged or altered.

---

## Future Enhancements

- **Batch QR Code Reading:** Implement the ability to read QR codes from multiple images at once.
- **Export Formats:** Add more options for saving QR codes, such as SVG, JPEG, or BMP.
- **Customization Panel:** Allow users to choose colors for the QR code or even embed logos in the center of the code.
- **Drag & Drop:** Enable users to drag and drop images into the app window for reading.

---

## Contributing

We welcome contributions to enhance the functionality of the application. Feel free to submit pull requests or open issues for bugs and suggestions.

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/my-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Open a pull request.

---

## License

This project is licensed under the MIT License. Feel free to modify and use it for personal or commercial projects.

---

## Credits

- Developed by **[1999azzar]**
- Powered by PyQt6, qrcode, pyzbar, and OpenCV.

