# util_for_WikiExtractor
utility_for_WikiExtractor (for using wikipedia data)  
To get new data from wikipedia, I made it because DL and processing are troublesome  
※WikiExtractor→https://github.com/attardi/wikiextractor  

## How to use
### we2json.py
**you can get LATEST wikipedia_dataset by oneline command**  
0.`$ pip install -U beautifulsoup4`  
1.Japanese:`$ python3 we2json.py` or English:`$ python3 we2json.py -L en`  
### json2noun.py
**you can get japanese noun dataset used by Word2Vec etc...**  
0.plz install MeCab+neologd on Windows → https://huxiin.ga/wordpress/?p=983  
1.plz get wikipedia_dataset(japanese) expressed by json → `$ python3 we2json.py -L ja`  
2.noun:`$ python3 json2noun.py` verb:`$ python3 json2noun.py -F 動詞`  
x.if you need dataset as one_file → `$ cat ./wikinoun/*.txt > wikinown.txt`  
