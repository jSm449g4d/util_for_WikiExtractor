from gensim.models.fasttext import FastText
from gensim.models import word2vec
from datetime import datetime
import logging
import multiprocessing
import os

MODEL_DIR="ft_model"

starttime=str(datetime.now())
print("start")
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

corpus =word2vec.LineSentence('wikinoun.txt')
model = FastText(corpus,sg=1,alpha=0.05, size=200, window=5,min_count=5,
                          workers=multiprocessing.cpu_count()-1,iter=10,negative=3,)
os.makedirs(MODEL_DIR, exist_ok=True)
model.save(os.path.join(MODEL_DIR,"wikinoun.model"))

print("Finish!"+starttime+"→"+str(datetime.now()))
