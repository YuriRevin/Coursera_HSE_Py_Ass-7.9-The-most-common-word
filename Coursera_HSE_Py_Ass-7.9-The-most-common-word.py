text = open('input.txt', 'r', encoding='utf8')
frequentWord = {}
for line in text:
    line = line.strip().split()
    for word in line:
        frequentWord[word] = frequentWord.get(word, 0) + 1
sortedItemsList = sorted(frequentWord.items(), key=lambda x: -x[1])
maxItemsList = []
for i in range(len(sortedItemsList)):
    if sortedItemsList[0][1] == sortedItemsList[i][1]:
        maxItemsList.append(sortedItemsList[i][0])
print(min(maxItemsList))
