def dataGenerator(dataGraph, abstracTree):
    '''paths, nodes = dataGraph

    print('\n\npaths:', paths)
    print('\nnodes:', nodes)'''

    interpreterAbstractTree(abstracTree)

    '''pathAcurracy, pathsFind = paths
    for node in pathsFind[0]:
        generatorDataPerNode(node, nodes)'''

    '''i = 1
    for path in pathsFind:
        print('path',i)
        for node in path:
            generatorDataPerNode(node, nodes)
        i += 1'''


def generatorDataPerNode(node, nodeList):
    node = nodeList[node]['label'].split('\n')

    print('\n\nnode:', node)


def interpreterAbstractTree(tree):
    treeSplit = tree.split('()')
    for e in treeSplit:
        print('\n',e)