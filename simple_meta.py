class PrintGreet(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print("Greetings!")
        print("Name:", clsname)
        print("Superclasses:", superclasses)
        print("Attributes:", attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)


class New(metaclass=PrintGreet):
    ...
