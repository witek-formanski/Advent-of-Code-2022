#	2022-12-02
#		8:03 - 8:46

def openFile(fileF):
	with open(fileF) as f:
		dataF = []
		for line in f.readlines():
			line = line.strip()
			lineList = line.split(' ')
			dataF.append(lineList)
		return dataF

data = openFile('notepad/229_advent_2022_day_2.txt')

oneValuesDict = {'X': 1, 'Y': 2, 'Z': 3}
oneWinDict = {'X': 'C', 'Y': 'A', 'Z': 'B'}
oneSameDict = {'X': 'A', 'Y': 'B', 'Z': 'C'}

def countScore(dataF):
	scoreF = 0
	for line in dataF:
		if line[0] == oneWinDict[line[1]]:
			scoreF += 6
		elif line[0] == oneSameDict[line[1]]:
			scoreF += 3
		scoreF += oneValuesDict[line[1]]
	return scoreF

def one():
	print('1:', countScore(data))

one()

twoRecipesDict = {'X': 0, 'Y': 3, 'Z': 6}
twoWinDict = {'A': 'C', 'B': 'A', 'C': 'B'}
twoValuesDict = {'A': 1, 'B': 2, 'C': 3}

def getKeyFromValue(d, val):
    return [k for k, v in d.items() if v == val][0]

def countScoreTwo(dataF):
	scoreF = 0
	for line in dataF:
		scoreF += twoRecipesDict[line[1]]
		if line[1] == 'X':
			scoreF += twoValuesDict[twoWinDict[line[0]]]
		elif line[1] == 'Y':
			scoreF += twoValuesDict[line[0]]
		elif line[1] == 'Z':
			scoreF += twoValuesDict[getKeyFromValue(twoWinDict ,line[0])]
	return scoreF

def two():
	print('2:', countScoreTwo(data))

two()



		