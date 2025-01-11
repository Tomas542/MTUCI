import psycopg2
import sys

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox,
                         QTableWidgetItem, QPushButton, QMessageBox)




class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()

        self.setWindowTitle("Shedule")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self._shedule_forms()
        self._create_addT_tab()
        self._create_addSubject_tab()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="schedular_db",
                                     user="postgres",
                                     password='1',
                                     host="localhost",
                                     port="5432")

        self.cursor = self.conn.cursor()

    def _create_addT_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "AddT")

        self.addT_gbox = QGroupBox('AddT')

        self.svbox = QVBoxLayout()
        self.shbox2 = QHBoxLayout()

        self.svbox.addLayout(self.shbox2)

        self.shbox2.addWidget(self.addT_gbox)

        self._create_addT_table()

        self.shedule_tab.setLayout(self.svbox)

    def _create_addSubject_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "AddSub")

        self.addSub_gbox = QGroupBox('AddSub')
        self.Subjects_gbox = QGroupBox('Subjects')

        self.svbox = QVBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.shbox3 = QHBoxLayout()

        self.svbox.addLayout(self.shbox2)
        self.svbox.addLayout(self.shbox3)

        self.shbox2.addWidget(self.addSub_gbox)
        self.shbox2.addWidget(self.Subjects_gbox)

        self._create_addSub_table()

        self.update_shedule_button = QPushButton("Update")
        self.shbox3.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.shedule_tab.setLayout(self.svbox)



    def _shedule_forms(self):
        self.monday1_gbox = QGroupBox("Monday nechet")
        self.monday2_gbox = QGroupBox('Monday chet')
        self.monday1_table = QTableWidget()
        self.monday2_table = QTableWidget()
        self._create_shedule_tab(self.monday1_gbox, self.monday2_gbox, self.monday1_table, self.monday2_table, 'Понедельник')

        self.tue1_gbox = QGroupBox("Tuesday nechet")
        self.tue2_gbox = QGroupBox('Tuesday chet')
        self.tue1_table = QTableWidget()
        self.tue2_table = QTableWidget()
        self._create_shedule_tab(self.tue1_gbox, self.tue2_gbox, self.tue1_table, self.tue2_table, 'Вторник')

        self.wed1_gbox = QGroupBox("Wednesday nechet")
        self.wed2_gbox = QGroupBox('Wednesday chet')
        self.wed1_table = QTableWidget()
        self.wed2_table = QTableWidget()
        self._create_shedule_tab(self.wed1_gbox, self.wed2_gbox, self.wed1_table, self.wed2_table, 'Среда')

        self.thu1_gbox = QGroupBox("Thusday nechet")
        self.thu2_gbox = QGroupBox('Thusday chet')
        self.thu1_table = QTableWidget()
        self.thu2_table = QTableWidget()
        self._create_shedule_tab(self.thu1_gbox, self.thu2_gbox, self.thu1_table, self.thu2_table, 'Четверг')

        self.fri1_gbox = QGroupBox("Friday nechet")
        self.fri2_gbox = QGroupBox('Friday chet')
        self.fri1_table = QTableWidget()
        self.fri2_table = QTableWidget()
        self._create_shedule_tab(self.fri1_gbox, self.fri2_gbox, self.fri1_table, self.fri2_table, 'Пятница')




    def _create_shedule_tab(self, gbox1, gbox2, table1, table2, weekDay):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, weekDay)


        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)

        self.shbox1.addWidget(gbox1)
        self.shbox1.addWidget(gbox2)


        self._create_table(table1, gbox1, False, weekDay)
        self._create_table(table2, gbox2, True, weekDay)

        self.update_shedule_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(lambda: self._update_shedule(weekDay))

        self.refresh_button = QPushButton("Rewrite")
        self.shbox2.addWidget(self.refresh_button)
        self.refresh_button.clicked.connect(lambda: self.refresh(weekDay))

        self.shedule_tab.setLayout(self.svbox)

    def _create_table(self, table, box, chet, weekDay):

        table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(['ID',"Subject", "Time", "Room", ""])


        self._update_table(table, chet, weekDay)

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(table)
        box.setLayout(self.mvbox)

    def _update_table(self, table, chet, weekDay):
        self.cursor.execute('SELECT * FROM timetable WHERE day = %s AND chet = %s;', (weekDay, chet))
        records = list(self.cursor.fetchall())
        table.setRowCount(len(records))
        for i, r in enumerate(records):
            r = list(r)
            table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            table.setItem(i, 1, QTableWidgetItem(str(r[2])))
            table.setItem(i, 2, QTableWidgetItem(str(r[4])))
            table.setItem(i, 3, QTableWidgetItem(str(r[3])))


        table.resizeRowsToContents()


    def refresh(self, weekDay):
        if weekDay == 'Понедельник':
            self._change_day_from_table(self.monday1_table)
            self._change_day_from_table(self.monday2_table)
        elif weekDay == 'Вторник':
            self._change_day_from_table(self.tue1_table)
            self._change_day_from_table(self.tue2_table)
        elif weekDay == 'Среда':
            self._change_day_from_table(self.wed1_table)
            self._change_day_from_table(self.wed2_table)
        elif weekDay == 'Четверг':
            self._change_day_from_table(self.thu1_table)
            self._change_day_from_table(self.thu2_table)
        elif weekDay == 'Пятница':
            self._change_day_from_table(self.fri1_table)
            self._change_day_from_table(self.fri2_table)

    def _change_day_from_table(self, table):
        row = list()
        for rowNum in range(table.rowCount()):

            for i in range(table.columnCount()):
                try:
                    row.append(table.item(rowNum, i).text())
                except:
                    row.append(None)
            try:
                self.cursor.execute('UPDATE timetable SET subject = %s, start_time = %s, room_numb = %s WHERE id = %s;', (row[1], row[2], row[3], row[0]))
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Enter all fields")
            row.clear()

    def _update_shedule(self, weekDay):
        self._add_fields_ToSub()

        if weekDay == 'Понедельник':
            self._update_table(self.monday1_table, False, 'Понедельник')
            self._update_table(self.monday2_table, True, 'Понедельник')

        elif weekDay == 'Вторник':
            self._update_table(self.tue1_table, False, 'Вторник')
            self._update_table(self.tue2_table, True, 'Вторник')

        elif weekDay == 'Среда':
            self._update_table(self.wed1_table, False, 'Среда')
            self._update_table(self.wed2_table, True, 'Среда')

        elif weekDay == 'Четверг':
            self._update_table(self.thu1_table, False, 'Четверг')
            self._update_table(self.thu2_table, True, 'Четверг')

        elif weekDay == 'Пятница':
            self._update_table(self.fri1_table, False, 'Пятница')
            self._update_table(self.fri2_table, True, 'Пятница')





    def _create_addT_table(self):
        self.addT_table = QTableWidget()
        self.addT_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.addT_table.setColumnCount(6)
        self.addT_table.setHorizontalHeaderLabels(['Day', "Subject", 'Room', "Time", 'Chet'])
        self.addT_table.setRowCount(1)

        self._add_fields_ToT()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.addT_table)
        self.addT_gbox.setLayout(self.mvbox)

    def _add_fields_ToT(self):
        addButton = QPushButton('ADD')
        self.addT_table.setItem(0, 0, QTableWidgetItem(' '))
        self.addT_table.setItem(0, 1, QTableWidgetItem(' '))
        self.addT_table.setItem(0, 2, QTableWidgetItem(' '))
        self.addT_table.setItem(0, 3, QTableWidgetItem(' '))
        self.addT_table.setItem(0, 4, QTableWidgetItem(' '))

        self.addT_table.setCellWidget(0, 5, addButton)
        addButton.clicked.connect(lambda: self._update_addT_table())

    def _update_addT_table(self): # Добавляем в расписание
        row = list()

        for i in range(self.addT_table.columnCount()):
            try:
                row.append(self.addT_table.item(0, i).text())
            except:
                row.append(None)

        try:
            self.cursor.execute("INSERT INTO timetable (day, subject, room_numb, start_time, chet) VALUES (%s, %s, %s, %s, %s);", (row[0], row[1], row[2], row[3], row[4]))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

        self.addT_table.resizeRowsToContents()



    def _update_addSub_table(self): # Добавляем новый предмет
        try:
            self.cursor.execute('INSERT INTO subject (name) VALUES (%s)', (self.addSub_table.item(0, 0).text(),))
            self.conn.commit()
            self._add_fields_ToSub()
        except:
            QMessageBox.about(self, "Error", "This is bullshit")

    def _add_fields_ToSub(self):
        addButton = QPushButton('ADD')
        self.addSub_table.setItem(0, 0, QTableWidgetItem(' '))

        self.addSub_table.setCellWidget(0, 1, addButton)
        addButton.clicked.connect(lambda: self._update_addSub_table())

        self.cursor.execute('SELECT * FROM subject;')
        records = list(self.cursor.fetchall())
        self.Subjects_table.setRowCount(len(records))
        for i, r in enumerate(records):
            self.Subjects_table.setItem(i, 0, QTableWidgetItem(r[0]))

    def _create_addSub_table(self):
        self.addSub_table = QTableWidget()
        self.addSub_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.addSub_table.setColumnCount(2)
        self.addSub_table.setHorizontalHeaderLabels(['Subject', ''])
        self.addSub_table.setRowCount(1)

        self.Subjects_table = QTableWidget()
        self.Subjects_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.Subjects_table.setColumnCount(1)
        self.Subjects_table.setHorizontalHeaderLabels(['Subject'])
        self.Subjects_table.setRowCount(10)

        self._add_fields_ToSub()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.addSub_table)
        self.addSub_gbox.setLayout(self.mvbox)

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.Subjects_table)
        self.Subjects_gbox.setLayout(self.mvbox)
app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())