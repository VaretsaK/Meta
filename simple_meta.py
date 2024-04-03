class PrintGreet(type):
    def __new__(cls, clsname: str, superclasses: tuple, attributedict: dict) -> "PrintGreet":
        """
            Metaclass that prints greetings and information when a new class is created.

            Attributes:
            clsname (str): The name of the class being created.
            superclasses (tuple): The tuple of superclasses of the class being created.
            attributedict (dict): The dictionary of attributes of the class being created.

            Returns:
            Type[type]: The newly created class.
        """
        print("Greetings!")
        print("Name:", clsname)
        print("Superclasses:", superclasses)
        print("Attributes:", attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)


def main() -> None:
    """
    Main function to demonstrate the usage of a simple metaclass.
    """

    class New(metaclass=PrintGreet):
        ...


if __name__ == "__main__":
    main()
