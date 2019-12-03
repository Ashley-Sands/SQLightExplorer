# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialogue_TextEnter.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class UiTextDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(572, 120)
        self.buttons_yes = QtWidgets.QDialogButtonBox(Dialog)
        self.buttons_yes.setGeometry(QtCore.QRect(20, 80, 531, 32))
        self.buttons_yes.setOrientation(QtCore.Qt.Horizontal)
        self.buttons_yes.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Open)
        self.buttons_yes.setObjectName("buttons_open")
        self.text_input = QtWidgets.QLineEdit(Dialog)
        self.text_input.setGeometry(QtCore.QRect(20, 40, 531, 31))
        self.text_input.setObjectName("text_input")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 73, 29))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.object_name = QtWidgets.QLabel(Dialog)
        self.object_name.setGeometry(QtCore.QRect(65, 10, 189, 29))
        self.object_name.setObjectName("object_name")

        self.retranslateUi(Dialog)
        self.buttons_yes.accepted.connect(Dialog.accept)
        self.buttons_yes.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AMSql"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter</span></p></body></html>"))
        self.object_name.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Database Name</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
