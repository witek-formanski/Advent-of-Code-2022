# 	2022-12-01
#		16:39 - 17:00

def openFile(filename):
	with open(filename) as f:
		return f.read().splitlines()

def sumElves(dataList):
	elfValue = 0
	elfList = []
	for element in dataList:
		if element != '':
			elfValue += int(element)
		elif element == '':
			elfList.append(elfValue)
			elfValue = 0
	return elfList


file = 'notepad/228_advent_2022_day_1.txt'

def one():
	print('1:', max(sumElves(openFile(file))))

one()

def topThreeSum(dataList):
	dataList.sort(reverse=True)
	ans = 0
	for i in range(3):
		ans += dataList[i]
	return ans

def two():
	print('2:', topThreeSum(sumElves(openFile(file))))

two()
