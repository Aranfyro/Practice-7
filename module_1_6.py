my_dict = {'Andrew' : 1999, 'Michael' : 2000}
print ('Начальный словарь: ', my_dict)

# Вывод значения по существующему ключу:
print ('Существующий ключ: ', my_dict['Andrew'])

# Вывод значения по отсутствующему ключу
#my_dict ['Carl'] = 1998
print ('Отсутсвующий ключ: ', my_dict.get('Carl'))

#Добавление пар
my_dict.update ({'Nathon' : 2001, 'Alexa' : 2002})

#Удаление пар
del my_dict ['Michael']
print ('Конечный словарь: ', my_dict)

my_set = {1, 2, 3, 'a', 'b', 'c', 1, 2, 3, 'a', 'b', 'c'}
print ('\nНачальное множество: ', my_set)

# Добавление элементов
my_set.add(4.3)
my_set.add((1, 2, 3))

# Удаление элемента
my_set.remove(1)
print ('Конечное множество: ', my_set)