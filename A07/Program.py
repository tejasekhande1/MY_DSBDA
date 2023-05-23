import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

from nltk import sent_tokenize
from nltk import word_tokenize

from nltk.corpus import stopwords

file = open('text.txt','r')
text = file.read()
print(text)

tokens_sents = nltk.sent_tokenize(text)

print("Sentence Tokenized : \n",tokens_sents)

tokens_words = nltk.word_tokenize(text)

print("\nWord Tokenized : \n",tokens_words)

#------- STEMMING -------

from nltk.stem import PorterStemmer

#from nltk.stem.snowball import SnowballStemmer
#from nltk.stem import LancasterStemmer

stem=[]
for i in tokens_words:
  ps = PorterStemmer()
  stem_word= ps.stem(i)
  stem.append(stem_word)

#print(stem)

#------- STOP WORD ------

sw_nltk = stopwords.words('english')
print(sw_nltk)
words = [word for word in text.split() if word.lower() not in sw_nltk]
new_text = " ".join(words)
print(new_text)

# ------- PARTSOFSPEECH ------

print("Parts of Speech : ",nltk.pos_tag(stem));
