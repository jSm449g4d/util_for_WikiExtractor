# -*- coding: utf-8 -*-
#How to use
#1.plz dl WikiExtractor→https://github.com/attardi/wikiextractor
#2.Throw this file into the WikiExtractor folder
#3.$ pip install -U beautifulsoup4
#4.$ python3 we2json.py

from bs4 import BeautifulSoup
import json
import subprocess
import os
import argparse
import io
import urllib.request
import zipfile

output_folder_json="./wikijson"
libdata={}


def extract(input_file):
    subprocess.call(['python3', 
                    'wikiextractor-master/WikiExtractor.py', 
                    input_file,])

def ffzk(input_dir):#Relative directory for all existing files
    imgname_array=[];input_dir=input_dir.strip("\"\'")
    for fd_path, _, sb_file in os.walk(input_dir):
        for fil in sb_file:imgname_array.append(fd_path.replace('\\','/') + '/' + fil)
    if os.path.isfile(input_dir):imgname_array.append(input_dir.replace('\\','/'))
    return imgname_array

def storer(input):
    if type(input) is not str:return ""
    io_ = io.StringIO() 
    spaceflag=1;sqflag=0;Ynflag=1
    for car in input:
        if car=='<':sqflag=1;continue
        if car=='>':sqflag=0;continue
        if sqflag==1:continue
        if car==' ' and spaceflag==0:io_.write(car);spaceflag=1;continue
        if car=='\n' and Ynflag==0:io_.write(car);Ynflag=1;continue
        if  car=='\n'or car==' 'or car=='\t' or car=='◆' or car=='　'or car=='★'\
            or car=='・' or car=='□'or car==',' or car=='■' or car=='♪' or car=='…'\
            or car=='◇' or car=='※' or car==':' or car =='‥' or car=='↓' or car=='＊'\
            or car=='▼' or car=='◎' or car=='③' or car=='②' or car=='①'\
            or car=='/' or car=='●' or car=='▲'or car=='〇'or car=='☆':continue
        io_.write(car);spaceflag=0;Ynflag=0
    output = io_.getvalue();io_.close()
    return output

if __name__ == '__main__':
    print("AA")
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("-L",
                        '--language',
                        default="ja",
                        help='en:english,ja:japanese')
    args = parser.parse_args()
    
    #download WikiExtractor
    urllib.request.urlretrieve("https://github.com/attardi/wikiextractor/archive/master.zip","master.zip")
    with zipfile.ZipFile("master.zip") as zf:zf.extractall()
    os.remove("master.zip")
    
    #download Wikipedia_dump
    dl_url="https://dumps.wikimedia.org/"+args.language+"wiki/latest/"\
    +args.language+"wiki-latest-pages-articles-multistream.xml.bz2"
    print("Downloading...")
    urllib.request.urlretrieve(dl_url,os.path.basename(dl_url))
    extract(os.path.basename(dl_url))
    print("Success!")
    os.makedirs(output_folder_json, exist_ok=True)
    
    imgname_array=ffzk("text")
    for imgname in imgname_array:
        print(imgname)
        with open(imgname, "r",encoding="utf-8") as fp:
            html=fp.read();soup=BeautifulSoup(html,"html.parser")
            
            for i in range(len(soup.findAll("doc"))):
                libdata[storer(str(soup.findAll("doc")[i].attrs["title"]))
                ]=storer(str(soup.findAll("doc")[i].string))
            with open(os.path.join(output_folder_json,
                                   imgname.translate(str.maketrans("","","\"\'\\/<>%`?;")))
                      +".json", "w",encoding="utf-8") as fp:
                json.dump(libdata,fp, ensure_ascii=False);libdata.clear()
                
    os.remove(os.path.basename(dl_url))
    print("Finish!")
                    