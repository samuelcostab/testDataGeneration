
import ast
import inspect
import sys
import importlib
from geraDot import *
from grafo import Grafo
from ast_walker import *
from ACO import ACOSymple
from staticfg import CFGBuilder
from interpreter import dataGenerator



def runner(nomeFunc, mainString, testResult, fun_name):
    # Executa tudo no arquivo executeTest.py com o comando "python3 executeTest.py"
    grafo = Grafo()
    codeAst = ast.parse(inspect.getsource(nomeFunc))
    
    cfg = CFGBuilder().build_from_file('gcd.py', './gcd.py')
    grafo = cfg._build_visual()
    #grafo.render(filename='g1.dot')
    print(grafo)
    paths = ACOSymple.createGraph(grafo)

    dataGenerator(paths, ast.dump(codeAst))
    
    #del grafo
    