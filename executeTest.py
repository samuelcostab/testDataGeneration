if __name__ == '__main__':
    from ast_walker import *
    from runner import *
    import foo

    elem = dir(foo)
    n_ele = []
    print(elem)
    for i in elem:
        if callable(getattr(foo, i)):
            print(type(getattr(foo, i).__name__))
            '''coloca o nome da funcao a ser testada '''
            if getattr(foo, i).__name__ == "insertionSort": 
                n_ele.append(getattr(foo, i))

    test_result = ""

    for j in n_ele:
        print(j.__name__)
        runner(j, "if __name__ == " + "'__main__'" + ":" + "\n\t" +
               "print (" + j.__name__ + '(' + str("") + '))', test_result, j.__name__)
