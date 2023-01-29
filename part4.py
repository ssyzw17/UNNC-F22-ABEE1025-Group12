Author: Ziyu Wang   Su Li
Date: 2023.1.27

import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QWidget
from PyQt6 import QtCore, QtWidgets


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

    def menu_triggered(self, q):
        if q.text() == "Wall":
            # clear menu0
            self.menu0.clear()
            self.menu0.addAction('Reinforced concrete')
            self.menu0.addAction('Cement mortar')
            self.menu0.addAction('The lime mortar')
            self.menu0.addAction('Lime plaster mortar')
            self.menu0.addAction(
                'Polystyrene board (including wire rack of polystyrene)')
            self.menu0.addAction('Polyurethane (pu)')
            self.menu0.addAction('Slag brick masonry')
            self.menu0.addAction('Foam glass')
            self.menu0.addAction('Boiler slag')
            self.menu0.addAction('The blast furnace slag')
            self.menu0.addAction('The fly ash')
            self.menu0.addAction('Solid clay')
            self.menu0.addAction('Light clay')
            self.menu0.addAction('Granite')
            self.menu0.addAction('The marble')
            self.menu0.addAction('Flat glass')
            self.menu0.triggered.connect(self.menu0_triggered)
        elif q.text() == "Roof":
            # clear menu0
            self.menu0.clear()
            self.menu0.addAction('Reinforced concrete')
            self.menu0.addAction('Cement mortar')
            self.menu0.addAction('The lime mortar')
            self.menu0.addAction('Lime plaster mortar')
            self.menu0.addAction(
                'Polystyrene board (including wire rack of polystyrene)')
            self.menu0.addAction('Polyurethane (pu)')
            self.menu0.addAction('Slag brick masonry')
            self.menu0.addAction('Foam glass')
            self.menu0.addAction('Boiler slag')
            self.menu0.addAction('The blast furnace slag')
            self.menu0.addAction('The fly ash')
            self.menu0.addAction('Solid clay')
            self.menu0.addAction('Light clay')
            self.menu0.addAction('Granite')
            self.menu0.addAction('The marble')
            self.menu0.addAction('Flat glass')
            self.menu0.triggered.connect(self.menu0_triggered)
        elif q.text() == "Floor":
            # clear menu0
            self.menu0.clear()
            self.menu0.addAction('Reinforced concrete')
            self.menu0.addAction('Cement mortar')
            self.menu0.addAction('The lime mortar')
            self.menu0.addAction('Lime plaster mortar')
            self.menu0.addAction(
                'Polystyrene board (including wire rack of polystyrene)')
            self.menu0.addAction('Polyurethane (pu)')
            self.menu0.addAction('Slag brick masonry')
            self.menu0.addAction('Foam glass')
            self.menu0.addAction('Boiler slag')
            self.menu0.addAction('The blast furnace slag')
            self.menu0.addAction('The fly ash')
            self.menu0.addAction('Solid clay')
            self.menu0.addAction('Light clay')
            self.menu0.addAction('Granite')
            self.menu0.addAction('The marble')
            self.menu0.addAction('Flat glass')
            self.menu0.triggered.connect(self.menu0_triggered)
        elif q.text() == "Door":
            self.menu0.clear()
            self.menu0.addAction('Fibreboard')
            # Oak material
            self.menu0.addAction('Oak material')
            # corkboard
            self.menu0.addAction('Corkboard')
            # particle board
            self.menu0.addAction('Particle board')
            self.menu0.triggered.connect(self.menu0_triggered)
        elif q.text() == "Window":
            self.menu0.clear()
            # plain glass
            self.menu0.addAction('Plain glass')
            # glass fiber reinforced plastics
            self.menu0.addAction('Glass fiber reinforced plastics')
            self.menu0.triggered.connect(self.menu0_triggered)

    def menu0_triggered(self, q):
        self.material = q.text()

    def button0_clicked(self):
        if self.material == None:
            a1 = "Error"
            a2 = "Please select material."
            QMessageBox.about(self, a1, a2)
        elif self.lineedit0_0.text() == "":
            a3 = "Error"
            a4 = "Please enter d(m)."
            QMessageBox.about(self, a3, a4)
        else:
            if self.material == "Reinforced concrete":
                r = float(self.lineedit0_0.text()) / 1.74
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            elif self.material == "Cement mortar":
                r = float(self.lineedit0_0.text()) / 0.93
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            elif self.material == "The lime mortar":
                r = float(self.lineedit0_0.text())/0.81
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            elif self.material == "Lime plaster mortar":
                r = float(self.lineedit0_0.text()) / 0.76
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            elif self.material == "Polystyrene board (including wire rack of polystyrene)":
                r = float(self.lineedit0_0.text()) / 0.041
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            elif self.material == "Polyurethane (pu)":
                r = float(self.lineedit0_0.text()) / 0.024
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            elif self.material == "Slag brick masonry":
                r = float(self.lineedit0_0.text()) / 0.87
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            elif self.material == "Foam glass":
                r = float(self.lineedit0_0.text()) / 0.058
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            elif self.material == "Boiler slag":
                r = float(self.lineedit0_0.text()) / 0.29
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            elif self.material == "The blast furnace slag":
                r = float(self.lineedit0_0.text()) / 0.26
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            elif self.material == "The fly ash":
                r = float(self.lineedit0_0.text()) / 0.23
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            elif self.material == "Solid clay":
                r = float(self.lineedit0_0.text()) / 1.16
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            elif self.material == "Light clay":
                r = float(self.lineedit0_0.text()) / 0.47
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            elif self.material == "Granite":
                r = float(self.lineedit0_0.text()) / 3.49
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            elif self.material == "The marble":
                r = float(self.lineedit0_0.text()) / 2.72
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            elif self.material == "Flat glass":
                r = float(self.lineedit0_0.text()) / 0.76
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            # fibreboard 0.34
            elif self.material == "Fibreboard":
                r = float(self.lineedit0_0.text()) / 0.34
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            # Oak material 0.17
            elif self.material == "Oak material":
                r = float(self.lineedit0_0.text()) / 0.17
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            # corkboard 0.093
            elif self.material == "Corkboard":
                r = float(self.lineedit0_0.text()) / 0.093
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            # particle board 0.065
            elif self.material == "Particle board":
                r = float(self.lineedit0_0.text()) / 0.065
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            # plain glass 0.76
            elif self.material == "Plain glass":
                r = float(self.lineedit0_0.text()) / 0.76
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()
            # glass fiber reinforced plastics 0.52
            elif self.material == "Glass fiber reinforced plastics":
                r = float(self.lineedit0_0.text()) / 0.52
                u = 1 / r
                self.textbrowser0_0.setText("u = " + str(u))
                sql = sqlite3.connect("data.db")
                cur = sql.cursor()
                # create
                cur.execute("CREATE TABLE IF NOT EXISTS data (material, d, u)")
                # insert
                cur.execute("INSERT INTO data VALUES (?, ?, ?)", (self.material,
                            self.lineedit0_0.text(), str(u)))
                sql.commit()
                sql.close()


app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec())
