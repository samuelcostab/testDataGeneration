
import ast
import inspect
from geraDot import *
from grafo import Grafo
from ast_walker import *
from ACO import ACOSymple
from staticfg import CFGBuilder
from interpreter import dataGenerator



def runner(nomeFunc, mainString, testResult, fun_name):
    # Executa tudo no arquivo executeTest.py com o comando "python3 executeTest.py"
    # Ao analisar nova função, lembrar de alterar o nome do arquivo em runner.py e executeTest.py
    # ao gerar o arquivo g1.dot, lembrar de retirar o primeiro nó de "declaração" para não entrar no loop infinito
    grafo = Grafo()
    codeAst = ast.parse(inspect.getsource(nomeFunc))
    
    cfg = CFGBuilder().build_from_file('gcd.py', './gcd.py')
    grafo = cfg._build_visual()
    #grafo.render(filename='g1.dot')
    print(grafo)
    paths = ACOSymple.createGraph(grafo)

    dataGenerator(paths, ast.dump(codeAst))
    
    #del grafo
    