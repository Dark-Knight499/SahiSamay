import sys
from PyQt5.QtWidgets import QApplication, QDialog, QFormLayout, QLineEdit, QComboBox, QPushButton, QFileDialog, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

# Assuming you have a person module
import person

class PageDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Add Person")
        self.setFixedSize(400, 300)

        # Create form layout
        form_layout = QFormLayout()

        # Create form fields with styling
        self.name_line_edit = QLineEdit(self)
        self.department_combo_box = QComboBox(self)
        self.year_combo_box = QComboBox(self)
        self.file_location_label = QLabel("No file selected", self)
        self.file_location_button = QPushButton("Select File", self)

        # Populate department dropdown
        self.department_combo_box.addItems(["Mech", "Elex", "Marketing", "Coding"])
        
        # Populate year dropdown
        self.year_combo_box.addItems(["First", "Second", "Third", "Fourth"])

        # Connect file selection button to file dialog
        self.file_location_button.clicked.connect(self.select_file)

        # Add widgets to form layout
        form_layout.addRow("Name:", self.name_line_edit)
        form_layout.addRow("Department:", self.department_combo_box)
        form_layout.addRow("Year:", self.year_combo_box)
        form_layout.addRow("Location of TT File:", self.file_location_button)
        form_layout.addWidget(self.file_location_label)

        # Create buttons for dialog
        button_box = QVBoxLayout()
        self.ok_button = QPushButton("OK", self)
        self.cancel_button = QPushButton("Cancel", self)
        self.ok_button.clicked.connect(self.accept)  # Close the dialog with OK
        self.cancel_button.clicked.connect(self.reject)  # Close the dialog with Cancel
        button_box.addWidget(self.ok_button)
        button_box.addWidget(self.cancel_button)

        # Set up the dialog layout
        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addLayout(button_box)
        self.setLayout(layout)

        # Apply styles
        self.apply_styles()

    def apply_styles(self):
        # General dialog styling
        self.setStyleSheet("""
            QDialog {
                background-color: #f5f5f5;
                border: 1px solid #ccc;
                border-radius: 10px;
            }
        """)

        # Styling for QLineEdit
        self.name_line_edit.setStyleSheet("""
            QLineEdit {
                padding: 5px;
                border: 1px solid #aaa;
                border-radius: 5px;
            }
        """)

        # Styling for QComboBox
        self.department_combo_box.setStyleSheet("""
            QComboBox {
                padding: 5px;
                border: 1px solid #aaa;
                border-radius: 5px;
            }
        """)
        self.year_combo_box.setStyleSheet("""
            QComboBox {
                padding: 5px;
                border: 1px solid #aaa;
                border-radius: 5px;
            }
        """)

        # Styling for QPushButton
        self.file_location_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.ok_button.setStyleSheet("""
            QPushButton {
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        self.cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #dc3545;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
        """)

        # Styling for QLabel
        self.file_location_label.setStyleSheet("""
            QLabel {
                color: #333;
                margin-top: 10px;
            }
        """)

    def select_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select TT File", "", "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            self.file_location_label.setText(file_name)

def main():    
    # Create and show the dialog
    dialog = PageDialog()
    result = dialog.exec_()  # Execute the dialog modally
    
    if result == QDialog.Accepted:
        print("Dialog accepted")
        name = dialog.name_line_edit.text()
        department = dialog.department_combo_box.currentText()
        year = dialog.year_combo_box.currentText()
        file_location = dialog.file_location_label.text()

        # Assuming person module is available and correct
        try:
            p1 = person.Person()
            p1.name = name
            p1.dept = department
            p1.year = year
            p1.timetable = person.getTimeTable(file_location)
            print("Person object created and timetable set.")
        except Exception as e:
            print(f"Error with person module: {e}")

    print("Application finished")

if __name__ == '__main__':
    main()
