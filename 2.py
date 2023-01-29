Author: Ziyu Wang
Date: 2023.1.27

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # title
        self.setWindowTitle("My App")
        # size
        self.setFixedSize(800, 600)
        self.structure = None
        self.material = None
        # menu
        self.menu = self.menuBar().addMenu("Structure")
        self.menu.addAction("Wall")
        self.menu.addAction("Roof")
        self.menu.addAction("Floor")
        # door
        self.menu.addAction("Door")
        # window
        self.menu.addAction("Window")
        # menu trigger
        self.menu.triggered.connect(self.menu_triggered)
        self.menu0 = self.menuBar().addMenu("Material")
        self.main0 = QWidget()
        self.main0.setFixedSize(800, 600)
        self.setCentralWidget(self.main0)
        self.layout0()
        self.layout1()
        self.label0()
        self.lineedit0()
        self.button0()
        self.textbrowser0()
    # layout

    def layout0(self):
        self.layout0_0 = QtWidgets.QVBoxLayout()
        self.main0.setLayout(self.layout0_0)

    def layout1(self):
        self.layout1_0 = QtWidgets.QHBoxLayout()
        self.layout0_0.addLayout(self.layout1_0)
        self.layout1_1 = QtWidgets.QHBoxLayout()
        self.layout0_0.addLayout(self.layout1_1)
    # label

    def label0(self):
        self.label0_0 = QLabel()
        self.label0_0.setText("Please enter d(m):")
        # label style
        self.label0_0.setStyleSheet("font-size: 16px; margin-left: 50%;")
        self.layout1_0.addWidget(self.label0_0)
    # lineedit

    def lineedit0(self):
        self.lineedit0_0 = QtWidgets.QLineEdit()
        self.lineedit0_0.setPlaceholderText("d(m)")
        # lineedit style
        self.lineedit0_0.setStyleSheet("font-size: 18px;")
        self.lineedit0_0.setFixedSize(300, 36)
        self.layout1_0.addWidget(self.lineedit0_0)
        self.layout1_0.addStretch()
    # button

    def button0(self):
        self.button0_0 = QtWidgets.QPushButton()
        self.button0_0.setText("Calculate")
        # button style
        self.button0_0.setStyleSheet(
            "font-size: 18px; font-weight: bold;")
        self.button0_0.setFixedSize(120, 50)
        self.button0_0.clicked.connect(self.button0_clicked)
        self.layout1_0.addWidget(self.button0_0)
        self.layout1_0.addStretch()
    # textbrowser

    def textbrowser0(self):
        self.textbrowser0_0 = QtWidgets.QTextBrowser()
        # textbrowser style
        self.textbrowser0_0.setStyleSheet(
            "font-size: 18px; text-align: center;")
        self.textbrowser0_0.setFixedSize(700, 300)
        # center
        self.textbrowser0_0.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.textbrowser0_0.setPlaceholderText("Result")
        self.textbrowser0_0.setReadOnly(True)
        self.textbrowser0_0.setText("Result")
        self.layout1_1.addStretch()
        self.layout1_1.addWidget(self.textbrowser0_0)
        self.layout1_1.addStretch()

