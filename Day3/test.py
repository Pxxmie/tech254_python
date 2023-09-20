def multi_args(*multiargs):
    for arg in multiargs:
        print(arg)
    # print(type(multiargs))


multi_args(1, 2, 3, 4, 5, "six")
