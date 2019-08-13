class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None
    

    def appendToLast(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node


    def printList(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def appendToMiddleOfNodes(self, prev_node, data):

        if not prev_node:
            print("No Previous Node Found")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    

    def deleteNodeFromStart(self):
            self.head = self.head.next
    
    def deleteNodeInBetween(self, prev_node_data):
        cur_node = self.head
        prev = None

        while cur_node and cur_node.data != prev_node_data:
            prev = cur_node
            cur_node = cur_node.next
        
        if(cur_node is None):
            return
        else:
            prev.next = cur_node.next
            cur_node = None
            
         

llist = LinkList()

llist.appendToLast("L")
llist.appendToLast("I")
llist.appendToLast("N")
llist.appendToLast("K")
#llist.prepend("Q")
llist.appendToMiddleOfNodes(llist.head.next.next, "W")
llist.deleteNodeInBetween("I")
llist.printList()
