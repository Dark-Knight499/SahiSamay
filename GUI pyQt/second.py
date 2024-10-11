import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QPushButton, QLabel, QVBoxLayout, QWidget, QTabWidget,
    QListView, QDialog, QDialogButtonBox, QCheckBox, QGroupBox, QTableWidget,
    QTableWidgetItem, QMessageBox
)
from PyQt5.QtCore import Qt, QStringListModel
from PyQt5.QtGui import QColor
import register
from person import Person

class SharedState:
    selected_persons = []

def analyze_schedule(selected_persons):
    if not selected_persons:
        return []

    num_days = 7
    num_slots = 20
    result_timetable = [[0] * num_slots for _ in range(num_days)]

    for person in selected_persons:
        for day_index, day_timetable in enumerate(person.timetable):
            for slot_index, slot in enumerate(day_timetable):
                if slot == "0":
                    result_timetable[day_index][slot_index] += 1
    return result_timetable

def update_table(timetable, table_widget):
    table_widget.setRowCount(len(timetable))
    table_widget.setColumnCount(len(timetable[0]))

    for i, day in enumerate(timetable):
        for j, count in enumerate(day):
            item = QTableWidgetItem(str(count))
            table_widget.setItem(i, j, item)
            # Set color intensity based on the count
            color_value = int((count / len(SharedState.selected_persons)) * 255)
            item.setBackground(QColor(color_value, 255 - color_value, 0))  # Corrected usage

class PersonSelectionWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Persons")
        self.setGeometry(100, 100, 300, 400)

        self.layout = QVBoxLayout(self)
        self.checkbox_groups = {}
        self.checkboxes = []

        # Group checkboxes by department
        self.departments = ["Coding", "Elex", "Mech"]
        self.dept_checkboxes = {}

        for dept in self.departments:
            group_box = QGroupBox(dept)
            self.checkbox_groups[dept] = group_box
            layout = QVBoxLayout()
            for person in Person.person_list:
                if person.dept == dept:
                    checkbox = QCheckBox(person.name)
                    checkbox.stateChanged.connect(self.on_checkbox_state_changed)
                    layout.addWidget(checkbox)
                    self.checkboxes.append(checkbox)
            group_box.setLayout(layout)
            self.layout.addWidget(group_box)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

    def on_checkbox_state_changed(self, state):
        source = self.sender()
        person_name = source.text()
        person = next((p for p in Person.person_list if p.name == person_name), None)
        if person:
            if source.isChecked():
                if person not in SharedState.selected_persons:
                    SharedState.selected_persons.append(person)
            else:
                if person in SharedState.selected_persons:
                    SharedState.selected_persons.remove(person)

    def get_selected_persons(self):
        return SharedState.selected_persons

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1600, 750)
        self.setWindowTitle('PyQt5 Tab and Sidebar Example')

        self.tab_view = QTabWidget(self)
        self.tab_view.setGeometry(0, 0, 1100, 700)

        self.tab1 = QWidget()
        self.tab1.setStyleSheet("background-color: lightgrey;")
        self.tab_view.addTab(self.tab1, "Tab 1")

        self.tab2 = QWidget()
        self.tab2.setStyleSheet("background-color: lightblue;")
        self.tab_view.addTab(self.tab2, "Tab 2")

        self.table_widget = QTableWidget(self.tab1)
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(self.table_widget)
        self.tab1.setLayout(tab1_layout)

        self.addBar = QWidget(self)
        self.addBar.setGeometry(1100, 25, 500, 675)
        self.addBar.setStyleSheet("background-color: white;")

        self.addBarLayout = QVBoxLayout()
        self.addBarLayout.setContentsMargins(10, 10, 10, 10)
        self.addBar.setLayout(self.addBarLayout)

        self.addPersonLabel = QLabel("Add Person", self.addBar)
        self.addPersonLabel.setStyleSheet("font-weight: bold; font-size: 24px;")
        self.addBarLayout.addWidget(self.addPersonLabel, alignment=Qt.AlignTop)

        self.person_list_view = QListView(self.addBar)
        self.model = QStringListModel()
        self.person_list_view.setModel(self.model)
        self.person_list_view.setEditTriggers(QListView.NoEditTriggers)
        self.person_list_view.setFixedSize(480, 500)
        self.addBarLayout.addWidget(self.person_list_view, alignment=Qt.AlignCenter)

        self.addButton = QPushButton("Add Person", self.addBar)
        self.addBarLayout.addWidget(self.addButton, alignment=Qt.AlignBottom)
        self.addButton.clicked.connect(self.open_person_selection_dialog)

        self.analyzeButton = QPushButton("Analyze", self.addBar)
        self.addBarLayout.addWidget(self.analyzeButton, alignment=Qt.AlignBottom)
        self.analyzeButton.clicked.connect(self.analyze_button_clicked)

        self.registerButton = QPushButton("Register", self.addBar)
        self.addBarLayout.addWidget(self.registerButton, alignment=Qt.AlignBottom)
        self.registerButton.clicked.connect(self.register_button_clicked)

    def open_person_selection_dialog(self):
        SharedState.selected_persons.clear()
        self.model.setStringList([])

        selection_window = PersonSelectionWindow(self)
        
        if selection_window.exec_() == QDialog.Accepted:
            self.update_list_view()  # Update with new selected items

    def update_list_view(self):
        selected_names = [person.name for person in SharedState.selected_persons]
        self.model.setStringList(selected_names)

    def analyze_button_clicked(self):
        if not SharedState.selected_persons:
            QMessageBox.warning(self, "No Selection", "Please select persons to analyze.")
            return
        common_timetable = analyze_schedule(SharedState.selected_persons)
        update_table(common_timetable, self.table_widget)

    def register_button_clicked(self):
        register.main()
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
