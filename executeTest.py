if __name__ == '__main__':
    from ast_walker import *
    from runner import *
    import gcd

    elem = dir(gcd)
    n_ele = []
    for i in elem:
        if callable(getattr(gcd, i)):
            if getattr(gcd, i).__name__ != sys.argv[0]:
                n_ele.append(getattr(gcd, i))

    test_result = ""

    for j in n_ele:
        print(j.__name__)
        runner(j, "if __name__ == " + "'__main__'" + ":" + "\n\t" +
               "print (" + j.__name__ + '(' + str("") + '))', test_result, j.__name__)
