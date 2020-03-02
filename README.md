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
**you can get noun dataset**  
0.plz install MeCab+neologd on Windows → https://huxiin.ga/wordpress/?p=983  
1.plz get wikipedia_dataset(japanese) expressed in json by `$ python3 we2json.py`  
2.Japanese:`$ python3 json2noun.py`  
