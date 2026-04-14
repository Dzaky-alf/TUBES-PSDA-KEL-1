import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QMessageBox, QHeaderView
from PySide6.QtCore import Qt
from ui_main import Ui_MainWindow               
from ui_dialog_tambah import Ui_Dialog as Ui_DialogTambah 
from ui_dialog_update import Ui_Dialog as Ui_DialogUpdate 
from TubesKel1 import DoublyLinkedList

class DialogTambah(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogTambah()
        self.ui.setupUi(self)
        self.ui.btn_batal_baru.clicked.connect(self.reject)
        self.ui.btn_simpan_baru.clicked.connect(self.accept)

class DialogUpdate(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogUpdate()
        self.ui.setupUi(self)
        self.ui.btn_batal_update.clicked.connect(self.reject)
        self.ui.btn_simpan_update.clicked.connect(self.accept)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.inventory = DoublyLinkedList()
        
        # --- 1. DATA AWAL (DEMO) ---
        self.siapkan_data_demo()
        
        # --- 2. NAVIGASI ---
        self.ui.btn_dashboard.clicked.connect(self.show_dashboard)
        self.ui.btn_stok.clicked.connect(self.show_stok_page)
        self.ui.btn_tentang.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        
        # --- 3. FILTER KATEGORI ---
        # Menambahkan kategori banyak-banyak sesuai permintaan
        kategori_opsi = ["Semua Kategori", "Elektronik", "Aksesoris", "Kabel", "Furnitur", "Jaringan", "ATK", "Makanan", "Minuman"]
        
        self.ui.combo_kategori_4.clear()
        self.ui.combo_kategori_4.addItems(kategori_opsi)
        self.ui.combo_kategori_4.currentTextChanged.connect(self.filter_kategori_dashboard)
        
        self.ui.combo_kategori_5.clear()
        self.ui.combo_kategori_5.addItems(kategori_opsi)
        self.ui.combo_kategori_5.currentTextChanged.connect(self.filter_kategori_stok)
        
        # --- 4. SEARCH ---
        self.ui.input_cari_4.textChanged.connect(self.cari_data)
        self.ui.input_cari_5.textChanged.connect(self.cari_data)
        
        # --- 5. TOMBOL OPERASI ---
        self.ui.btn_tambah_5.clicked.connect(self.buka_dialog_tambah)
        self.ui.btn_tambah_4.clicked.connect(self.buka_dialog_update_publish)
        self.ui.btn_restock.clicked.connect(self.urutkan_priority_dashboard) # Tombol Restock
        
        self.ui.btn_hapus_4.clicked.connect(self.hapus_data) 
        self.ui.btn_hapus_5.clicked.connect(self.hapus_data) 
        
        # Setting Tabel agar bisa pilih banyak baris
        self.ui.tableWidget_4.setSelectionMode(self.ui.tableWidget_4.SelectionMode.ExtendedSelection)
        self.ui.tableWidget_5.setSelectionMode(self.ui.tableWidget_5.SelectionMode.ExtendedSelection)
        
        # Jalankan Dashboard di awal
        self.show_dashboard()

    def siapkan_data_demo(self):
        """Memasukkan 8 data awal ke dalam sistem"""
        data_awal = [
            ("LAP-AZ-001", "Laptop Asus Zenbook", "Elektronik", 5),
            ("MOU-LG-022", "Mouse Logitech G304", "Aksesoris", 45),
            ("MON-SS-010", "Monitor Samsung 24\"", "Elektronik", 8),
            ("KYB-RG-005", "Keyboard Mechanical", "Aksesoris", 12),
            ("CAB-HD-099", "Kabel HDMI 2 Meter", "Kabel", 60),
            ("CHR-SL-003", "Kursi Gaming Secretlab", "Furnitur", 3),
            ("TAB-WD-012", "Meja Kerja Minimalis", "Furnitur", 15),
            ("NET-TP-044", "Router TP-Link AX10", "Jaringan", 7)
        ]
        for sku, nama, kat, stok in data_awal:
            self.inventory.insert(sku, nama, kat, stok)

    # ================= LOGIKA TAMPILAN =================

    def show_dashboard(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_5)
        self.refresh_ui_dashboard()

    def show_stok_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_6)
        self.refresh_ui_stok()

    def refresh_ui_dashboard(self, data_list=None):
        if data_list is None:
            all_data = self.inventory.display()
            # SKU, Nama, Kat, Stok_Dashboard (index 5)
            data_list = [[d[0], d[1], d[2], d[5]] for d in all_data if d[4] == "Published"]
        
        self.isi_tabel(self.ui.tableWidget_4, data_list)
        
        # --- LOGIKA STATISTIK ---
        total_p = len(data_list)
        total_s = sum(int(i[3]) for i in data_list)
        # Hitung Stok Rendah (1-9)
        stok_rendah = len([i for i in data_list if 0 < int(i[3]) < 10])

        self.ui.label_total_produk_4.setText(str(total_p))
        self.ui.label_total_stok_4.setText(str(total_s))
        self.ui.label_stok_rendah_4.setText(str(stok_rendah))

    def refresh_ui_stok(self, data_list=None):
        if data_list is None:
            all_data = self.inventory.display()
            data_list = [[d[0], d[1], d[2], d[3]] for d in all_data]
        self.isi_tabel(self.ui.tableWidget_5, data_list)

    def isi_tabel(self, tabel, data_list):
        tabel.setRowCount(len(data_list))
        
        # --- PENGATURAN LEBAR KOLOM ---
        header = tabel.horizontalHeader()
        
        # Kolom No (tetap kecil)
        tabel.setColumnWidth(0, 40)
        header.setSectionResizeMode(0, QHeaderView.Fixed)
        
        # Kolom Nama Barang (dibuat Stretch agar mengambil sisa ruang)
        header.setSectionResizeMode(2, QHeaderView.Stretch) 
        
        # Kolom Stok (index ke-4) dibuat mengecil pas dengan isi
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents) 

        # Mengisi data ke tabel
        for row, data in enumerate(data_list):
            item_no = QTableWidgetItem(str(row + 1))
            item_no.setTextAlignment(Qt.AlignCenter)
            tabel.setItem(row, 0, item_no)
            for col, val in enumerate(data):
                item = QTableWidgetItem(str(val))
                item.setTextAlignment(Qt.AlignCenter)
                tabel.setItem(row, col + 1, item)

    # ================= FILTER & SEARCH =================

    def filter_kategori_dashboard(self, kat):
        all_data = self.inventory.display()
        pub = [[d[0], d[1], d[2], d[5]] for d in all_data if d[4] == "Published"]
        res = pub if kat == "Semua Kategori" else [d for d in pub if d[2] == kat]
        self.refresh_ui_dashboard(res)

    def filter_kategori_stok(self, kat):
        all_data = self.inventory.display()
        stk = [[d[0], d[1], d[2], d[3]] for d in all_data]
        res = stk if kat == "Semua Kategori" else [d for d in stk if d[2] == kat]
        self.refresh_ui_stok(res)

    def cari_data(self):
        keyword = self.sender().text()
        hasil = self.inventory.search(keyword)
        if self.ui.stackedWidget.currentWidget() == self.ui.page_5:
            res = [[h[0], h[1], h[2], h[5]] for h in hasil if h[4] == "Published"]
            self.refresh_ui_dashboard(res)
        else:
            res = [[h[0], h[1], h[2], h[3]] for h in hasil]
            self.refresh_ui_stok(res)

    # ================= OPERASI DATA =================

    def urutkan_priority_dashboard(self):
        """Logika Khusus Kelompok 1: Sort stok paling sedikit & pindah ke Dashboard"""
        all_data = self.inventory.display()
        pub = [[d[0], d[1], d[2], d[5]] for d in all_data if d[4] == "Published"]
        
        # Urutkan
        sorted_data = sorted(pub, key=lambda x: int(x[3]))
        
        # Pindah halaman ke Dashboard otomatis
        self.show_dashboard()
        
        # Tampilkan hasil urutan
        self.refresh_ui_dashboard(sorted_data)

    def buka_dialog_tambah(self):
        dialog = DialogTambah(self)
        if dialog.exec():
            sku = dialog.ui.txt_sku_baru.text()
            nama = dialog.ui.txt_nama_baru.text()
            kat = dialog.ui.txt_kategori_baru.text()
            stok = dialog.ui.input_stok_baru.value()
            if sku and nama:
                self.inventory.insert(sku, nama, kat, int(stok))
                self.refresh_ui_stok()

    def buka_dialog_update_publish(self):
        dialog = DialogUpdate(self)
        if dialog.exec():
            sku = dialog.ui.txt_sku_update.text()
            jml = dialog.ui.input_jumlah_masuk.value()
            curr = self.inventory.head
            while curr:
                if curr.sku == sku:
                    if curr.stok >= jml:
                        curr.stok -= jml
                        curr.stok_dashboard += jml
                        curr.status = "Published"
                        self.refresh_ui_dashboard()
                        self.refresh_ui_stok()
                        return
                    else:
                        QMessageBox.warning(self, "Gagal", "Stok gudang tidak cukup!")
                        return
                curr = curr.next
            QMessageBox.warning(self, "Gagal", "SKU tidak ditemukan!")

    def hapus_data(self):
        is_dash = self.ui.stackedWidget.currentWidget() == self.ui.page_5
        tabel = self.ui.tableWidget_4 if is_dash else self.ui.tableWidget_5
        indices = tabel.selectionModel().selectedRows()
        if not indices: return
        
        rows = sorted([i.row() for i in indices], reverse=True)
        if is_dash:
            if QMessageBox.question(self, "Konfirmasi", "Tarik kembali ke Gudang?") == QMessageBox.Yes:
                for r in rows:
                    sku = tabel.item(r, 1).text()
                    curr = self.inventory.head
                    while curr:
                        if curr.sku == sku:
                            curr.stok += curr.stok_dashboard
                            curr.stok_dashboard = 0
                            curr.status = "Draft"
                            break
                        curr = curr.next
        else:
            if QMessageBox.question(self, "Konfirmasi", "Hapus data permanen?") == QMessageBox.Yes:
                for r in rows:
                    self.inventory.delete(tabel.item(r, 1).text())
        
        self.refresh_ui_dashboard()
        self.refresh_ui_stok()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())