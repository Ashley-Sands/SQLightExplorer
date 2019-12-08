# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ams_config.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class UiConfigDialog(object):
    def setupUi(self, amsql_config):
        amsql_config.setObjectName("amsql_config")
        amsql_config.resize(400, 301)
        amsql_config.setWindowOpacity(1.0)
        self.buttons_yes = QtWidgets.QDialogButtonBox(amsql_config)
        self.buttons_yes.setGeometry(QtCore.QRect(30, 260, 341, 32))
        self.buttons_yes.setOrientation(QtCore.Qt.Horizontal)
        self.buttons_yes.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save)
        self.buttons_yes.setCenterButtons(False)
        self.buttons_yes.setObjectName("buttons_yes")
        self.label = QtWidgets.QLabel(amsql_config)
        self.label.setGeometry(QtCore.QRect(15, 45, 140, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(amsql_config)
        self.label_2.setGeometry(QtCore.QRect(15, 15, 600, 25))
        self.label_2.setObjectName("label_2")
        self.text_host = QtWidgets.QLineEdit(amsql_config)
        self.text_host.setGeometry(QtCore.QRect(155, 45, 230, 20))
        self.text_host.setObjectName("text_host")
        self.label_3 = QtWidgets.QLabel(amsql_config)
        self.label_3.setGeometry(QtCore.QRect(15, 70, 140, 20))
        self.label_3.setObjectName("label_3")
        self.text_port = QtWidgets.QLineEdit(amsql_config)
        self.text_port.setGeometry(QtCore.QRect(155, 70, 230, 20))
        self.text_port.setObjectName("text_port")
        self.label_4 = QtWidgets.QLabel(amsql_config)
        self.label_4.setGeometry(QtCore.QRect(15, 145, 201, 20))
        self.label_4.setObjectName("label_4")
        self.text_default_databases = QtWidgets.QPlainTextEdit(amsql_config)
        self.text_default_databases.setGeometry(QtCore.QRect(15, 170, 370, 75))
        self.text_default_databases.setObjectName("text_default_databases")
        self.label_5 = QtWidgets.QLabel(amsql_config)
        self.label_5.setGeometry(QtCore.QRect(15, 120, 140, 20))
        self.label_5.setObjectName("label_5")
        self.spinBox_timeout = QtWidgets.QSpinBox(amsql_config)
        self.spinBox_timeout.setGeometry(QtCore.QRect(155, 120, 150, 22))
        self.spinBox_timeout.setMinimum(5)
        self.spinBox_timeout.setMaximum(120)
        self.spinBox_timeout.setProperty("value", 10)
        self.spinBox_timeout.setDisplayIntegerBase(10)
        self.spinBox_timeout.setObjectName("spinBox_timeout")
        self.label_6 = QtWidgets.QLabel(amsql_config)
        self.label_6.setGeometry(QtCore.QRect(315, 120, 140, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(amsql_config)
        self.label_7.setGeometry(QtCore.QRect(15, 95, 140, 20))
        self.label_7.setObjectName("label_7")
        self.text_root_dir = QtWidgets.QLineEdit(amsql_config)
        self.text_root_dir.setGeometry(QtCore.QRect(155, 95, 230, 20))
        self.text_root_dir.setObjectName("text_root_dir")

        self.retranslateUi(amsql_config)
        self.buttons_yes.accepted.connect(amsql_config.accept)
        self.buttons_yes.rejected.connect(amsql_config.reject)
        QtCore.QMetaObject.connectSlotsByName(amsql_config)

    def retranslateUi(self, amsql_config):
        _translate = QtCore.QCoreApplication.translate
        amsql_config.setWindowTitle(_translate("amsql_config", "AMSql - Config"))
        self.label.setText(_translate("amsql_config",
                                      "<html><head/><body><p><span style=\" font-size:11pt;\">Host</span></p></body></html>"))
        self.label_2.setText(_translate("amsql_config",
                                        "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">SQLight Host Server Config</span></p></body></html>"))
        self.text_host.setText(_translate("amsql_config", "192.0.0.1"))
        self.label_3.setText(_translate("amsql_config",
                                        "<html><head/><body><p><span style=\" font-size:11pt;\">Port</span></p></body></html>"))
        self.text_port.setText(_translate("amsql_config", "6000"))
        self.label_4.setText(_translate("amsql_config",
                                        "<html><head/><body><p><span style=\" font-size:11pt;\">Default databases (1 per line)</span></p></body></html>"))
        self.label_5.setText(_translate("amsql_config",
                                        "<html><head/><body><p><span style=\" font-size:11pt;\">Connection Timeout</span></p></body></html>"))
        self.label_6.setText(_translate("amsql_config",
                                        "<html><head/><body><p><span style=\" font-size:11pt;\">Seconds</span></p></body></html>"))
        self.label_7.setText(_translate("amsql_config",
                                        "<html><head/><body><p><span style=\" font-size:11pt;\">SQL Root Path</span></p></body></html>"))
        self.text_root_dir.setText(_translate("amsql_config", "/amsql"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UiConfigDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
