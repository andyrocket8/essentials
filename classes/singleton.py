from typing import Generic
from typing import Optional
from typing import Type
from typing import TypeVar

T = TypeVar('T', bound='Singleton', covariant=True)
TypeT = Type[T]


class Singleton(Generic[T]):
    # Singleton class based on simple inheritance
    # Attention: __init__ of inherited class called on each instantiation
    _instances: dict[str, T] = dict()

    def __new__(cls: TypeT, *args, **kwargs) -> 'Singleton':
        instance: Optional[T] = cls._instances.get(cls.__name__)
        if instance is None:
            instance = super().__new__(cls, *args, **kwargs)
            cls._instances[cls.__name__] = instance
        return instance


class SingletonMeta(type, Generic[T]):
    # Singleton based on Meta class
    _instances: dict[str, T] = dict()

    def __call__(cls: TypeT, *args, **kwargs) -> T:
        instance: Optional[T] = cls._instances.get(cls.__name__)
        if instance is None:
            instance = type.__call__(cls, *args, **kwargs)
            cls._instances[cls.__name__] = instance
        return instance
