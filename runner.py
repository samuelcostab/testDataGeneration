
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
from staticfg import CFGBuilder
from interpreter import dataGenerator



def runner(nomeFunc, mainString, testResult, fun_name):
    # Executa tudo no arquivo test.py com o comando "python3 test.py"
    grafo = Grafo()
    #walker = Ast_walker(grafo)
    codeAst = ast.parse(inspect.getsource(nomeFunc))
    ##listCoverage = getCoverage(nomeFunc, mainString,fun_name, mod_name)
    #walker.visit(codeAst) #dentro do walker fazer com que o nó possua as informações
                          #da Sintaxe Abstrata do código para poder gerar dados com base nisso
    
    cfg = CFGBuilder().build_from_file('foo.py', './foo.py')
    grafo = cfg._build_visual()
    
    #grafo.render(filename='g1.dot')
    paths = []#ACOSymple.createGraph(grafo)

    dataGenerator(paths, ast.dump(codeAst))
    
    #del grafo
    