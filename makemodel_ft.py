import fasttext
from datetime import datetime
import multiprocessing

starttime=str(datetime.now())
print("start")

model = fasttext.train_unsupervised('wikinoun.txt',lr=0.05,dim=200,ws=5,minCount=5,
                                    thread=multiprocessing.cpu_count()-1,epoch=10,neg=3,)
model.save_model("wikinoun.bin")

print("Finish!"+starttime+"→"+str(datetime.now()))
