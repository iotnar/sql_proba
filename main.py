# This Python file uses the following encoding: utf-8



import mysql.connector
from mydesign import Ui_MainWindow
import sys

from getpass import getpass
from mysql.connector import connect, Error
from PyQt5 import QtCore, QtGui, QtWidgets

from conf import host,user,password,database,base
from func import conn,show_db,execute_query,disconn
from qyery import q3,create_starshie_table


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # подключение клик-сигнал к слоту btnClicked
        self.ui.pushButton.clicked.connect(self.btnClicked_1)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)

    def btnClicked_1(self):

        try:
            connection = conn(host,user,database)
            # execute_query(connection,create_starshie_table)
            results = show_db(connection, q3)
            text = str("Вы подключились к сереверу "+ host)

        except Error as err:
            print(f"Error: '{err}'")
        self.ui.label.setText(text)
        self.ui.label.adjustSize()# Если не использовать, то часть текста исчезнет.
        self.ui.label_3.setText(str(host))
        self.ui.label.adjustSize()
        self.ui.label_5.setText(str(database))
        self.ui.label.adjustSize()

    def btnClicked_2(self):

        try:
            connection = disconn()
            text = str("Вы отключились ")

        except Error as err:
            print(f"Error: '{err}'")
        self.ui.label.setText(text)
        self.ui.label.adjustSize() # Если не использовать, то часть текста исчезнет.
        self.ui.label_3.setText("no")
        self.ui.label.adjustSize()
        self.ui.label_5.setText("no")
        self.ui.label.adjustSize()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = mywindow()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
