from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import MySQLdb
from PyQt5.uic import loadUiType

ui,_ = loadUiType('library.ui')

class MainApp(QMainWindow , ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI_Changes()
        self.Handle_Buttons()

    def Handle_UI_Changes(self):
        self.Hiding_Themes()
        self.tabWidget.tabBar().setVisible(False)

    def Handle_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton.clicked.connect(self.Day_To_Day_Button)
        self.pushButton_2.clicked.connect(self.Books_Button)
        self.pushButton_3.clicked.connect(self.Users_Button)
        self.pushButton_4.clicked.connect(self.Settings_Button)

        self.pushButton_7.clicked.connect(self.Add_New_Books)

        self.pushButton_14.clicked.connect(self.Add_New_Category)

    def Show_Themes(self):
        self.groupBox_3.show()

    def Hiding_Themes(self):
        self.groupBox_3.hide()
        self.pushButton_21.clicked.connect(self.Hiding_Themes)

    #########################################################
    ####################OPEN TABS############################
    def Day_To_Day_Button(self):
        self.tabWidget.setCurrentIndex(0)
    def Books_Button(self):
        self.tabWidget.setCurrentIndex(1)
    def Users_Button(self):
        self.tabWidget.setCurrentIndex(2)
    def Settings_Button(self):
        self.tabWidget.setCurrentIndex(3)

    #########################################################
    ####################BOOKS############################
    def Add_New_Books(self):
        self.db = MySQLdb.connect(host="localhost", user="root", password="1234", db="library")
        self.cur = self.db.cursor()

        book_title = self.lineEdit_5.text()
        book_code = self.lineEdit_4.text()
        book_category = self.comboBox.CurrentText()
        book_author = self.comboBox_4.CurrentText()
        book_publisher = self.comboBox_5.CurrentText()
        book_price = self.lineEdit_3.text()

    def Edit_Books(self):
        pass
    def Search_Books(self):
        pass
    def Delete_Books(self):
        pass

    #########################################################
    ########################USERS############################
    def Add_New_Users(self):
        pass
    def Edit_Users(self):
        pass
    def Login_Users(self):
        pass
    def Delete_Users(self):
        pass


    #########################################################
    ########################SETTINGS############################


    def Add_New_Category(self):
        self.db = MySQLdb.connect(host="localhost", user="root", password="1234", db="library")
        self.cur = self.db.cursor()

        category_name = self.lineEdit_19.text()

        self.cur.execute('''
            INSERT INTO category (category_name) VALUES (%s)
        ''',(category_name,))

        self.db.commit()
        print('DONE')

    def Add_New_Author(self):
        pass
    def Add_New_Publisher(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()