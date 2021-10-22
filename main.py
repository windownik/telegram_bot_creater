import create_handlers
from create_main_files import *
from create_keyboards import *
from create_states import *
import openpyxl
import btn_metods

# from PyQt5 import QtCore, QtGui, QtWidgets
#
#
# class Ui_Bot_window(object):
#     def setupUi(self, Bot_window):
#         Bot_window.setObjectName("Bot_window")
#         Bot_window.resize(960, 750)
#         Bot_window.setMinimumSize(QtCore.QSize(960, 750))
#         Bot_window.setMaximumSize(QtCore.QSize(960, 750))
#         self.centralwidget = QtWidgets.QWidget(Bot_window)
#         self.centralwidget.setObjectName("centralwidget")
#         self.add_handler_btn = QtWidgets.QPushButton(self.centralwidget)
#         self.add_handler_btn.setGeometry(QtCore.QRect(180, 670, 161, 31))
#         self.add_handler_btn.setObjectName("add_handler_btn")
#         self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
#         self.verticalScrollBar.setGeometry(QtCore.QRect(340, 50, 20, 611))
#         self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
#         self.verticalScrollBar.setObjectName("verticalScrollBar")
#         self.list_label = QtWidgets.QLabel(self.centralwidget)
#         self.list_label.setGeometry(QtCore.QRect(36, 20, 301, 21))
#         font = QtGui.QFont()
#         font.setPointSize(14)
#         self.list_label.setFont(font)
#         self.list_label.setObjectName("list_label")
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(420, 30, 161, 31))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.pushButton_2.setFont(font)
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.type_kboard_btn = QtWidgets.QPushButton(self.centralwidget)
#         self.type_kboard_btn.setGeometry(QtCore.QRect(600, 30, 161, 31))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.type_kboard_btn.setFont(font)
#         self.type_kboard_btn.setObjectName("type_kboard_btn")
#         self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_4.setGeometry(QtCore.QRect(790, 30, 161, 31))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.pushButton_4.setFont(font)
#         self.pushButton_4.setObjectName("pushButton_4")
#         self.confirm_btn = QtWidgets.QPushButton(self.centralwidget)
#         self.confirm_btn.setGeometry(QtCore.QRect(780, 430, 161, 31))
#         font = QtGui.QFont()
#         font.setPointSize(10)
#         self.confirm_btn.setFont(font)
#         self.confirm_btn.setObjectName("confirm_btn")
#         self.status_label = QtWidgets.QLabel(self.centralwidget)
#         self.status_label.setGeometry(QtCore.QRect(420, 70, 521, 21))
#         font = QtGui.QFont()
#         font.setPointSize(14)
#         self.status_label.setFont(font)
#         self.status_label.setObjectName("status_label")
#         self.main_text = QtWidgets.QTextEdit(self.centralwidget)
#         self.main_text.setGeometry(QtCore.QRect(420, 140, 521, 241))
#         self.main_text.setObjectName("main_text")
#         self.listWidget = QtWidgets.QListWidget(self.centralwidget)
#         self.listWidget.setGeometry(QtCore.QRect(30, 50, 311, 611))
#         self.listWidget.setObjectName("listWidget")
#         self.rework_btn = QtWidgets.QPushButton(self.centralwidget)
#         self.rework_btn.setGeometry(QtCore.QRect(30, 670, 141, 31))
#         self.rework_btn.setObjectName("rework_btn")
#         self.next_state = QtWidgets.QTextEdit(self.centralwidget)
#         self.next_state.setGeometry(QtCore.QRect(420, 390, 521, 31))
#         self.next_state.setObjectName("next_state")
#         self.previos_state = QtWidgets.QTextEdit(self.centralwidget)
#         self.previos_state.setGeometry(QtCore.QRect(420, 100, 521, 31))
#         self.previos_state.setObjectName("previos_state")
#         Bot_window.setCentralWidget(self.centralwidget)
#         self.statusbar = QtWidgets.QStatusBar(Bot_window)
#         self.statusbar.setObjectName("statusbar")
#         Bot_window.setStatusBar(self.statusbar)
#         self.menubar = QtWidgets.QMenuBar(Bot_window)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 21))
#         self.menubar.setObjectName("menubar")
#         Bot_window.setMenuBar(self.menubar)
#
#         self.retranslateUi(Bot_window)
#         QtCore.QMetaObject.connectSlotsByName(Bot_window)
#
#         self.clicked_btn()
#
#     def retranslateUi(self, Bot_window):
#         _translate = QtCore.QCoreApplication.translate
#         Bot_window.setWindowTitle(_translate("Bot_window", "MainWindow"))
#         self.add_handler_btn.setText(_translate("Bot_window", "Добавить хэндлер"))
#         self.list_label.setText(_translate("Bot_window", "Список хэндлеров"))
#         self.pushButton_2.setText(_translate("Bot_window", "Добавить клавиатуру"))
#         self.type_kboard_btn.setText(_translate("Bot_window", "Тип клавиатуры"))
#         self.pushButton_4.setText(_translate("Bot_window", "Изменить основной текст"))
#         self.confirm_btn.setText(_translate("Bot_window", "Сохранить"))
#         self.status_label.setText(_translate("Bot_window", "Статус"))
#         self.rework_btn.setText(_translate("Bot_window", "Обновить"))
#
#     def clicked_btn(self):
#         self.listWidget.itemClicked.connect(self.load_handler)
#         self.confirm_btn.clicked.connect(self.change_item)
#         self.rework_btn.clicked.connect(self.rework_list)
#
#     def change_item(self):
#         item_index = str(self.status_label.text()[15:])
#         item_text = str(self.main_text.toPlainText())
#         pre_state = self.previos_state.toPlainText()
#         next_state = self.previos_state.toPlainText()
#         btn_metods.change_item(index=item_index, main_text=item_text, previos_state=pre_state, next_state=next_state)
#         self.rework_list()
#
#     def rework_list(self):
#         self.listWidget.clear()
#         self.listWidget.addItems(btn_metods.create_list())
#
#     def load_handler(self, item):
#         index_item = str(item.text()).split(' |--| ')[0]
#         index_text = str(item.text()).split(' |--| ')[1]
#         btn_metods.read_item_data(index_item)
#         self.previos_state.setText(btn_metods.read_item_data(index_item)[0])
#         self.next_state.setText(btn_metods.read_item_data(index_item)[1])
#         self.status_label.setText(f'Выбран объект №{index_item}')
#         self.main_text.setText(index_text)
#
#
if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     Bot_window = QtWidgets.QMainWindow()
#     ui = Ui_Bot_window()
#     ui.setupUi(Bot_window)
#     Bot_window.show()
#     sys.exit(app.exec_())

    creat_main()
    creat_json()
    creat_dispatcher()
    creat_states()
    creat_init()
    creat_keyboards()
    create_handlers.create_handler()
