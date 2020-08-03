import random
import sys
import re

lyrics = open('kodaline.txt', 'r').read()
lyrics = re.sub('[^a-zA-Z]', ' ', lyrics)
lyrics = lyrics.lower().split()


index = 1
markov_chain = {} #dictionary of words in lyrics
count = 50

for word in lyrics[index:]:
    key = lyrics[index - 1]
    if key in markov_chain:
        markov_chain[key].append(word)
    else:
        markov_chain[key] = [word]
    index += 1

word1 = random.choice(list(markov_chain.keys())) #random first word
message = word1.capitalize()

# Picks the next word over and over until word count achieved
while len(message.split(' ')) < count:
	word2 = random.choice(markov_chain[word1])
	word1 = word2
	message += ' ' + word2

print('yo')
print(message)
