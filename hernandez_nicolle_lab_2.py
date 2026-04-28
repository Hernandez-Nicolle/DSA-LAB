class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        
head = None

def traverseLinkedList():
    current = head
    while(current):
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def insertNodeAtTheBeggining(data):
    global head 
    newNode = Node(data)
    
    if(head == None):
        head = newNode
    else:
        newNode.next = head
        head = newNode
        
def insertNodeAtTheEnd(data):
    global head
    newNode = Node(data)
    
    if(head == None):
        head = newNode
        return
    else: 
        current = head 
        while(current.next != None):
            current = current.next
        current.next = newNode
        
def insertNodeafterGivenNode(data, node):
    global head
    newNode = Node(data)
    
    if(head == None):
        head = newNode
    else:
        current = head.next
        prev = head
        
        while(prev.data != node):
            prev = current
            current = current.next
        
            if(current == None):
                print("The node does not exist")
                return
            
    newNode.next = current
    prev.next = newNode


node1 = Node("pahina by cup of joe")
head = node1

insertNodeAtTheBeggining("mean it by lany")
insertNodeAtTheBeggining("24k magic by Bruno Mars")
insertNodeAtTheBeggining("Ale by The Bloomfields")

insertNodeAtTheEnd("Backburner by Niki")
insertNodeAtTheEnd("The only Exception")

insertNodeafterGivenNode("confident by justin bieber", "Ale by The Bloomfields")

traverseLinkedList()
