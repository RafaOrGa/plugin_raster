# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModuloRaster(object):
    def setupUi(self, ModuloRaster):
        ModuloRaster.setObjectName("ModuloRaster")
        ModuloRaster.resize(411, 226)
        self.centralwidget = QtWidgets.QWidget(ModuloRaster)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 331, 151))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 111, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(10, 50, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(160, 50, 41, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 171, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 47, 13))
        self.label_3.setObjectName("label_3")
        ModuloRaster.setCentralWidget(self.centralwidget)

        self.retranslateUi(ModuloRaster)
        QtCore.QMetaObject.connectSlotsByName(ModuloRaster)

    def retranslateUi(self, ModuloRaster):
        _translate = QtCore.QCoreApplication.translate
        ModuloRaster.setWindowTitle(_translate("ModuloRaster", "Modulo Raster"))
        self.groupBox.setTitle(_translate("ModuloRaster", "Datos de entrada"))
        self.label.setText(_translate("ModuloRaster", "Selecciona el archivo"))
        self.pushButton.setText(_translate("ModuloRaster", "..."))
        self.label_2.setText(_translate("ModuloRaster", "Sistema de referenc ia geoespacial"))
        self.label_3.setText(_translate("ModuloRaster", "SRG"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModuloRaster = QtWidgets.QMainWindow()
    ui = Ui_ModuloRaster()
    ui.setupUi(ModuloRaster)
    ModuloRaster.show()
    sys.exit(app.exec_())