from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QLineEdit,
    QMainWindow
)

from PyQt6.QtCore import QThread, pyqtSignal, Qt

from .vision import analyze_screen

class Worker(QThread):

    finished = pyqtSignal(str)

    def __init__(self, prompt):
        super().__init__()
        self.prompt = prompt

    def run(self):
        result = analyze_screen(self.prompt)
        self.finished.emit(result)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rajora AI Desktop Assistant")
        self.setGeometry(300, 200, 700, 500)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        title = QLabel("Rajora AI Desktop Assistant")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        command_label = QLabel("Command")
        self.command_input = QLineEdit()
        self.command_input.setPlaceholderText(
            "Describe everything visible on my screen..."
        )
        self.analyze_button = QPushButton("Analyze Screen")
        output_label = QLabel("Output")
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        self.output_box.setText("Waiting for input...")
        self.status_label = QLabel("Status : Ready")

        layout.addWidget(title)

        layout.addWidget(command_label)

        layout.addWidget(self.command_input)

        layout.addWidget(self.analyze_button)

        layout.addWidget(output_label)

        layout.addWidget(self.output_box)

        layout.addWidget(self.status_label)
        self.analyze_button.clicked.connect(self.start_analysis)
    

    def start_analysis(self):
        prompt = self.command_input.text().strip()

        if not prompt:
            prompt = "Describe everything visible on my screen."

        self.output_box.setText("Analyzing screen... Please wait.")

        self.status_label.setText("Status : Analyzing...")

        self.analyze_button.setEnabled(False)

        self.worker = Worker(prompt)

        self.worker.finished.connect(self.display_result)

        self.worker.start()
    

    def display_result(self, result):
        self.output_box.setText(result)

        self.status_label.setText("Status : Ready")

        self.analyze_button.setEnabled(True)
