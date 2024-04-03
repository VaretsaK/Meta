class SingletonMeta(type):
    """
       Metaclass implementing the Singleton pattern.

       This metaclass ensures that only one instance of each class using it is created.

       Attributes:
       _instance (dict): A dictionary to store instances of classes using this metaclass.

       Returns:
       object: The instance of the class.
    """

    _instance = {}

    def __call__(cls, *args, **kwargs) -> object:
        if cls not in cls._instance:
            cls._instance[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


def main() -> None:
    """
    Main function to demonstrate the usage of a singleton metaclass.
    """

    class SingleInstance(metaclass=SingletonMeta):
        def __init__(self, name: str) -> None:
            print(f"Hello, {name}!")
            self.name = name

    inst_1 = SingleInstance("Dave")
    inst_2 = SingleInstance("Mark")
    print(inst_2.name)
    print(inst_1.name)


if __name__ == "__main__":
    main()
