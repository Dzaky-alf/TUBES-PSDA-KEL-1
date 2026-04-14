# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1155, 584)
        self.actionactionCari = QAction(MainWindow)
        self.actionactionCari.setObjectName(u"actionactionCari")
        icon = QIcon()
        icon.addFile(u"search-searching-icon-vector-magnifying-260nw-1613155609.webp", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionactionCari.setIcon(icon)
        self.actionactionCari.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_9 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.sidebar = QFrame(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMinimumSize(QSize(250, 0))
        self.sidebar.setMaximumSize(QSize(250, 16777215))
        self.sidebar.setStyleSheet(u"\n"
"QFrame#frame_5 {\n"
"    background-color: #f8fafc; \n"
"    border-right: 1px solid #e2e8f0; \n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"\n"
"QLabel#label_9 {\n"
"    background-color: transparent;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #334155; \n"
"    text-align: left;\n"
"    padding: 15px 25px;\n"
"    border: none;\n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ffffff; \n"
"    color: #3b82f6;\n"
"    border-radius: 8px;\n"
"    margin: 0px 10px;\n"
"}")
        self.sidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.sidebar)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_9 = QLabel(self.sidebar)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 150))
        self.label_9.setPixmap(QPixmap(u"Gemini_Generated_Image_tdtyybtdtyybtdty.png"))
        self.label_9.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label_9)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_dashboard = QPushButton(self.sidebar)
        self.btn_dashboard.setObjectName(u"btn_dashboard")

        self.verticalLayout.addWidget(self.btn_dashboard)

        self.btn_stok = QPushButton(self.sidebar)
        self.btn_stok.setObjectName(u"btn_stok")

        self.verticalLayout.addWidget(self.btn_stok)

        self.btn_restock = QPushButton(self.sidebar)
        self.btn_restock.setObjectName(u"btn_restock")

        self.verticalLayout.addWidget(self.btn_restock)

        self.btn_tentang = QPushButton(self.sidebar)
        self.btn_tentang.setObjectName(u"btn_tentang")

        self.verticalLayout.addWidget(self.btn_tentang)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_4.addLayout(self.verticalLayout)


        self.horizontalLayout_9.addWidget(self.sidebar)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.horizontalLayout_11 = QHBoxLayout(self.page_5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.scrollArea = QScrollArea(self.page_5)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 861, 503))
        self.horizontalLayout_10 = QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(20, 9, 20, 0)
        self.label_judul_4 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_judul_4.setObjectName(u"label_judul_4")
        font = QFont()
        font.setFamilies([u"Arial Rounded MT"])
        font.setPointSize(18)
        font.setBold(True)
        self.label_judul_4.setFont(font)

        self.verticalLayout_10.addWidget(self.label_judul_4)

        self.label_14 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_14.setObjectName(u"label_14")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_14.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_14)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 15)
        self.frame_13 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 100))
        self.frame_13.setStyleSheet(u"/* Ini ditaruh di StyleSheet milik Frame Kartu */\n"
"QFrame {\n"
"    background-color: white;\n"
"    border: 1px solid #e5e7eb;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"/* Tambahkan ini di bawahnya biar label di dalamnya bersih */\n"
"QLabel {\n"
"    border: none;\n"
"}")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 10, 91, 31))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_15.setFont(font2)
        self.label_total_produk_4 = QLabel(self.frame_13)
        self.label_total_produk_4.setObjectName(u"label_total_produk_4")
        self.label_total_produk_4.setGeometry(QRect(20, 40, 81, 31))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_total_produk_4.setFont(font3)

        self.horizontalLayout_7.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 100))
        self.frame_14.setStyleSheet(u"QFrame {\n"
"    background-color: white;\n"
"    border: 1px solid #e5e7eb;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    border: none;\n"
"}")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.label_16 = QLabel(self.frame_14)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 20, 111, 16))
        self.label_16.setFont(font2)
        self.label_total_stok_4 = QLabel(self.frame_14)
        self.label_total_stok_4.setObjectName(u"label_total_stok_4")
        self.label_total_stok_4.setGeometry(QRect(20, 40, 71, 31))
        self.label_total_stok_4.setFont(font3)

        self.horizontalLayout_7.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(268, 100))
        self.frame_15.setStyleSheet(u"QFrame {\n"
"    background-color: white;\n"
"    border: 1px solid #e5e7eb;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    border: none;\n"
"}")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.label_17 = QLabel(self.frame_15)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 20, 111, 21))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.label_17.setFont(font4)
        self.label_17.setStyleSheet(u"QLabel {\n"
"    color: #e11d48; /* Warna merah peringatan */\n"
"    font-weight: bold;\n"
"    border: none;\n"
"}")
        self.label_stok_rendah_4 = QLabel(self.frame_15)
        self.label_stok_rendah_4.setObjectName(u"label_stok_rendah_4")
        self.label_stok_rendah_4.setGeometry(QRect(30, 40, 49, 31))
        self.label_stok_rendah_4.setFont(font3)
        self.label_stok_rendah_4.setStyleSheet(u"QLabel {\n"
"    color: #e11d48; /* Warna merah peringatan */\n"
"    font-weight: bold;\n"
"    border: none;\n"
"}")

        self.horizontalLayout_7.addWidget(self.frame_15)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.frame_16 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(300, 60))
        self.frame_16.setStyleSheet(u"\n"
"QFrame {\n"
"    background-color: #f9fafb; \n"
"    border: 1px solid #e5e7eb; \n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: white;\n"
"    border: 1px solid #d1d5db;\n"
"    border-radius: 8px;\n"
"    padding: 8px 12px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #d1d5db;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #2563eb;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"}")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.input_cari_4 = QLineEdit(self.frame_16)
        self.input_cari_4.setObjectName(u"input_cari_4")
        self.input_cari_4.setMinimumSize(QSize(200, 40))

        self.horizontalLayout_8.addWidget(self.input_cari_4)

        self.combo_kategori_4 = QComboBox(self.frame_16)
        self.combo_kategori_4.addItem("")
        self.combo_kategori_4.addItem("")
        self.combo_kategori_4.addItem("")
        self.combo_kategori_4.addItem("")
        self.combo_kategori_4.setObjectName(u"combo_kategori_4")
        self.combo_kategori_4.setMinimumSize(QSize(120, 40))

        self.horizontalLayout_8.addWidget(self.combo_kategori_4)

        self.btn_tambah_4 = QPushButton(self.frame_16)
        self.btn_tambah_4.setObjectName(u"btn_tambah_4")
        self.btn_tambah_4.setEnabled(True)
        self.btn_tambah_4.setMinimumSize(QSize(180, 40))

        self.horizontalLayout_8.addWidget(self.btn_tambah_4)

        self.btn_hapus_4 = QPushButton(self.frame_16)
        self.btn_hapus_4.setObjectName(u"btn_hapus_4")
        self.btn_hapus_4.setMinimumSize(QSize(0, 40))
        self.btn_hapus_4.setStyleSheet(u"QPushButton {\n"
"    background-color: #fff5f5;    /* Latar belakang merah sangat muda */\n"
"    border: 1px solid #ff8a80;    /* Garis pinggir merah pastel */\n"
"    color: #e53935;               /* Warna teks merah cerah */\n"
"    border-radius: 6px;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ffebee;    /* Sedikit lebih gelap saat kursor lewat */\n"
"    border: 1px solid #ef5350;\n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_hapus_4)

        self.horizontalLayout_8.setStretch(0, 3)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 1)

        self.verticalLayout_10.addWidget(self.frame_16)

        self.tableWidget_4 = QTableWidget(self.scrollAreaWidgetContents_4)
        if (self.tableWidget_4.columnCount() < 5):
            self.tableWidget_4.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setStyleSheet(u"QTableWidget {\n"
"    background-color: white;\n"
"    gridline-color: #f1f5f9; \n"
"    border: none;\n"
"    font-size: 10pt;\n"
"    color: #334155;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f8fafc; \n"
"    border: none;\n"
"    border-bottom: 2px solid #e2e8f0;\n"
"    font-weight: bold;\n"
"    color: #475569;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #e0efff;\n"
"    color: #2563eb;\n"
"}")
        self.tableWidget_4.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_4.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4.verticalHeader().setVisible(False)

        self.verticalLayout_10.addWidget(self.tableWidget_4)


        self.horizontalLayout_10.addLayout(self.verticalLayout_10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)

        self.horizontalLayout_11.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.horizontalLayout_12 = QHBoxLayout(self.page_6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.scrollArea_2 = QScrollArea(self.page_6)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 861, 503))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_judul_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_judul_5.setObjectName(u"label_judul_5")
        font5 = QFont()
        font5.setFamilies([u"Arial Rounded MT"])
        font5.setBold(True)
        self.label_judul_5.setFont(font5)
        self.label_judul_5.setStyleSheet(u"QLabel {\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    color: #2f3640; /* Abu-abu gelap elegan */\n"
"    padding-bottom: 5px;\n"
"}")

        self.verticalLayout_2.addWidget(self.label_judul_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_17 = QFrame(self.scrollAreaWidgetContents)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(300, 60))
        self.frame_17.setStyleSheet(u"QFrame {\n"
"    background-color: #f9fafb; \n"
"    border: 1px solid #e5e7eb; \n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: white;\n"
"    border: 1px solid #d1d5db;\n"
"    border-radius: 8px;\n"
"    padding: 8px 12px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: white;\n"
"    border: 1px solid #d1d5db;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #2563eb;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    font-weight: bold;\n"
"}")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_13.setSpacing(15)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.input_cari_5 = QLineEdit(self.frame_17)
        self.input_cari_5.setObjectName(u"input_cari_5")
        self.input_cari_5.setMinimumSize(QSize(200, 40))

        self.horizontalLayout_13.addWidget(self.input_cari_5)

        self.combo_kategori_5 = QComboBox(self.frame_17)
        self.combo_kategori_5.addItem("")
        self.combo_kategori_5.addItem("")
        self.combo_kategori_5.addItem("")
        self.combo_kategori_5.addItem("")
        self.combo_kategori_5.setObjectName(u"combo_kategori_5")
        self.combo_kategori_5.setMinimumSize(QSize(120, 40))

        self.horizontalLayout_13.addWidget(self.combo_kategori_5)

        self.btn_tambah_5 = QPushButton(self.frame_17)
        self.btn_tambah_5.setObjectName(u"btn_tambah_5")
        self.btn_tambah_5.setEnabled(True)
        self.btn_tambah_5.setMinimumSize(QSize(180, 40))

        self.horizontalLayout_13.addWidget(self.btn_tambah_5)

        self.btn_hapus_5 = QPushButton(self.frame_17)
        self.btn_hapus_5.setObjectName(u"btn_hapus_5")
        self.btn_hapus_5.setMinimumSize(QSize(0, 40))
        self.btn_hapus_5.setStyleSheet(u"QPushButton {\n"
"    background-color: #fff5f5;    /* Latar belakang merah sangat muda */\n"
"    border: 1px solid #ff8a80;    /* Garis pinggir merah pastel */\n"
"    color: #e53935;               /* Warna teks merah cerah */\n"
"    border-radius: 6px;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ffebee;    /* Sedikit lebih gelap saat kursor lewat */\n"
"    border: 1px solid #ef5350;\n"
"}")

        self.horizontalLayout_13.addWidget(self.btn_hapus_5)

        self.horizontalLayout_13.setStretch(0, 3)
        self.horizontalLayout_13.setStretch(1, 1)
        self.horizontalLayout_13.setStretch(2, 1)

        self.verticalLayout_2.addWidget(self.frame_17)

        self.tableWidget_5 = QTableWidget(self.scrollAreaWidgetContents)
        if (self.tableWidget_5.columnCount() < 5):
            self.tableWidget_5.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setStyleSheet(u"QTableWidget {\n"
"    background-color: white;\n"
"    gridline-color: #f1f5f9; \n"
"    border: none;\n"
"    font-size: 10pt;\n"
"    color: #334155;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f8fafc;\n"
"    padding: 10px;\n"
"    border: none;\n"
"    border-bottom: 2px solid #e2e8f0;\n"
"    font-weight: bold;\n"
"    color: #475569;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #e0efff;\n"
"    color: #2563eb;\n"
"}")
        self.tableWidget_5.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_5.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_5.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_5.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_5.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tableWidget_5)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_12.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.page_6)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout = QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea_3 = QScrollArea(self.page)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 988, 486))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_header_tentang = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_header_tentang.setObjectName(u"frame_header_tentang")
        self.frame_header_tentang.setStyleSheet(u"QFrame#frame_header_tentang {\n"
"    background-color: #34495e;\n"
"    border: 2px solid #2c3e50; \n"
"    border-radius: 0px;        \n"
"}")
        self.frame_header_tentang.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_header_tentang.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_header_tentang)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(40, -1, 40, -1)
        self.label = QLabel(self.frame_header_tentang)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white;\n"
