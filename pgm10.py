import nltk
from nltk.compus import stop words
from nltk.stem import porter
from nltk import post_tag, ne_chunk, word_tokenize, regexpParser
text="""Ravi kumar is working at infosys in bangalore he met Dr Anita sharma on monday to discuss a new NLP project for health care data analysis in india."""
print("original text:")
print(text)
print("_"*60)
token=word_tokenize(text)
print("a)token(word tokenizeation):")
print("_"*60)
stop_word=set(stopwords.word)("english")
filtered_tokens=[word for word in tokens if word.lover()not in stop_word.is slpha()]
print("b)after removing stop words:")
print(filtered_tokens)
print("_"*60)
stemmer=porterstemmer()
stemmer_word=[stemmer.stem(word in filtered.token)]
print("c)stemmed_words:")
print(stemmed_word)
print("_"*60)
por_tags=por_tag(tokens)
print("d)part of speech (por)tags:")
print(por_tags)
print("_"*60)
grammar=r"NP:{<DT>?<JJ>*<NNP>+}"
chunk_passes(grammar)
chunk_tree=chunk_passes.parse.(por_tags)
print("e)chunking(noun phrasses):")
print(chunk_tree)
print("_"*60)


