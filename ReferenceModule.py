from __future__ import annotations
class __tmp__:
    '''dont use this.'''
    @staticmethod
    def load(id): raise NotImplementedError("please add a constant TYPE = your_class for the Reference class!")

class Reference(object):
    TYPE = __tmp__
    REFERENCES : dict[str,Reference] = {}
    def __init__(self, id) -> None:
        self.__referencing__ = None
        self.__id__ = id
        self.REFERENCES[id] = self

    def __repr__(self) -> str:
        self.__Accessed_Attribute__()
        return self.__referencing__.__repr__()

    def __str__(self) -> str:
        self.__Accessed_Attribute__()
        return self.__referencing__.__str__()

    def __getattribute__(self, name: str):
        if name in ["__referencing__", "__id__", "TYPE", "__Accessed_Attribute__", "REFERENCES", "__clear__"]:
            return object.__getattribute__(self, name)
        self.__Accessed_Attribute__()
        return object.__getattribute__(self.__referencing__, name)
    
    def __setattr__(self, name: str, value) -> None:
        if name in ["__referencing__", "__id__", "TYPE"]:
            object.__setattr__(self, name, value)
            return
        self.__Accessed_Attribute__()
        object.__setattr__(self.__referencing__, name, value)

    def __Accessed_Attribute__(self):
        if self.__referencing__ == None:
            self.__referencing__ = self.TYPE.load(id=self.__id__)

    @classmethod
    def __clear__(cls):
        for ref in cls.REFERENCES:
            ref = cls.REFERENCES[ref]
            ref.__referencing__ = None

    @classmethod
    def Get(cls, id) -> TYPE:
        if id in cls.REFERENCES:
            return cls.REFERENCES[id]
        return cls(id=id)