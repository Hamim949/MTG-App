from PyQt6.QtWidgets import (QApplication, QVBoxLayout, QWidget, 
                             QLabel, QHBoxLayout, QLineEdit, 
                            QPushButton, QTextEdit)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys
import controller
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 400)
        self.setWindowTitle("MTG Guide")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.UI()
    
    def UI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

    # Create the Widget # 
        title_label = QLabel("MTG Guide")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont("Consolas", 22))

        description = "Search the MTG Guide by Catagory"
        description_label = QLabel(description)
        description_label.setFont(QFont("Consolas", 14))

        search_layout = QHBoxLayout()
        self.search_field = QLineEdit()
        self.search_field.setFont(QFont("Consolas", 12))


        search_button = QPushButton("Search")
        search_button.setFont(QFont("Consolas", 12))
        search_button.clicked.connect(self.search)

        search_layout.addWidget(self.search_field)
        search_layout.addWidget(search_button)

        self.results_text = QTextEdit("Results.")
        self.results_text.setFont(QFont("Consolas", 12))

        layout.addWidget(title_label)
        layout.addWidget(description_label)
        layout.addLayout(search_layout)
        layout.addWidget(self.results_text)
    
    def search(self):
        # get user input 
        query = self.search_field.text()
        self.results_text.setText("Searching...")

        # make API call 
        results = controller.make_call(query)

        # display results
        self.results_text.setText(results)



def main(): 
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

card_types = {
"types": [
"Artifact",
"Conspiracy",
"Creature",
"Dragon",
"Elemental",
"Enchantment",
"Goblin",
"Hero",
"instant",
"Instant",
"Jaguar",
"Knights",
"Land",
"Phenomenon",
"Plane",
"Planeswalker",
"Scheme",
"Sorcery",
"Stickers",
"Summon",
"Tribal",
"Universewalker",
"Vanguard",
"Wolf"
]
}
