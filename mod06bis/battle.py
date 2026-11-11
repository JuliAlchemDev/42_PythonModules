import ex3


def main():
    factory = ex3.FlameFactory()
    print("Testing factory")
    print(factory.create_base().describe())
    print(factory.create_base().attack())
    print(factory.create_evolved().describe())
    print(factory.create_evolved().attack())
    print()
    # factory = FlameFactory()
    print("Testing factory")
    factory = ex3.TransformCreatureFactory()
    print(factory.create_base().describe())
    print(factory.create_base().attack())
    print(factory.create_evolved().describe())
    print(factory.create_evolved().attack())


if __name__ == "__main__":
    main()
    # import sys
    # print(sys.modules)

    # import sys
    # import ex3

    # print(dir(sys.modules["ex3.factories"]))
