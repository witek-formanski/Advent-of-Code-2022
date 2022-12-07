#	2022-12-05
#		17:41 - 18:40 	data preparation
#		19:03 - 19:20 	one
#		21:00 - 21:21   two

file = 'notepad/233_advent_2022_day_5.txt'

def splitDataBlankLine(file_):
	with open(file_) as f_:
		before_ = []
		after_ = []
		flag_ = True
		for line_ in f_.readlines():
			if line_.strip() == '':
				flag_ = False
			elif flag_ == True:
				before_.append(line_)
			elif flag_ == False:
				after_.append(line_.rstrip())
		return [before_, after_]

def splitWithSpace(data_):
	list_ = []
	for line_ in data_:
		list_.append(line_.split(' '))
	return list_

def saveOnlyEvenElements(data_):
	list_of_lists_ = []
	for line_ in data_:
		list_ = []
		for i in range(1,len(line_)+1,2):
			list_.append(line_[i])
		list_of_lists_.append(list_)
	return list_of_lists_

def saveOnlyOddElements(data_):
	list_of_lists_ = []
	for line_ in data_:
		list_ = []
		for i in range(0,len(line_),2):
			list_.append(line_[i])
		list_of_lists_.append(list_)
	return list_of_lists_

def intMatrix(matrix_):
	new_matrix_ = []
	for line_ in matrix_:
		new_line_ = []
		for element_ in line_:
			new_line_.append(int(element_))
		new_matrix_.append(new_line_)
	return new_matrix_

def stringToListOfChars(data_):
	return [list(line_) for line_ in data_]

def rotateMatrixMirror(matrix_):
	new_matrix_ = []
	for i in range(len(matrix_)):
		new_matrix_.append([])
	for line_ in matrix_:
		for element_index_ in range(len(line_)):
			new_matrix_[element_index_].append(line_[element_index_])
	return new_matrix_

def reverseMatrixLines(matrix_):
	new_matrix_ = []
	for line_ in matrix_:
		line_.reverse()
		new_matrix_.append(line_)
	return new_matrix_

def clearStacks(matrix_):
	new_matrix_ = []
	for line_ in matrix_:
		del line_[0]
		new_line_ = []
		for element_ in line_:
			if element_ != ' ':
				new_line_.append(element_)
		new_matrix_.append(new_line_)
	return new_matrix_

def prepareInstructions(file_):
	instructions_ = splitDataBlankLine(file_)[1]
	instructions_ = splitWithSpace(instructions_)
	instructions_ = saveOnlyEvenElements(instructions_)
	instructions_ = intMatrix(instructions_)
	return instructions_

def prepareStacks(file_):
	stacks_ = splitDataBlankLine(file_)[0]
	stacks_ = stringToListOfChars(stacks_)
	stacks_ = saveOnlyEvenElements(stacks_)
	stacks_ = saveOnlyOddElements(stacks_)
	stacks_ = rotateMatrixMirror(stacks_)
	stacks_ = reverseMatrixLines(stacks_)
	stacks_ = clearStacks(stacks_)
	return stacks_

def moveOne(line_):
	global stacks
	moved_stack = stacks[line_[1]-1][-1]
	del stacks[line_[1]-1][-1]
	stacks[line_[2]-1].append(moved_stack)

def moveNPartOne(line_):
	for n in range(line_[0]):
		moveOne(line_)

def followTheInstructions(instructions_, func):
	for line_ in instructions_:
		func(line_)

def message(stacks_):
	mess_ = ''
	for line_ in stacks_:
		mess_ += line_[-1]
	return mess_

stacks = prepareStacks(file)
instructions = prepareInstructions(file)

def one():
	followTheInstructions(instructions, moveNPartOne)
	print(stacks)
	print("1:", message(stacks))	

one()

def moveNPartTwo(line_):
	global stacks
	move_number = line_[0]
	from_number = line_[1]-1
	to_number = line_[2]-1
	load = []
	for n in range(move_number):
		load.append(stacks[from_number][-1])
		del stacks[from_number][-1]
	load.reverse()
	stacks[to_number].extend(load)
	# for n in move_number:

stacks = prepareStacks(file)

def two():
	followTheInstructions(instructions, moveNPartTwo)
	print("2:", message(stacks))

two()