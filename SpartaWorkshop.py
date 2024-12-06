#Day 1
#str.strip()
#str.count("text")
#str.lower()
#str.upper()
#str.capitalize()
#str = "with a long case"
#str.replace("with", ',')
#print(str, "\n")

#x = 2
#y = 5.4
#z = " there's now number 25.4 unless we put a space in!"
#result = str(x) + str(y) + z
#print(result)

#int_string = "6"
#int_var = int(int_string)
#float_var = float(int_string)
#print(type(int_var))
#print(type(float_var))
#print (int_var + float_var)

#name = "Lassie"
#years = 7
#height_cm = 60.2
#string_out = f"{name} is {years} old and {height_cm} cm tall."
#print(string_out)





#Day 2
#Task 1
shopping_list = ['eggs','bread','bananas','biscuits','milk']
print(shopping_list)
print(type(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])
result = [item.replace('bread', 'rice') for item in shopping_list]
#shopping_list[1] = 'rice'
#for index, value in enumerate(shopping_list):
#    if value == 'bread':
#        shopping_list[index] = 'rice'

print(shopping_list)
shopping_list.append('carrots')
print(shopping_list)
list2 = ['toffee', 'coffee']
shopping_list.extend(list2)
res_list = shopping_list + list2
print(res_list)
shopping_list.remove('bananas')
shopping_list.pop(-1)
print(shopping_list)


#Task 2

