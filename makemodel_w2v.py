from gensim.models import word2vec
from datetime import datetime
import logging
import multiprocessing

#Distributed Representations of Words and Phrases and their Compositionality
#https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf

starttime=str(datetime.now())
print("start")
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

corpus =word2vec.LineSentence('wikinoun.txt')
model = word2vec.Word2Vec(corpus,sg=1,alpha=0.025, size=200, window=5,min_count=5,
                          workers=multiprocessing.cpu_count(),iter=5,negative=3,)
model.save("wikinoun.model")

print("Finish!"+starttime+"→"+str(datetime.now()))
