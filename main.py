import re
from collections import Counter
from nltk.corpus import stopwords


with open('file.txt', 'r') as f:
    text = f.read()
# Split the text into individual words
words = re.findall(r'\w+', text.lower())

# Remove stop words
stop_words = set(stopwords.words('english'))
words = [word for word in words if word not in stop_words]

# Calculate the frequency of each word in the text
word_freq = Counter(words)

# Split the text into individual sentences
sentences = re.split(r'[.!?]', text)

# Calculate the total number of words in each sentence
sentence_word_count = [len(re.findall(r'\w+', sentence.lower())) for sentence in sentences]

# Calculate the score of each word
word_score = {}
for word in word_freq.keys():
    word_degree = 0
    for sentence, word_count in zip(sentences, sentence_word_count):
        if word in sentence.lower():
            word_degree += word_count
    word_score[word] = word_degree / word_freq[word]

# Sort the words by score
sorted_words = sorted(word_score.items(), key=lambda x: x[1], reverse=True)

# Extract the top keywords
keywords = []
for word, score in sorted_words[:10]:
    if len(word) > 1:
        keywords.append(word)

print(keywords)
