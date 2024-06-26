# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(629, 885)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 611, 608))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("* {\n"
"    color: rgb(0, 170, 0);\n"
"}")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setStyleSheet("* {\n"
"    color: rgb(0, 170, 0);\n"
"}")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.addButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.addButton.setFont(font)
        self.addButton.setStyleSheet("*{\n"
"    background-color: rgb(85, 255, 127);\n"
"}")
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 2, 1, 1, 2)
        self.meal = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.meal.setObjectName("meal")
        self.gridLayout.addWidget(self.meal, 0, 2, 1, 1)
        self.calories = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.calories.setObjectName("calories")
        self.gridLayout.addWidget(self.calories, 1, 2, 1, 1)
        self.cal_sum_label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.cal_sum_label.setStyleSheet("*{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.cal_sum_label.setObjectName("cal_sum_label")
        self.gridLayout.addWidget(self.cal_sum_label, 4, 1, 1, 1)
        self.sum_cal = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.sum_cal.setObjectName("sum_cal")
        self.gridLayout.addWidget(self.sum_cal, 4, 2, 1, 1)
        self.mealList = QtWidgets.QListWidget(parent=self.gridLayoutWidget)
        self.mealList.setMinimumSize(QtCore.QSize(250, 250))
        self.mealList.setObjectName("mealList")
        self.gridLayout.addWidget(self.mealList, 3, 1, 1, 2)
        self.image = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.image.setMinimumSize(QtCore.QSize(250, 250))
        self.image.setText("")
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image, 5, 1, 1, 2)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 680, 611, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.woman = QtWidgets.QRadioButton(parent=self.gridLayoutWidget_2)
        self.woman.setObjectName("woman")
        self.gridLayout_2.addWidget(self.woman, 0, 0, 1, 1)
        self.man = QtWidgets.QRadioButton(parent=self.gridLayoutWidget_2)
        self.man.setObjectName("man")
        self.gridLayout_2.addWidget(self.man, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 770, 611, 111))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.medium_activity = QtWidgets.QRadioButton(parent=self.gridLayoutWidget_3)
        self.medium_activity.setObjectName("medium_activity")
        self.gridLayout_3.addWidget(self.medium_activity, 1, 0, 1, 1)
        self.small_activity = QtWidgets.QRadioButton(parent=self.gridLayoutWidget_3)
        self.small_activity.setObjectName("small_activity")
        self.gridLayout_3.addWidget(self.small_activity, 0, 0, 1, 1)
        self.high_activity = QtWidgets.QRadioButton(parent=self.gridLayoutWidget_3)
        self.high_activity.setObjectName("high_activity")
        self.gridLayout_3.addWidget(self.high_activity, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(parent=Dialog)
        self.line.setGeometry(QtCore.QRect(20, 620, 601, 41))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kalkulator kalorii"))
        self.label_2.setText(_translate("Dialog", "Liczba kalorii"))
        self.label.setText(_translate("Dialog", "Nazwa posiłku"))
        self.addButton.setText(_translate("Dialog", "Dodaj"))
        self.cal_sum_label.setText(_translate("Dialog", "Suma spożytych kalorii"))
        self.sum_cal.setText(_translate("Dialog", "0"))
        self.woman.setText(_translate("Dialog", "Kobieta"))
        self.man.setText(_translate("Dialog", "Mężczyzna"))
        self.medium_activity.setText(_translate("Dialog", "Średnia aktywność fizyczna"))
        self.small_activity.setText(_translate("Dialog", "Mała aktywność fizyczna"))
        self.high_activity.setText(_translate("Dialog", "Duża aktywność fizyczna"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
