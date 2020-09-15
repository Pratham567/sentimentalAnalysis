from scraper import data
import string
from collections import Counter
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

text = open('/home/bilbo/@workspace/python_projects/sentimentalAnalysis/scrapeYTcomments/comments.txt', encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Using word_tokenize because it's faster than split()
tokenized_words = word_tokenize(cleaned_text, "english")

# Removing Stop Words
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

# Lemmatization - From plural to single + Base form of a word (example better-> good)
lemma_words = []
for word in final_words:
    word = WordNetLemmatizer().lemmatize(word)
    lemma_words.append(word)
# Get emotions text
emotion_list = []
with open('/home/bilbo/@workspace/python_projects/sentimentalAnalysis/model/emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        # print(emotion)
        if word in final_words:
            emotion_list.append(emotion)
            # print(final_words)

w = Counter(emotion_list)
print(w)

# fig, ax1 = plt.subplots()
# ax1.bar(w.keys(), w.values())
# fig.autofmt_xdate()
# plt.savefig('graph.png')
# plt.show()