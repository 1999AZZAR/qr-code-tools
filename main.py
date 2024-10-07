import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
                             QLineEdit, QPushButton, QComboBox, QFileDialog, QFrame)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
import qrcode
from io import BytesIO
from qt_material import apply_stylesheet
from pyzbar.pyzbar import decode
from PIL import Image
import cv2

class QRCodeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QR Code Generator & Reader')
        self.setGeometry(100, 100, 400, 600)

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(25, 25, 25, 25)

        # Input field
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText('Enter text for QR code')
        self.input_field.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border-radius: 5px;
                background-color: #2b2b2b;
                color: white;
            }
            QLineEdit::placeholder {
                color: #8e8e8e;
            }
            QLineEdit:focus {
                border: 2px solid #26a69a;
            }
            QLineEdit::selection {
                background-color: #4caf50;
                color: white;
            }
        """)
        main_layout.addWidget(self.input_field)

        # Options layout
        options_layout = QHBoxLayout()
        options_layout.setSpacing(15)

        # QR Version selection
        version_layout = QVBoxLayout()
        version_label = QLabel('QR Version:')
        version_label.setStyleSheet("font-weight: bold;")
        version_layout.addWidget(version_label)
        self.version_combo = QComboBox()
        self.version_combo.addItems([str(i) for i in range(1, 41)])
        self.version_combo.setStyleSheet("padding: 6px; border-radius: 5px; background-color: #2b2b2b; color: white;")
        version_layout.addWidget(self.version_combo)
        options_layout.addLayout(version_layout)

        # Error correction level selection
        error_layout = QVBoxLayout()
        error_label = QLabel('Error Correction:')
        error_label.setStyleSheet("font-weight: bold;")
        error_layout.addWidget(error_label)
        self.error_combo = QComboBox()
        self.error_combo.addItems(['L', 'M', 'Q', 'H'])
        self.error_combo.setStyleSheet("padding: 6px; border-radius: 5px; background-color: #2b2b2b; color: white;")
        error_layout.addWidget(self.error_combo)
        options_layout.addLayout(error_layout)

        main_layout.addLayout(options_layout)

        # Buttons layout
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(15)

        # Generate button
        self.generate_button = QPushButton('Generate')
        self.generate_button.setIcon(QIcon.fromTheme("view-refresh"))
        self.generate_button.setStyleSheet("background-color: #26a69a; color: white; padding: 10px; border-radius: 5px;")
        self.generate_button.clicked.connect(self.generate_qr)
        buttons_layout.addWidget(self.generate_button)

        # Save button
        self.save_button = QPushButton('Save')
        self.save_button.setIcon(QIcon.fromTheme("document-save"))
        self.save_button.setStyleSheet("background-color: #00796b; color: white; padding: 10px; border-radius: 5px;")
        self.save_button.clicked.connect(self.save_qr)
        self.save_button.setEnabled(False)
        buttons_layout.addWidget(self.save_button)

        # Read button
        self.read_button = QPushButton('Read QR Code')
        self.read_button.setIcon(QIcon.fromTheme("folder-open"))
        self.read_button.setStyleSheet("background-color: #3f51b5; color: white; padding: 10px; border-radius: 5px;")
        self.read_button.clicked.connect(self.read_qr)
        buttons_layout.addWidget(self.read_button)

        main_layout.addLayout(buttons_layout)

        # QR Code display
        self.qr_frame = QFrame()
        self.qr_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.qr_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.qr_frame.setLineWidth(2)
        qr_layout = QVBoxLayout(self.qr_frame)
        self.qr_label = QLabel()
        self.qr_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.qr_label.setStyleSheet("border: 2px solid #4caf50; padding: 10px;")
        qr_layout.addWidget(self.qr_label)
        main_layout.addWidget(self.qr_frame)

        # Result label for read QR code
        self.result_label = QLabel('')
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

    def generate_qr(self):
        text = self.input_field.text()
        version = int(self.version_combo.currentText())
        error_correction = self.error_combo.currentText()

        # Generate QR code in black and white
        qr = qrcode.QRCode(version=version, error_correction=getattr(qrcode.constants, f'ERROR_CORRECT_{error_correction}'))
        qr.add_data(text)
        qr.make(fit=True)

        # Keep the default black and white color scheme for the QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Convert PIL image to QPixmap
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        qr_pixmap = QPixmap()
        qr_pixmap.loadFromData(buffer.getvalue())

        # Scale the QR code to fit the label
        scaled_pixmap = qr_pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio)
        self.qr_label.setPixmap(scaled_pixmap)

        # Enable save button
        self.save_button.setEnabled(True)

        # Store the QR image for saving later
        self.qr_image = img

    def save_qr(self):
        if hasattr(self, 'qr_image'):
            file_name, _ = QFileDialog.getSaveFileName(self, "Save QR Code", "", "PNG Files (*.png);;All Files (*)")
            if file_name:
                self.qr_image.save(file_name)

    def read_qr(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open QR Code Image", "", "Image Files (*.png *.jpg *.bmp);;All Files (*)")
        if file_name:
            img = cv2.imread(file_name)
            decoded_objects = decode(Image.open(file_name))
            if decoded_objects:
                for obj in decoded_objects:
                    self.result_label.setText(f"Decoded Data: {obj.data.decode('utf-8')}")
            else:
                self.result_label.setText("No QR code found.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    ex = QRCodeApp()
    ex.show()
    sys.exit(app.exec())
