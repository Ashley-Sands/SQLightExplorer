# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messageWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class UiMessageDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 119)
        self.buttons_yes = QtWidgets.QDialogButtonBox(Dialog)
        self.buttons_yes.setGeometry(QtCore.QRect(30, 80, 341, 32))
        self.buttons_yes.setOrientation(QtCore.Qt.Horizontal)
        self.buttons_yes.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttons_yes.setObjectName("buttons_yes")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 301, 51))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttons_yes.accepted.connect(Dialog.accept)
        self.buttons_yes.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AMSql - message"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Error: Could not open table</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
