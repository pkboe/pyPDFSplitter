from PyQt5 import QtCore, QtGui, QtWidgets
from spliter import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(624, 257)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("color:rgb(0, 170, 255);\n"
"font: 8pt \"Segoe Print\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 3)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 2)
        self.actionfilePick = QtWidgets.QAction(Dialog)
        self.actionfilePick.setObjectName("actionfilePick")

        self.retranslateUi(Dialog)
        self.pushButton_3.clicked.connect(self.actionfilePick.trigger) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def selectFile(self):
        filter = "pdf(*.pdf)"
        self.filePath = QtWidgets.QFileDialog.getOpenFileName(filter=filter)
        self.label_2.setText(self.filePath[0])

    def splitPDF(self):
        keys=self.lineEdit.text()
        print(self.filePath[0])
        print(keys)
        if self.filePath[0] != '':
            if keys != ['']:
                if keys.split(',') != ['']:
                    pdfCSVSplitter(self.filePath[0], keys.split(','))
                if keys.split('+') == ['']:
                    pdfADDSplitter(self.filePath[0], keys.split('+'))
                self.label.setText('PDF Split Completed')
                # popup message 

            else:
                self.label.setText('Please enter keys to split')

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("PDF Split Completed")
        msg.setWindowTitle("PDF Splitter")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
        
        self.label_2.setText("Select PDF File ")
        self.lineEdit.setText("")
        pass
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PDF Splitter"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">PDF Splitter V1.0</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Select PDF File"))
        self.pushButton_3.setText(_translate("Dialog", "Select..."))
        self.pushButton_2.setText(_translate("Dialog", "Split"))
        self.label_3.setText(_translate("Dialog", "Split by keys CSV or +"))
        self.pushButton.setText(_translate("Dialog", "Cancel"))
        self.actionfilePick.setText(_translate("Dialog", "filePick"))
        #assigning Actions
        self.pushButton.clicked.connect(app.closeAllWindows) # type: ignore
        # click pushBUtton_3 to select file
        self.pushButton_3.clicked.connect(self.selectFile) # type: ignore
        self.pushButton_2.clicked.connect(self.splitPDF) # type: ignore




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
