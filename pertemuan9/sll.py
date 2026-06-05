class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_list(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def delete_list(self, data):
        temp = self.head
        prev = None
        
        while temp:
            if temp.data == data:
                if prev is None: # Jika yang dihapus adalah head
                    self.head = temp.next
                else: # Jika yang dihapus di tengah atau akhir
                    prev.next = temp.next
                print(f"Data {data} berhasil dihapus")
                return # Keluar fungsi setelah berhasil
            prev = temp
            temp = temp.next
        print(f"Data {data} tidak ditemukan")

    def search_list(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

ll = LinkedList()
ll.add_list(30)
ll.add_list(20)
ll.add_list(10)

print("Cetak LinkedList Awal:")
ll.display()

# Contoh Pencarian
print(f"Cari 20: {'Ditemukan' if ll.search_list(20) else 'Tidak ada'}")

# Contoh Penghapusan
ll.delete_list(10)
print("Cetak LinkedList Setelah Dihapus:")
ll.display()