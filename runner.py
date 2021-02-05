
import ast
import inspect
import sys
import importlib
#import coverage
from geraDot import *
from grafo import Grafo
from ast_walker import *
from instrumentation import *
from ACO import ACOSymple


def runner(nomeFunc, mainString, testResult, fun_name):
    # Executa tudo no arquivo test.py com o comando "python3 test.py"
    grafo = Grafo()
    walker = Ast_walker(grafo)
    codeAst = ast.parse(inspect.getsource(nomeFunc))
    ##listCoverage = getCoverage(nomeFunc, mainString,fun_name, mod_name)
    walker.visit(codeAst)

    geraDot(grafo.listaNos, [0], [0], [0], testResult, fun_name)

    print("\nPRINTANTO GRAFO")

    ACOSymple.createGraph(grafo.listaNos)

    del grafo
