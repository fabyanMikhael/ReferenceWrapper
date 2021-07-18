from __future__ import annotations
from ReferenceModule import Reference
class player:
    def __init__(self, id) -> None:
        self.health = 10
        self.damage = 1
        self.id = id

    def __repr__(self) -> str:
        return f"ID: {self.id} -- health: {self.health} , damage: {self.damage}"
    
    @staticmethod
    def load(id):
        # You would load the player from a database here...
        return player(id=id)

class PlayerReference(Reference): TYPE = player

PlayerRef1 : player = PlayerReference.Get(id=1)
PlayerRef2 : player = PlayerReference.Get(id=1)

print("\nOriginal: \n")
print("PlayerRef 1: ", PlayerRef1)
print("PlayerRef 2: ", PlayerRef2)

print("\nmodifying...\n")
PlayerRef1.health = 5
print("PlayerRef 1: ", PlayerRef1)
print("PlayerRef 2: ", PlayerRef2)

print("\nclearing...\n")
PlayerReference.__clear__()
print("PlayerRef 1: ", PlayerRef1)
print("PlayerRef 2: ", PlayerRef2)