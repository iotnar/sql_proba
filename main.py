# This Python file uses the following encoding: utf-8



import mysql.connector
from mydesign import Ui_MainWindow
import sys

from getpass import getpass
from mysql.connector import connect, Error
from PyQt5 import QtCore, QtGui, QtWidgets

from conf import host, user, password, database, base
from func import conn, show_db, execute_query, disconn, show_db_tables
from qyery import q2, q3, q0, create_starshie_table

connection = disconn()

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked_1)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)

    def btnClicked_1(self):

        try:
            connection = conn(host, user, database)
            text = str("Вы подключились к сереверу " + host)
            tabel = show_db_tables(connection, q0)
            i = 0
            """переводим кортеж в список"""
            tabel2 = []
            for x in tabel:
                tabel2.append(str(x))
            self.ui.comboBox.clear()
            for i in range(len(tabel2)):
                # Добавляем новые значения
                self.ui.comboBox.addItem(str(tabel2[int(i)][2:-3]))

        except Error as err:
            print(f"Error: '{err}'")
        self.ui.label.setText(text)
        self.ui.label.adjustSize()
        # Если не использовать, то часть текста исчезнет.
        self.ui.label_3.setText(host)
        self.ui.label_3.adjustSize()
        self.ui.label_5.setText(str(database))
        self.ui.label_5.adjustSize()

        return connection

    def btnClicked_2(self):


        try:
            connection = disconn()
            text = str("Вы отключились ")
            self.ui.comboBox.clear()

        except Error as err:
            print(f"Error: '{err}'")
        self.ui.label.setText(text)
        self.ui.label.adjustSize() # Если не использовать, то часть текста исчезнет.
        self.ui.label_3.setText("no")
        self.ui.label.adjustSize()
        self.ui.label_5.setText("no")
        self.ui.label.adjustSize()

    def btnClicked_3(self):
        name_tb_bd = self.ui.comboBox.currentText()
        print("нажал всетаки  "+name_tb_bd)
        query = """SELECT * FROM """+name_tb_bd
        connection = conn(host, user, database)
        res = show_db(connection, query)
        print(res)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = mywindow()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
