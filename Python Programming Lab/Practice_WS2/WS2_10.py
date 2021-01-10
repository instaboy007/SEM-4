lines = []
inputSentence = input('Enter the sentence ')
lines = inputSentence.split('. ')
print(lines)
sentences = []
for line in lines:
    words = line.split(':')[1].split()
    sentences.append([line.split(':')[0],words])
print(sentences)