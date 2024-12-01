def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a = 3)
print_params(b = 25)
print_params(c = [1,2,3])

# Распаковка параметров:

values_list = ['Иванов', 758, [1, 2, 4]]
values_dict = {'a': values_list[1], 'b': values_list[0], 'c': values_list[2]}
print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)



