import re
from sympy import symbols, Or, And, Not
from sympy.logic.boolalg import simplify_logic

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

print('DDNF: ', sort_def(DDNF.split('|')))
print('Maklaske: ', sort_def(Maklaske.split('|')))




