import sys

from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout, QLabel


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Temperature Converter")

        # Create widgets
        self.c_label = QLabel("Temperature in C")
        self.c_edit = QLineEdit()
        self.button_c_to_f = QPushButton("Convert C to F")
        self.c_result = QLabel(f"Result:")
        self.f_label = QLabel("Temperature in F")
        self.f_edit = QLineEdit()
        self.button_f_to_c = QPushButton("Convert F to C")
        self.f_result = QLabel(f"Result:")

        # Create layout and add widgets
        layout = QVBoxLayout(self)
        for element in [self.c_label, self.c_edit, self.button_c_to_f, self.c_result,
                        self.f_label, self.f_edit, self.button_f_to_c, self.f_result]:
            layout.addWidget(element)

        # Set dialog layout
        self.setLayout(layout)

        # Add button signal to convert slot
        self.button_c_to_f.clicked.connect(self.c_to_f)
        self.button_f_to_c.clicked.connect(self.f_to_c)

    # Converts from C to F
    def c_to_f(self):
        temp_c = (float(self.c_edit.text()) * 9 / 5) + 32
        self.c_result.setText(f"Result: {round(float(temp_c), 3)} F")

    # Converts from F to C
    def f_to_c(self):
        temp_f = (float(self.f_edit.text()) - 32) * 5 / 9
        self.f_result.setText(f"Result: {round(float(temp_f), 2)} C")


if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
