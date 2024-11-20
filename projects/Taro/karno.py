import re

def add_ampersand_with_spaces_and_parentheses(expression):
    parts = expression.split(" + ")
    modified_parts = []
    for part in parts:
        modified_part = re.sub(r"X(\d)", r"X\1 &", part)
        modified_part = modified_part.rstrip(" &")
        modified_parts.append(f"({modified_part})")
    return " + ".join(modified_parts)


expression = ""


result = add_ampersand_with_spaces_and_parentheses(expression)
result = str(result).replace('&', '& ')
result = str(result).replace('+', '∨')
print("Модифицированное выражение:", result)
