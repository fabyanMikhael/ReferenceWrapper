from __future__ import annotations
from typing import Generic, TypeVar

U = TypeVar('U')

class __tmp__:
    '''dont use this.'''
    @staticmethod
    def load(id): raise NotImplementedError("please add a constant TYPE = your_class for the Reference class!")

class Reference(Generic[U]):
    TYPE : U = __tmp__
    REFERENCES : dict[str,Reference]
    __ALLOWED_TO_ACCESS__ = ["__referencing__", "__id__", "TYPE", "__Accessed_Attribute__", "REFERENCES", "ToDict", "FromDict", "__dict__", "__eq__"]
    __ALLOWED_TO_MODIFY__ = ["__referencing__", "__id__", "TYPE", "__Accessed_Attribute__", "REFERENCES", "ToDict", "__dict__"]

    def __init_subclass__(cls, scm_type=None, name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.REFERENCES = {}

    def __init__(self, __id__) -> None:
        __id__ = str(__id__)
        self.__referencing__ = None
        self.__id__ = __id__
        self.REFERENCES[__id__] = self

    def __repr__(self) -> str:
        self.__Accessed_Attribute__()
        return self.__referencing__.__repr__()
    
    def __eq__(self, o: object) -> bool:
        self.__Accessed_Attribute__()
        return self.__referencing__ == o

    def __str__(self) -> str:
        self.__Accessed_Attribute__()
        return self.__referencing__.__str__()

    def __getattribute__(self, name: str):
        if name in Reference.__ALLOWED_TO_ACCESS__:
            return object.__getattribute__(self, name)
        self.__Accessed_Attribute__()
        return object.__getattribute__(self.__referencing__, name)
    
    def __setattr__(self, name: str, value) -> None:
        if name in Reference.__ALLOWED_TO_MODIFY__:
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
    def pop(cls, id) -> None:
        id = str(id)
        if id in cls.REFERENCES:
            cls.REFERENCES[id].__referencing__ = None

    @classmethod
    def Get(cls, id) -> U:
        id = str(id)
        if id in cls.REFERENCES:
            return cls.REFERENCES[id]
        return cls(__id__=id)