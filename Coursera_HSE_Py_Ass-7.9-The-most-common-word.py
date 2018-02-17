text = []
while True:
    textInp = input().strip().split()
    if len(textInp) > 0:
        text += textInp
    else:
        break
frequentWord = {}
print(text)
for word in text:
    frequentWord[word] = frequentWord.get(word, 0) + 1
sortedItemsList = sorted(frequentWord.items(), key=lambda x: -x[1])
maxItemsList = []
for i in range(len(sortedItemsList)):
    if sortedItemsList[0][1] == sortedItemsList[i][1]:
        maxItemsList.append(sortedItemsList[i][0])
print(min(maxItemsList))
