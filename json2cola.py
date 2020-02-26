import json
import os
import random

input_folder_json="./wikijson"
output_file_cola="./wikicola.txt"

SAMPLE_NUM=10
SENTENCE_MIN=15

def ffzk(input_dir):#Relative directory for all existing files
    imgname_array=[];input_dir=input_dir.strip("\"\'")
    for fd_path, _, sb_file in os.walk(input_dir):
        for fil in sb_file:imgname_array.append(fd_path.replace('\\','/') + '/' + fil)
    if os.path.isfile(input_dir):imgname_array.append(input_dir.replace('\\','/'))
    return imgname_array

if __name__ == '__main__':
    imgname_array=random.sample(ffzk(input_folder_json),SAMPLE_NUM)
    
    for imgname in imgname_array:
        with open(imgname, "r",encoding="utf-8") as fp:
            json_load = json.load(fp)
            for title in json_load.keys():
                for sentence in json_load[title].translate(str.maketrans("。",".","\n")).split("."):
                    if len(sentence)<SENTENCE_MIN:continue#←filter
                    with open(output_file_cola, "a",encoding="utf-8") as fp2:
                        fp2.write(title+"\t"+"1"+"\t_\t"+sentence.strip()+"\n")
    print("finish!")
    