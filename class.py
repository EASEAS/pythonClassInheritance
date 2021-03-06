import time
import hashlib

###############################################################################
# Abstractions with Inheritance
###############################################################################
class world():
    def __init__(self):
        h = hashlib.sha1(str(time.time_ns()).encode()).hexdigest()
        self.ID = h
        self.objects = []
        self.objectID = 0 
    def __iter__(self):
        return iter(self.objects)
    def __reversed__(self):
        return reversed(self.objects)
    def addObject(self,objectToAdd):
        self.objectID = self.objectID + 1
        objectToAdd.id = self.objectID
        self.objects.append(objectToAdd)
class objects():
    def __init__(self,worldContext):
        if (worldContext == None):
            worldContext = world()
        self.world = worldContext
        self.world.addObject(self)
class A(objects):
    def __init__(self,worldContext = None):
        super().__init__(worldContext)
                self.l = [0,1,2,3,4,5,7,8,9]
class B(A):
    def __init__(self,worldContexti = None):
        super().__init__(worldContext)
        self.l = [ x+10 for x in self.l]
###############################################################################
# Mixins with Inheritance
###############################################################################
class C(object):
    def __init__(self):
        super(C, self).__init__()
        self.C = 1
class D(object):
    def __init__(self):
        super(D, self).__init__()
        self.D = 10
class E(C,D):
    def __init__(self):
        super(E, self).__init__()
        if hasattr(self,'C') and hasattr(self,'D') :
            print('Object e instance has inheritance of both C and D')
        else:
            print('Inheritance failed')
# Mixin Inheritance
e = E()

#Abstractions with Inheritance
w = world()
a = A(w)
b = B(w)

#check that inheritance is correct by printing IDs then creating a new object
print(''.join(["\nWorld id = ",str(w.ID)]))
for obj in w:
    print( ''.join(["list = ", str(obj.l),',\n ID = ',str(obj.id)] ) )

w = world()
print(''.join(["\nWorld id = ",str(w.ID)]))
for obj in w:
    print( ''.join(["list = ", str(obj.l),',\n ID = ',str(obj.id)] ) )

