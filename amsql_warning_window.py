# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialogue_Warning.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 97)
        self.buttons_yes = QtWidgets.QDialogButtonBox(Dialog)
        self.buttons_yes.setGeometry(QtCore.QRect(30, 60, 341, 32))
        self.buttons_yes.setOrientation(QtCore.Qt.Horizontal)
        self.buttons_yes.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Yes)
        self.buttons_yes.setObjectName("buttons_yes")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 381, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.table_name = QtWidgets.QLabel(Dialog)
        self.table_name.setGeometry(QtCore.QRect(10, 30, 381, 21))
        self.table_name.setAlignment(QtCore.Qt.AlignCenter)
        self.table_name.setObjectName("table_name")

        self.retranslateUi(Dialog)
        self.buttons_yes.accepted.connect(Dialog.accept)
        self.buttons_yes.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AMSql - Warning"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Are You Sure You Want To Drop</span></p></body></html>"))
        self.table_name.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Table Name</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
