list1 = []
list2 = []

length = 0

def add():
    ch = int(input("Enter List To Add 1 or 2"))
    a = int(input("Enter Element:-"))
    if ch == 1:
        list1.append(a)
    else:
        list2.append(a)

def remove():
    a = int(input("Enter Element To Be Deleted"))
    list1.remove(a)
    print(list1)


def search():
    
    ch = int(input("Enter List To Add 1 or 2"))
    a = int(input("Enter Element To Be Searched:-"))
    if ch == 1:
        if a in list1:
            print("Elemnt Is Present In List")
        else:
            print("Elemnt Is Not Present in List")
    else:
        if a in list2:
            print("Elemnt Is Present In List")
        else:
            print("Elemnt Is Not Present in List")
        
        
def len1():
    print("List Of Length Is", len(list))
    

def intesect():
    ins = list(set(list1).intersection(list2))
    print("Intersection Is ", ins)
    

def union():
    uni = list(set(list1).union(list2))
    print("Union Is:-",uni)
    

def diff():
    diff = list(set(list1).difference(list2))
    

def subsets():
    sub = list(set(list1).issubset(list2))
    
while True:
    print("\n1.Add\n2.Remove\n3.Search\n4.Size Of List\n5.Intersection \n6.Union \n7.Diffrence \n8.Subset")
    
    a = int(input("Enter Choice"))
    
    if a == 1:
        add()
    elif a == 2:
        remove()
    elif a == 3:
        search()
    elif a == 4:
        len1()
    elif a == 5:
        intesect()
    elif a == 6:
        union()
    elif a == 7:
        diff()
    elif a == 8:
        subsets()