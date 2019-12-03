# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ams_config.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class UiConfigDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 142)
        self.buttons_yes = QtWidgets.QDialogButtonBox(Dialog)
        self.buttons_yes.setGeometry(QtCore.QRect(30, 100, 341, 32))
        self.buttons_yes.setOrientation(QtCore.Qt.Horizontal)
        self.buttons_yes.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttons_yes.setCenterButtons(False)
        self.buttons_yes.setObjectName("buttons_yes")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(15, 45, 100, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(15, 15, 600, 25))
        self.label_2.setObjectName("label_2")
        self.text_host = QtWidgets.QLineEdit(Dialog)
        self.text_host.setGeometry(QtCore.QRect(115, 45, 250, 20))
        self.text_host.setObjectName("text_host")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(15, 70, 100, 20))
        self.label_3.setObjectName("label_3")
        self.text_port = QtWidgets.QLineEdit(Dialog)
        self.text_port.setGeometry(QtCore.QRect(115, 70, 250, 20))
        self.text_port.setObjectName("text_port")

        self.retranslateUi(Dialog)
        self.buttons_yes.accepted.connect(Dialog.accept)
        self.buttons_yes.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\">Host</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">SQLight Host Server Config</span></p></body></html>"))
        self.text_host.setText(_translate("Dialog", "192.0.0.1"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\">Port</span></p></body></html>"))
        self.text_port.setText(_translate("Dialog", "6000"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UiConfigDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
