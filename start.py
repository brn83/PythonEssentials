#!/usr/bin/env python3
"""Hello World Multi Línguas.
    
    Dependendo a língua configurada no ambiente o programa 
    exibe a msg correspondente.
    
    Usage: 
    
    Tenha a váriavel LANG devidamente configurada ex:
    
        export LANG=pt_BR
        
    Run: 
        python3 start.py
        or
        ./hello.py    
"""
__version__ = "0.0.1"
__author__ = "Bruno Fereira"
__license__ ="Unlicense"

import os

current_language = os.envget("LANG")
msg = "Hello, World!"
    
# if __name__ == "__main__":
if current_language == "pt_BR.UTF-8":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
    
#imprimir o valor da var msg:    
print(msg)