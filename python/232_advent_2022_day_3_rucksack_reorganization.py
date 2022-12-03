#	2022-12-03
#		16:10 - 16:57 part one
#		20:29 - 20:46 part two

def openFile(file):
	with open(file) as f:
		return [line.strip() for line in f.readlines()]

def splitIntoHalves(data):
	all_rucksacks = []
	for line in data:
		rucksack = []
		rucksack.append(line[:len(line)//2])
		rucksack.append(line[len(line)//2:])
		all_rucksacks.append(rucksack)
	return all_rucksacks
		
def findDuplicatedLetter(string1, string2):
	for letter in string1:
		if letter in string2:
			return letter

def createListOfDuplicatedLetters(data):
	duplicates = []
	for i in range(len(data)):
		duplicates.append(findDuplicatedLetter(data[i][0], data[i][1]))
	return duplicates

def countAsciiSum(list_):
	ans = 0
	for letter in list_:
		if letter.lower() == letter:
			ans += ord(letter)-96
		elif letter.upper() == letter:
			ans += ord(letter)-64+26
	return ans

data_one = splitIntoHalves(openFile('notepad/231_advent_2022_day_3.txt'))

def one():
	print("1:", countAsciiSum(createListOfDuplicatedLetters(data_one)))

one()



def divideIntoGroupsOfThree(data):
	all_groups = []
	group = []
	for i in range(len(data)):
		group.append(data[i])
		if i % 3 == 2:
			all_groups.append(group)
			group = []
	return all_groups

data_two = divideIntoGroupsOfThree(openFile('notepad/231_advent_2022_day_3.txt'))

# print(data_two)

def findLetterCommonInThree(string1, string2, string3):
	for letter in string1:
		if letter in string2 and letter in string3:
			return letter

def createListOfTripledLetters(data):
	triplicates = []
	for group in data:
		triplicates.append(findLetterCommonInThree(group[0], group[1], group[2]))
	return triplicates

def two():
	print("2:", countAsciiSum(createListOfTripledLetters(data_two)))

two()



