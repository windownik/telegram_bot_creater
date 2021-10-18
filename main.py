import create_handlers
from create_main_files import *
from create_keyboards import *
from create_states import *
import openpyxl

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Bot_window(object):
    def setupUi(self, Bot_window):
        Bot_window.setObjectName("Bot_window")
        Bot_window.resize(960, 750)
        self.centralwidget = QtWidgets.QWidget(Bot_window)
        self.centralwidget.setObjectName("centralwidget")
        self.add_handler_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_handler_btn.setGeometry(QtCore.QRect(180, 670, 161, 31))
        self.add_handler_btn.setObjectName("add_handler_btn")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(340, 50, 20, 611))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.list_label = QtWidgets.QLabel(self.centralwidget)
        self.list_label.setGeometry(QtCore.QRect(36, 20, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.list_label.setFont(font)
        self.list_label.setObjectName("list_label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 30, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 30, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(790, 30, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.confirm_btn = QtWidgets.QPushButton(self.centralwidget)
        self.confirm_btn.setGeometry(QtCore.QRect(780, 350, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.confirm_btn.setFont(font)
        self.confirm_btn.setObjectName("confirm_btn")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(420, 70, 531, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.status_label.setFont(font)
        self.status_label.setObjectName("status_label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(423, 100, 521, 241))
        self.textEdit.setObjectName("textEdit")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 50, 311, 611))
        self.listWidget.setObjectName("listWidget")
        Bot_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Bot_window)
        self.statusbar.setObjectName("statusbar")
        Bot_window.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(Bot_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 21))
        self.menubar.setObjectName("menubar")
        Bot_window.setMenuBar(self.menubar)

        self.retranslateUi(Bot_window)
        QtCore.QMetaObject.connectSlotsByName(Bot_window)

        self.listWidget.addItem("123")
        self.listWidget.addItem("254274")

    def retranslateUi(self, Bot_window):
        _translate = QtCore.QCoreApplication.translate
        Bot_window.setWindowTitle(_translate("Bot_window", "BOT Creater"))
        self.add_handler_btn.setText(_translate("Bot_window", "Добавить хэндлер"))
        self.list_label.setText(_translate("Bot_window", "Список хэндлеров"))
        self.pushButton_2.setText(_translate("Bot_window", "Добавить клавиатуру"))
        self.pushButton_3.setText(_translate("Bot_window", "Добавить клавиатуру"))
        self.pushButton_4.setText(_translate("Bot_window", "Изменить основной текст"))
        self.confirm_btn.setText(_translate("Bot_window", "Задать"))
        self.status_label.setText(_translate("Bot_window", "Статус"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bot_window = QtWidgets.QMainWindow()
    ui = Ui_Bot_window()
    ui.setupUi(Bot_window)
    Bot_window.show()
    sys.exit(app.exec_())

    # creat_main()
    # creat_json()
    # creat_dispatcher()
    # creat_states()
    # creat_init()
    # creat_keyboards()
    # create_handlers.create_hendler()
