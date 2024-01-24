from classes.singleton import Singleton
from classes.singleton import SingletonMeta

sc_init_usages = 0


class SingletonClassOne(Singleton):
    def __init__(self):
        global sc_init_usages
        sc_init_usages += 1
        print('Instantiating class', self.__class__.__name__)


class SingletonClassTwo(Singleton):
    def __init__(self):
        global sc_init_usages
        sc_init_usages += 1
        print('Instantiating class', self.__class__.__name__)


class SingletonClassTwoDerived(SingletonClassTwo):
    def __init__(self):
        global sc_init_usages
        sc_init_usages += 1
        super().__init__()


def test_singleton_class():
    sc_1_1 = SingletonClassOne()
    sc_1_2 = SingletonClassOne()
    assert id(sc_1_1) == id(sc_1_2), 'SingletonClassOne instances must be the same object'
    sc_2_1 = SingletonClassTwo()
    sc_2_2 = SingletonClassTwo()
    assert id(sc_2_1) == id(sc_2_2), 'SingletonClassTwo instances must be the same object'
    assert id(sc_1_1) != id(
        sc_2_1
    ), 'SingletonClassOne instance and SingletonClassTwo instance must be different objects'
    sc_2_d_1 = SingletonClassTwoDerived()
    sc_2_d_2 = SingletonClassTwoDerived()
    assert id(sc_2_d_1) == id(sc_2_d_2), 'SingletonClassTwoDerived instances must be the same object'
    assert id(sc_2_d_1) != id(
        sc_2_1
    ), 'SingletonClassTwoDerived instance and SingletonClassTwo instance must be different objects'


sm_init_usages = 0


class SingletonMetaOne(metaclass=SingletonMeta):
    def __init__(self, *args):
        global sm_init_usages
        sm_init_usages += 1
        print(f'Constructor of {self.__class__.__name__} invoked, args: {args}')


class SingletonMetaTwo(metaclass=SingletonMeta):
    def __init__(self, *args):
        global sm_init_usages
        sm_init_usages += 1
        print(f'Constructor of {self.__class__.__name__} invoked, args: {args}')


class SingletonMetaTwoDerived(SingletonMetaTwo):
    def __init__(self, *args):
        global sm_init_usages
        sm_init_usages += 1
        super().__init__(*args)
        self.usage_count = sm_init_usages


def test_singleton_meta_class():
    global sm_init_usages
    sm_1_1 = SingletonMetaOne(1)
    sm_1_2 = SingletonMetaOne()
    sm_1_3 = SingletonMetaOne()
    assert id(sm_1_1) == id(sm_1_2), 'SingletonMetaOne instances must be the same object'
    assert id(sm_1_2) == id(sm_1_3), 'SingletonMetaOne instances must be the same object, third instance'
    assert sm_init_usages == 1, 'Excepting one __init__ call on SingletonMetaOne creations'
    sm_init_usages = 0
    sm_2_1 = SingletonMetaTwo(2)
    sm_2_2 = SingletonMetaTwo()
    assert sm_init_usages == 1, 'Excepting one __init__ call on SingletonMetaTwo creations'
    assert id(sm_2_1) == id(sm_2_2), 'SingletonMetaTwo instances must be the same object'
    assert id(sm_1_1) != id(sm_2_1), 'SingletonMetaOne instance and SingletonMetaTwo instance must be different objects'
    sm_init_usages = 0
    sm_2_d_1 = SingletonMetaTwoDerived(3)
    sm_2_d_2 = SingletonMetaTwoDerived()
    assert sm_init_usages == 2, 'Excepting one __init__ call on SingletonMetaTwoDerived creations'
    assert id(sm_2_d_1) == id(sm_2_d_2), 'SingletonMetaTwoDerived instances must be the same object'
    assert id(sm_2_1) != id(
        sm_2_d_1
    ), 'SingletonMetaTwo instance and SingletonMetaTwoDerived instance must be different objects'
    assert sm_2_d_1.usage_count == 2, 'usage_count of SingletonMetaTwoDerived must be equal to 2'
    assert 'usage_count' not in sm_2_1.__dict__, 'SingletonMetaTwo should not have usage_count attribute'
