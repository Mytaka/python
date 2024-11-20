import re
import numpy as np
from sympy import symbols, Or, And, Not
from sympy.logic.boolalg import simplify_logic
from pyeda.inter import expr, espresso_exprs

def generate_dnf(truth_table):
    num_vars = len(truth_table[0]) - 1  
    vars = symbols(f'X1:{num_vars + 1}') 

    expression = 0
    rows = []
    for row in truth_table:
        if row[-1] == 1: 
            term = []
            for i in range(num_vars):
                if row[i] == 1:
                    term.append(vars[i])  
                else:
                    term.append(Not(vars[i]))  
            expression = Or(expression, And(*term))  

    return simplify_logic(expression, form='dnf'), expression


def sort_def(terms):
    def sort_variables(term):
        variables = re.findall(r'[~]?X[1-4]', term) 
        sorted_vars = sorted(variables, key=lambda x: int(x[-1]), reverse=True)  
        return " & ".join(sorted_vars)

    sorted_terms = [sort_variables(term) for term in terms]
    sorted_expression = " ∨ ".join(f"({term})" for term in sorted_terms)
    return sorted_expression


def generate_karnaugh_map(expression):
    kmap = np.zeros((4, 4), dtype=int)

    row_map = {(0, 0): 0, (0, 1): 1, (1, 1): 2, (1, 0): 3}
    col_map = {(0, 0): 0, (0, 1): 1, (1, 1): 2, (1, 0): 3}
    
    terms = expression.split(" | ")
    for term in terms:
        X4 = X3 = X2 = X1 = None
        literals = term.replace("(", "").replace(")", "").split(" & ")
        for literal in literals:
            if literal == "X4":
                X4 = 1
            elif literal == "~X4":
                X4 = 0
            elif literal == "X3":
                X3 = 1
            elif literal == "~X3":
                X3 = 0
            elif literal == "X2":
                X2 = 1
            elif literal == "~X2":
                X2 = 0
            elif literal == "X1":
                X1 = 1
            elif literal == "~X1":
                X1 = 0
        row = row_map[(X4, X3)]
        col = col_map[(X2, X1)]
        kmap[row, col] = 1  
    return kmap

arr = '0	0	0	0	1	1	0	0	0	0	0	0	1	0	0	0'
variant_arr = list(map(int,arr.split('	')))

truth_table = [
    [0, 0, 0, 0, 0],  
    [0, 0, 0, 1, 0],  
    [0, 0, 1, 0, 0],  
    [0, 0, 1, 1, 0],  
    [0, 1, 0, 0, 0],  
    [0, 1, 0, 1, 0],  
    [0, 1, 1, 0, 0],  
    [0, 1, 1, 1, 0],  
    [1, 0, 0, 0, 0],  
    [1, 0, 0, 1, 0],  
    [1, 0, 1, 0, 0],  
    [1, 0, 1, 1, 0],  
    [1, 1, 0, 0, 0],  
    [1, 1, 0, 1, 0],  
    [1, 1, 1, 0, 0],  
    [1, 1, 1, 1, 0]   
]

truth_table = [i[:-1][::-1] + [j] for i,j in zip(truth_table,variant_arr)]

Maklaske,DDNF = generate_dnf(truth_table)

DDNF = str(DDNF)
Maklaske = str(Maklaske)

print('DDNF: ', sort_def(DDNF.split(" | ")))
print(generate_karnaugh_map(DDNF))
# print('Maklaske: ', sort_def(Maklaske.split(' | ')))

DDNF = expr(DDNF)
Karno = espresso_exprs(DDNF)

Karno = str(Karno)
Karno = Karno.replace("And", "").replace("Or", "").replace(', (',' | (').replace(', ', ' & ')
Karno = Karno.replace('(((', '(').replace(')),)',')')

print("Мінімізована форма: ", sort_def(Karno.split(' | ')))


#https://sublime.tools/ru/karta-karno