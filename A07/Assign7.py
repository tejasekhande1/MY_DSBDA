
import nltk
import re

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger")
nltk.download("omw-1.4")

file = open('text.txt', 'r')
text = file.read()
#print(text)

#Sentence Tokenization.
from nltk.tokenize import sent_tokenize
tokenized_text=sent_tokenize(text)
#print(tokenized_text)

#Word Tokenization
from nltk.tokenize import word_tokenize
tokenized_word=word_tokenize(text)
#print(tokenized_word)

#Print stop words of English
from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
#print(stop_words)

text = re.sub("[^a-zA-Z]"," ",text)
tokens = word_tokenize(text.lower ())
filtered_text=[]

for w in tokens:
    if w not in stop_words:
        filtered_text.append(w)
#print ("Tokenized Sentence:", tokens)
#print ("Filterd Sentence:", filtered_text)

from nltk.stem import PorterStemmer
ps=PorterStemmer()
#for w in tokens:
    #rootWord=ps.stem(w)
    #print(rootWord)

from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
#for w in filtered_text:
    #print(w,"--->",wordnet_lemmatizer.lemmatize(w))


from nltk.tokenize import word_tokenize
words = word_tokenize(text)
#for word in words:
    #print(nltk.pos_tag([word]))

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
string=[text]
tfidf =TfidfVectorizer()
result = tfidf.fit_transform(string)
print("Word indices:", tfidf.vocabulary)
print("TF-IDF Values:", result)
