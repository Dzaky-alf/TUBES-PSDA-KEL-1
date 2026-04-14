class Node:
    def __init__(self, sku, nama, kategori, stok):
        self.sku = sku
        self.nama = nama
        self.kategori = kategori
        self.stok = int(stok)           
        self.stok_dashboard = 0         
        self.status = "Draft"
        self.next = None
        self.prev = None

    def to_list(self):
        return [self.sku, self.nama, self.kategori, self.stok, self.status, self.stok_dashboard]

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, sku, nama, kategori, stok):
        new_node = Node(sku, nama, kategori, stok)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        return True

    def delete(self, sku):
        curr = self.head
        while curr:
            if curr.sku == sku:
                if curr.prev: curr.prev.next = curr.next
                else: self.head = curr.next
                if curr.next: curr.next.prev = curr.prev
                else: self.tail = curr.prev
                return True
            curr = curr.next
        return False

    def display(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.to_list())
            curr = curr.next
        return res

    def search(self, keyword):
        res = []
        curr = self.head
        k = keyword.lower()
        while curr:
            if k in curr.nama.lower() or k in curr.sku.lower():
                res.append(curr.to_list())
            curr = curr.next
        return res