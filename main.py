import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.kcal = 0.00
        self.ui.mealList.setDisabled(True)
        self.ui.addButton.clicked.connect(self.addMeal)
        self.show()

    def addMeal(self):
        if self.ui.woman.isChecked() is False and self.ui.man.isChecked() is False:
            msgbox = QMessageBox()
            msgbox.setText("Zaznacz płeć")
            msgbox.setWindowTitle("Błąd")
            msgbox.exec()
            return
        if self.ui.small_activity.isChecked() is False and self.ui.medium_activity.isChecked() is False and self.ui.high_activity.isChecked() is False:
            msgbox = QMessageBox()
            msgbox.setText("Zaznacz swoją aktywność")
            msgbox.setWindowTitle("Błąd")
            msgbox.exec()
            return
        meal = self.ui.meal.text()
        cal = self.ui.calories.text()
        cal_numb = float(cal.replace(",", "."))
        self.kcal += cal_numb
        self.ui.mealList.addItem(f"{meal} - {cal_numb}")
        self.ui.sum_cal.setText(f'{round(self.kcal, 2)}')
        self.updateCalories()

    def updateCalories(self):
        if self.ui.woman.isChecked():
            if self.ui.small_activity.isChecked():
                kcal1 = (self.kcal/1700.00)*100.00
                if kcal1 <= 80.00:
                    self.ui.cal_sum_label.setStyleSheet(f'background-color: rgb(0, 255, 0)')
                    self.ui.image.setPixmap(QPixmap("1.jpg").scaled(250, 250))
                elif kcal1 <= 100.00:
                    self.ui.cal_sum_label.setStyleSheet(f'background-color: #000000')
                    self.ui.image.setPixmap(QPixmap("2.jpg").scaled(250, 250))
                elif kcal1 > 100:
                    self.ui.cal_sum_label.setStyleSheet(f'background-color: rgb(255, 0, 0)')
                    self.ui.image.setPixmap(QPixmap("3.jpg").scaled(250, 250))
            elif self.ui.medium_activity.isChecked():
                kcal1 = (self.kcal / 1900.00) * 100.00
                if kcal1 <= 80.00:
                    self.ui.cal_sum_label.setStyleSheet(f'background-color: rgb(0, 255, 0)')
                    self.ui.image.setPixmap(QPixmap("1.jpg").scaled(250, 250))
                elif kcal1 <= 100.00:
                    self.ui.cal_sum_label.setStyleSheet(f'background-color: #000000')
                    self.ui.image.setPixmap(QPixmap("2.jpg").scaled(250, 250))
                elif kcal1 > 100:
                    self.ui.cal_sum_label.setStyleSheet(f'background-color: rgb(255, 0, 0)')
                    self.ui.image.setPixmap(QPixmap("3.jpg").scaled(250, 250))
            elif self.ui.high_activity.isChecked():
                kcal1 = (self.kcal / 2100.00) * 100.00
                if kcal1 <= 80.00:
                    self.ui.cal_sum_label.setStyleSheet(f'background-color: rgb(0, 255, 0)')
                    self.ui.image.setPixmap(QPixmap("1.jpg").scaled(250, 250))
                elif kcal1 <= 100.00:
                    self.ui.cal_sum_label.setStyleSheet(f'background-color: #000000')
                    self.ui.image.setPixmap(QPixmap("2.jpg").scaled(250, 250))
                elif kcal1 > 100:
                    self.ui.cal_sum_label.setStyleSheet(f'background-color: rgb(255, 0, 0)')
                    self.ui.image.setPixmap(QPixmap("3.jpg").scaled(250, 250))
        elif self.ui.man.isChecked():
            if self.ui.small_activity.isChecked():
                kcal1 = (self.kcal / 1900.00) * 100.00
                if kcal1 <= 80.00:
                    self.ui.cal_sum_label.setStyleSheet(f'background-color: rgb(0, 255, 0)')
                    self.ui.image.setPixmap(QPixmap("1.jpg").scaled(250, 250))
                elif kcal1 <= 100.00:
                    self.ui.cal_sum_label.setStyleSheet(f'background-color: #000000')
                    self.ui.image.setPixmap(QPixmap("2.jpg").scaled(250, 250))
                elif kcal1 > 100:
                    self.ui.cal_sum_label.setStyleSheet(f'background-color: rgb(255, 0, 0)')
                    self.ui.image.setPixmap(QPixmap("3.jpg").scaled(250, 250))
            elif self.ui.medium_activity.isChecked():
                kcal1 = (self.kcal / 2200.00) * 100.00
                if kcal1 <= 80.00:
                    self.ui.cal_sum_label.setStyleSheet(f'background-color: rgb(0, 255, 0)')
                    self.ui.image.setPixmap(QPixmap("1.jpg").scaled(250, 250))
                elif kcal1 <= 100.00:
                    self.ui.cal_sum_label.setStyleSheet(f'background-color: #000000')
                    self.ui.image.setPixmap(QPixmap("2.jpg").scaled(250, 250))
                elif kcal1 > 100:
                    self.ui.cal_sum_label.setStyleSheet(f'background-color: rgb(255, 0, 0)')
                    self.ui.image.setPixmap(QPixmap("3.jpg").scaled(250, 250))
            elif self.ui.high_activity.isChecked():
                kcal1 = (self.kcal / 2500.00) * 100.00
                if kcal1 <= 80.00:
                    self.ui.cal_sum_label.setStyleSheet(f'background-color: rgb(0, 255, 0)')
                    self.ui.image.setPixmap(QPixmap("1.jpg").scaled(250, 250))
                elif kcal1 <= 100.00:
                    self.ui.cal_sum_label.setStyleSheet(f'background-color: #000000')
                    self.ui.image.setPixmap(QPixmap("2.jpg").scaled(250, 250))
                elif kcal1 > 100:
                    self.ui.cal_sum_label.setStyleSheet(f'background-color: rgb(255, 0, 0)')
                    self.ui.image.setPixmap(QPixmap("3.jpg").scaled(250, 250))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyForm()
    ex.show()
    sys.exit(app.exec())
