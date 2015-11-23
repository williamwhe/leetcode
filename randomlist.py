class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

def copyl(head):
    if head is None:
        return None
    nodes=[]
    nodemap={}
    pos=0
    while head is not None:
        nodes.append(head)
        nodemap[id(head)]=pos
        pos+=1
        head=head.next
    rand=[]
    for n in nodes:
        if n.random is None:
            rand.append(None)
        else:
            rand.append(nodemap[id(n.random)])
    newnodes=[]
    for i in range(len(nodes)):
        n=RandomListNode(nodes[i].label)
        newnodes.append(n)
    for i in range(len(nodes)-1):
        newnodes[i].next=newnodes[i+1]
    newnodes[-1].next=None
    for i in range(len(newnodes)):
        if rand[i] is None:
            newnodes[i].random=None
        else:
            newnodes[i].random=newnodes[rand[i]]
    return newnodes[0]

def printl(head):
    while head is not None:
        print head.label,
        head=head.next
    print

def makel(arr):
    head=None
    for i in range(len(arr)-1,-1,-1):
        n=RandomListNode(arr[i])
        if head is None:
            head=n
        else:
            n.next=head
            n.random=head
            head=n
    return head

a=[-1]
l=makel(a)
printl(l)
l2=copyl(l)
printl(l2)