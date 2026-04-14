# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_update.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(346, 270)
        Dialog.setStyleSheet(u"/* 1. BACKGROUND JENDELA */\n"
"QDialog {\n"
"    background-color: #ffffff; /* Putih bersih */\n"
"}\n"
"\n"
"/* 2. JUDUL (Pastikan objectName-nya: label_judul) */\n"
"QLabel#label_judulstok {\n"
"    font-size: 20pt;\n"
"    font-weight: bold;\n"
"    color: #1f2937;\n"
"    margin-bottom: 15px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* 3. LABEL KETERANGAN (Nama Barang, SKU, dll) */\n"
"QLabel {\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"    color: #4b5563; /* Abu-abu gelap elegan */\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* 4. KOTAK INPUT (LineEdit & SpinBox) */\n"
"QLineEdit, QSpinBox {\n"
"    border: 1px solid #d1d5db;\n"
"    border-radius: 8px; /* Membuat sudut melengkung */\n"
"    padding: 10px;\n"
"    background-color: #f9fafb;\n"
"    color: #1f2937;\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"/* Efek saat kotak input diklik */\n"
"QLineEdit:focus, QSpinBox:focus {\n"
"    border: 2px solid #2563eb; /* Garis biru tebal */\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
""
                        "/* 5. TOMBOL TAMBAH (Pastikan objectName-nya: btn_simpan) */\n"
"QPushButton#btn_simpan_update {\n"
"    background-color: #2563eb; /* Biru Modern */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton#btn_simpan_update:hover {\n"
"    background-color: #1d4ed8; /* Biru lebih gelap saat disentuh */\n"
"}\n"
"\n"
"/* 6. TOMBOL BATAL (Pastikan objectName-nya: btn_batal) */\n"
"QPushButton#btn_batal_update {\n"
"    background-color: white;\n"
"    color: #374151;\n"
"    border: 1px solid #d1d5db;\n"
"    border-radius: 8px;\n"
"    padding: 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton#btn_batal_update:hover {\n"
"    background-color: #f3f4f6;\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_judulstok = QLabel(Dialog)
        self.label_judulstok.setObjectName(u"label_judulstok")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_judulstok.setFont(font)

        self.verticalLayout.addWidget(self.label_judulstok, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.txt_sku_update = QLineEdit(Dialog)
        self.txt_sku_update.setObjectName(u"txt_sku_update")

        self.verticalLayout.addWidget(self.txt_sku_update)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout.addWidget(self.label_4)

        self.input_jumlah_masuk = QSpinBox(Dialog)
        self.input_jumlah_masuk.setObjectName(u"input_jumlah_masuk")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.input_jumlah_masuk.setFont(font2)

        self.verticalLayout.addWidget(self.input_jumlah_masuk)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_batal_update = QPushButton(Dialog)
        self.btn_batal_update.setObjectName(u"btn_batal_update")

        self.horizontalLayout_3.addWidget(self.btn_batal_update)

        self.btn_simpan_update = QPushButton(Dialog)
        self.btn_simpan_update.setObjectName(u"btn_simpan_update")

        self.horizontalLayout_3.addWidget(self.btn_simpan_update)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_judulstok.setText(QCoreApplication.translate("Dialog", u"Update Stok Barang", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Kode Sku", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Jumlah Stok Masuk", None))
        self.btn_batal_update.setText(QCoreApplication.translate("Dialog", u"Batal", None))
        self.btn_simpan_update.setText(QCoreApplication.translate("Dialog", u"Simpan Update", None))
    # retranslateUi

