# ReferenceWrapper
a python module that lets you wrap a class and control references to it

# why?
* Able to `retrieve` user defined `objects` (such as `player` objects) from `anywhere` in your `code` 
* `Caches` the `objects` by default 
* You can `save` and `delete` the `objects` without worrying about it being `held` by any `other objects`
* It makes it `possible` to easily `serialize` into `json` format even if there are `circular references`
* `lazy loads` the objects once an `attribute` is `accessed`
* Works with using [Auto-Json😉](https://github.com/fabyanMikhael/Auto-Json)

# usage
Add a static method with `@staticmethod` decorator called `load` that takes in a `parameter` of `id`. \
The method should `return` an `instance object` of the class by `loading` `data` somewhere with the provided `id`
```py
from ReferenceModule import Reference

class Example:

  def Hi(self) -> None: print("hello!")
  
  @staticmethod
  def load(id) -> Example:
    # make an object of type *Example*
    return Example()
    
class ExampleReference(Reference[Example]): TYPE = Example
```
Now you can get an instance by calling: 
```py
instance = ExampleReference.Get(id=1) # instance will act as a type of Example
```
The typechecker should also think that the type is `Example` instead of `ExampleReference`
```py
instance.Hi()
```

# example

```py
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

class PlayerReference(Reference[player]): TYPE = player

PlayerRef1 : player = PlayerReference.Get(id=1)
PlayerRef2 : player = PlayerReference.Get(id=1)
PlayerReference.Get(id=1)
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
```
