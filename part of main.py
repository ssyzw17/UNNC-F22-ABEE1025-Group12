Author: Ziyu Wang   Su Li
Date: 2023.1.27


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
                # That is what Ziyu Wang wrote
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