"font-size: 15px; \n"
"font-family: \"Segoe UI\";\n"
"qproperty-alignment: 'AlignCenter'; ")
        self.label.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.frame_header_tentang)

        self.frame_anggota = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_anggota.setObjectName(u"frame_anggota")
        self.frame_anggota.setStyleSheet(u"QFrame#frame_anggota {\n"
"    background-color: white;   \n"
"    border: 2px solid #dcdde1; \n"
"    border-radius: 0px;       \n"
"}\n"
"\n"
"QLabel {\n"
"    padding: 10px;\n"
"    color: #2c3e50;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLabel#label_kelompok {\n"
"    color: #2c3e50;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    font-family: \"Segoe UI\";\n"
"    qproperty-alignment: 'AlignCenter';\n"
"    border: none; \n"
"    margin-top: 10px;\n"
"}")
        self.frame_anggota.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_anggota.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_anggota)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_kelompok = QLabel(self.frame_anggota)
        self.label_kelompok.setObjectName(u"label_kelompok")
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setBold(True)
        self.label_kelompok.setFont(font6)

        self.verticalLayout_6.addWidget(self.label_kelompok)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.frame_anggota)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"margin-top: -50px; ")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_anggota)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"margin-top: -50px; ")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_anggota)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"margin-top: -50px; ")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_anggota)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"margin-top: -50px; ")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_anggota)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"margin-top: -50px; ")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)
        self.horizontalLayout_2.setStretch(4, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addWidget(self.frame_anggota)

        self.frame_foto = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_foto.setObjectName(u"frame_foto")
        self.frame_foto.setStyleSheet(u"QFrame#frame_foto {\n"
"    background-color: #243447; \n"
"    border-radius: 0px;\n"
"}")
        self.frame_foto.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_foto.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_foto)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(50)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.frame_foto)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(450, 150))
        self.label_8.setPixmap(QPixmap(u"WhatsApp Image 2026-04-09 at 12.43.08.jpeg"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.label_2 = QLabel(self.frame_foto)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(450, 150))
        self.label_2.setPixmap(QPixmap(u"WhatsApp Image 2026-04-09 at 12.43.10.jpeg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_2)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addWidget(self.frame_foto)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout.addWidget(self.scrollArea_3)

        self.stackedWidget.addWidget(self.page)

        self.horizontalLayout_9.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1155, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionactionCari.setText(QCoreApplication.translate("MainWindow", u"actionCari", None))
        self.label_9.setText("")
        self.btn_dashboard.setText(QCoreApplication.translate("MainWindow", u"\U0001f3e0 Dashboard", None))
        self.btn_stok.setText(QCoreApplication.translate("MainWindow", u"\U0001f4e6 Stok Barang", None))
        self.btn_restock.setText(QCoreApplication.translate("MainWindow", u"\u26a0\ufe0f Restock Priority", None))
        self.btn_tentang.setText(QCoreApplication.translate("MainWindow", u"\u2139\ufe0f Tentang Kami", None))
        self.label_judul_4.setText(QCoreApplication.translate("MainWindow", u"MANAJEMEN INVENTARIS GUDANG (WAREHOUSE)", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Kelola stok dan inventaris barang gudang anda", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Total Produk", None))
        self.label_total_produk_4.setText(QCoreApplication.translate("MainWindow", u"\U0001f4e6 100", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Total Unit Stok", None))
        self.label_total_stok_4.setText(QCoreApplication.translate("MainWindow", u"\U0001f4c8 200", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u" Stok Rendah", None))
        self.label_stok_rendah_4.setText(QCoreApplication.translate("MainWindow", u"\u26a0\ufe0f 1", None))
        self.input_cari_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\U0001f50d Cari nama barang atau kode SKU...", None))
        self.combo_kategori_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Semua Kategori", None))
        self.combo_kategori_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Elektronik", None))
        self.combo_kategori_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Furniture", None))
        self.combo_kategori_4.setItemText(3, QCoreApplication.translate("MainWindow", u"ATK", None))

        self.btn_tambah_4.setText(QCoreApplication.translate("MainWindow", u"Tambah Barang +", None))
        self.btn_hapus_4.setText(QCoreApplication.translate("MainWindow", u" \U0001f5d1 ", None))
        ___qtablewidgetitem = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"No", None))
        ___qtablewidgetitem1 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Kode SKU", None))
        ___qtablewidgetitem2 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nama Barang", None))
        ___qtablewidgetitem3 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Kategori", None))
        ___qtablewidgetitem4 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Stok", None))
        self.label_judul_5.setText(QCoreApplication.translate("MainWindow", u"DATA STOK GUDANG (INVENTARIS BARANG LENGKAP)", None))
        self.input_cari_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\U0001f50d Cari nama barang atau kode SKU...", None))
        self.combo_kategori_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Semua Kategori", None))
        self.combo_kategori_5.setItemText(1, QCoreApplication.translate("MainWindow", u"Elektronik", None))
        self.combo_kategori_5.setItemText(2, QCoreApplication.translate("MainWindow", u"Furniture", None))
        self.combo_kategori_5.setItemText(3, QCoreApplication.translate("MainWindow", u"ATK", None))

        self.btn_tambah_5.setText(QCoreApplication.translate("MainWindow", u"+ Tambah Barang", None))
        self.btn_hapus_5.setText(QCoreApplication.translate("MainWindow", u" \U0001f5d1 ", None))
        ___qtablewidgetitem5 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"No", None))
        ___qtablewidgetitem6 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Kode SKU", None))
        ___qtablewidgetitem7 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Nama Barang", None))
        ___qtablewidgetitem8 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Kategori", None))
        ___qtablewidgetitem9 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Stok", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Aplikasi Manajemen Gudang ini dibuat oleh Kelompok 1 untuk mempermudah pencatatan stok barang secara digital. Kami menggunakan data penting seperti Nama Barang, Kode SKU, Kategori, dan Jumlah Stok yang disimpan menggunakan sistem Doubly Linked List. Dengan sistem ini, pengelolaan data jadi lebih cepat dan ringan saat digunakan. Selain itu, ada fitur Restock Priority yang otomatis mengurutkan barang dari stok paling sedikit ke yang terbanyak, sehingga admin bisa langsung tahu barang apa yang harus segera ditambah agar tidak kehabisan stok.", None))
        self.label_kelompok.setText(QCoreApplication.translate("MainWindow", u"KELOMPOK 1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Dzaky Alfareza Zahari\n"
"G1A025005", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Aprilizza Auliya\n"
"G1A025007", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Annisa Rohiimah Sufriyani\n"
"G1A025013", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Fayola Deeba Fathinah\n"
"G1A025028", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Melzaqi Al-Faroh\n"
"G1A025035", None))
        self.label_8.setText("")
        self.label_2.setText("")
    # retranslateUi

