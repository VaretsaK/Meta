class RenameAttr(type):
    """
        Metaclass that renames attributes of a class.

        This metaclass modifies the attributes of a class by prepending "__private" to the names of attributes
        that are specific to the class (i.e., attributes whose names start with an underscore followed by the class name).

        Attributes:
        clsname (str): The name of the class being created.
        superclasses (tuple): The tuple of superclasses of the class being created.
        attributedict (dict): The dictionary of attributes of the class being created.

        Returns:
        object: The instance of the class.
    """

    def __new__(cls, clsname: str, superclasses: tuple, attributedict: dict) -> object:
        """
        Create a new instance of the class with modified attribute names.

        Parameters:
        clsname (str): The name of the class being created.
        superclasses (tuple): The tuple of superclasses of the class being created.
        attributedict (dict): The dictionary of attributes of the class being created.

        Returns:
        object: The instance of the class.
        """

        attributedict = {"__private" + item[len(clsname) + 2:] if item.startswith(f"_{clsname}") else item: value
                         for item, value in attributedict.items()}

        print("Class name:", clsname)
        print("Superclasses:", superclasses)
        print("Attributes:", attributedict)

        return type.__new__(cls, clsname, superclasses, attributedict)


def main() -> None:
    """
    Main function to demonstrate the usage of a RenameAttr metaclass.
    """

    class NewClass(metaclass=RenameAttr):
        four = 4
        _one = 1
        __two = 2

    print(NewClass.__private_two)


if __name__ == "__main__":
    main()
