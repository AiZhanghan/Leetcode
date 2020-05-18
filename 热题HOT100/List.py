class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class List:
    def __init__(self, head=None):
        self.head = head
    
    def built(self, val_list):
        if val_list:
            self.head = ListNode(val_list[0])
            cur = self.head
            for i in range(1, len(val_list)):
                cur.next = ListNode(val_list[i])
                cur = cur.next
    
    def print(self):
        cur = self.head
        while cur:
            print("%s->" % cur.val, end="")
            cur = cur.next
        print("None")


if __name__ == "__main__":
    a = List()
    a.built([1, 2, 3, 4, 5])
    a.print()
            