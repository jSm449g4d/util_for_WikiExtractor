
import os 
import MeCab
import random
import json
import urllib.request
import zipfile
import subprocess
import sys

input_folder_json="./wikijson"
output_folder_json="./wikinoun"
SENTENCE_MIN=15

#plz check this article because this program require these data.
#https://github.com/jSm449g4d/util_for_WikiExtractor
#https://qiita.com/_likr/items/0fc845f59b4ad685cc06

def ffzk(input_dir):#Relative directory for all existing files
    imgname_array=[];input_dir=input_dir.strip("\"\'")
    for fd_path, _, sb_file in os.walk(input_dir):
        for fil in sb_file:imgname_array.append(fd_path.replace('\\','/') + '/' + fil)
    if os.path.isfile(input_dir):imgname_array.append(input_dir.replace('\\','/'))
    return imgname_array


def text2noun(MeCab_Tagger,text="",separator=' ',indention='\n',wakachi_mode=0):
    sep=text.replace("。","\n").split('\n');
    sep=text.translate(str.maketrans("。",".","\n")).split(".")
    ret=""
    sep = filter(lambda a: SENTENCE_MIN<len(a), sep)
    for line in sep:
        nounline=""
        node=MeCab_Tagger.parseToNode(line)
        while node:
            if node.feature.split(",")[0] == "名詞":
                nounline+=node.surface+separator
            elif wakachi_mode:nounline+=node.surface+separator
            node = node.next
        ret+=nounline.strip(separator)+indention
    return ret

if __name__ == '__main__':
    
#MeCab+Neologd on Windows
    chasen = MeCab.Tagger('-Ochasen -d $(rcpath)\..\dic\mecab-ipadic-neologd')
       
#    imgname_array=random.sample(ffzk(input_folder_json),1)
    imgname_array=ffzk(input_folder_json)
    os.makedirs(output_folder_json, exist_ok=True)
    for imgname in imgname_array:
        print(imgname)
        with open(imgname, "r",encoding="utf-8") as fp:
            json_load = json.load(fp)
            for title in json_load.keys():
                try:
                     with open(os.path.join(output_folder_json,os.path.basename(imgname)+".csv"), "a",encoding="utf-8") as fp2:
                         fp2.write(text2noun(chasen,json_load[title]))
                except:
                    print("Error:"+imgname)
    print("finish!")
    