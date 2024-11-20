data = set("Hello")
data = {5,2,34,1,5,6,4}

data.add(47)                # добавить 
data.update([32121,12,51])  # добавить много
data.remove(47)             # удалить значение
data.pop()                  # удалить первое значение
data.clear                  # очистить
data.union(setTwo)          # объеденить множества
data.intersection(setTwo)   # пересечение множеств
data.difference(setTwo)     # разница множеств 

print(data)

# ---------------------------------------------------------------------------

nums = [5,2,4,5,6,1,2,3,5,6,5,4,1]
number = set(nums) # множество которое можно менять 

new_date = frozenset(nums) # множество которое нельзя менять 

print(nums)                 




