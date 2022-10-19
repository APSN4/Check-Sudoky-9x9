"""
by APSN4 // Суть проги заключается в том,
что если строка.sort() == идеальной строке(1,2,3,4,5,6,7,8,9) ,
столбец.sort() == идеальному столбцу(1,2,3,4,5,6,7,8,9) ,
и в каждом блоке(3x3) == идеалу(1,2,3,4,5,6,7,8,9) ,
то судоку решена верно. Отсортированная строка, стлб., блок = 123456789,
т.к судоку 9*9

"""

data = [
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],

  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],

  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

def Sydoky_checker(data):
	ideal_massiv = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	stolbs = [0] * 9
	for i in range(9): 
	    stolbs[i] = [0] * 9

	Success = True
	block_1 = []
	block_2 = []
	block_3 = []

	line_counter = 0 # 3 элемента в строке
	for number in data: # все числа
		counter = 0
		for number_in_line in number: # числа в строке
			if counter < 3:
				block_1.append(number_in_line)
			elif counter >= 3 and counter <= 5:
				block_2.append(number_in_line)
			elif counter >= 5 and counter <= 9:
				block_3.append(number_in_line)
			counter += 1
	for count_blocks in range(3): # 3 блока в общем блоке
		counter = 0
		local_massiv = [] # складываем сюда числа
		for number in block_1: # чекаем по 9 чисел в блоке
			if counter != 9:
				local_massiv.append(number)
			else:
				break
			counter += 1
		local_massiv.sort()
		if local_massiv != ideal_massiv:
			return False

	for stolb_number in range(0, 9):
		for number_stolb in range(0, 9):
			try:
				stolbs[stolb_number][number_stolb] = data[number_stolb][stolb_number]
			except:
				return False
		stolbs[stolb_number].sort()

		if stolbs[stolb_number] != ideal_massiv:
			return False

	for str_number in data:
		str_number.sort()
		if str_number != ideal_massiv:
			return False

	return Success

print(Sydoky_checker(data))