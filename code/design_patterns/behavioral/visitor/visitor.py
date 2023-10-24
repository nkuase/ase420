# interface
class Visitable(object):
  def accept(self, visitor): pass
class Visitor(object):
  def visit(self, element): pass

# Implementations
class Room(Visitable):
    def __init__(self, size):
        self.size = size
    def accept(self, visitor):
        visitor.visitRoom(self)
 
class House(Visitable):
    def __init__(self, roomSizes):
        self.rooms = []
        for roomSize in roomSizes:
            room = Room(roomSize)
            self.rooms.append(room)

    def accept(self, visitor):
        visitor.visit(self)

class Visitor(Visitor):
    def __init__(self):
        self.totalSize = 0

    def visit(self, house):
        self.totalSize = 0 # make sure the initial size is 0
        # get the size of rooms
        for room in house.rooms:
            room.accept(self)
    def visitRoom(self, room): # should have been visit with Java
        self.totalSize += room.size

# Driver

roomSizes = [200, 300, 500]
kitchenSize = 400
house = House(roomSizes)
visitor = Visitor()
visitor.visit(house)

print(visitor.totalSize) # 200 + 300 + 500 = 1000
