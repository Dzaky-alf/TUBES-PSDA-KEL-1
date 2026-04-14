# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_tambah.ui'
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
        Dialog.resize(462, 436)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(18)
        font.setBold(True)
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"/* 1. BACKGROUND JENDELA */\n"
"QDialog {\n"
"    background-color: #ffffff; /* Putih bersih */\n"
"}\n"
"\n"
"/* 2. JUDUL (Pastikan objectName-nya: label_judul) */\n"
"QLabel#label_judul {\n"
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
"/* "
                        "5. TOMBOL TAMBAH (Pastikan objectName-nya: btn_simpan) */\n"
"QPushButton#btn_simpan_baru {\n"
"    background-color: #2563eb; /* Biru Modern */\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton#btn_simpan_baru:hover {\n"
"    background-color: #1d4ed8; /* Biru lebih gelap saat disentuh */\n"
"}\n"
"\n"
"/* 6. TOMBOL BATAL (Pastikan objectName-nya: btn_batal) */\n"
"QPushButton#btn_batal_baru {\n"
"    background-color: white;\n"
"    color: #374151;\n"
"    border: 1px solid #d1d5db;\n"
"    border-radius: 8px;\n"
"    padding: 12px;\n"
"    font-weight: bold;\n"
"    font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton#btn_batal_baru:hover {\n"
"    background-color: #f3f4f6;\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(25, 20, 25, 20)
        self.label_judul = QLabel(Dialog)
        self.label_judul.setObjectName(u"label_judul")

        self.verticalLayout.addWidget(self.label_judul, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.txt_nama_baru = QLineEdit(Dialog)
        self.txt_nama_baru.setObjectName(u"txt_nama_baru")

        self.verticalLayout.addWidget(self.txt_nama_baru)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout.addWidget(self.label_3)

        self.txt_sku_baru = QLineEdit(Dialog)
        self.txt_sku_baru.setObjectName(u"txt_sku_baru")

        self.verticalLayout.addWidget(self.txt_sku_baru)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout.addWidget(self.label_4)

        self.input_stok_baru = QSpinBox(Dialog)
        self.input_stok_baru.setObjectName(u"input_stok_baru")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.input_stok_baru.setFont(font2)

        self.verticalLayout.addWidget(self.input_stok_baru)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout.addWidget(self.label_5)

        self.txt_kategori_baru = QLineEdit(Dialog)
        self.txt_kategori_baru.setObjectName(u"txt_kategori_baru")

        self.verticalLayout.addWidget(self.txt_kategori_baru)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_batal_baru = QPushButton(Dialog)
        self.btn_batal_baru.setObjectName(u"btn_batal_baru")

        self.horizontalLayout_3.addWidget(self.btn_batal_baru)

        self.btn_simpan_baru = QPushButton(Dialog)
        self.btn_simpan_baru.setObjectName(u"btn_simpan_baru")

        self.horizontalLayout_3.addWidget(self.btn_simpan_baru)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_judul.setText(QCoreApplication.translate("Dialog", u"Tambah Barang", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nama Barang ", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Kode SKU", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Stok", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Kategori", None))
        self.btn_batal_baru.setText(QCoreApplication.translate("Dialog", u"Batal", None))
        self.btn_simpan_baru.setText(QCoreApplication.translate("Dialog", u"Tambah", None))
    # retranslateUi

