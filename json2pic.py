import json
import os
import random

input_folder_json="./wikijson"
output_file_pic="./wikipic.tsv"

SAMPLE_NUM=1
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
        print(imgname)
        with open(imgname, "r",encoding="utf-8") as fp:
            json_load = json.load(fp)
            for title in json_load.keys():
                sentence=json_load[title].translate(str.maketrans("。",".","\n")).split(".")
                for i in range(len(sentence)-1):
                    if len(sentence[i])<SENTENCE_MIN:continue#←filter
                    if len(sentence[i+1])<SENTENCE_MIN:continue#←filter
                    with open(output_file_pic, "a",encoding="utf-8") as fp2:
                        fp2.write(title+"_"+str(i)+"\t"+"1"+"\t"
                                 +sentence[i].strip()+"\t"+sentence[i+1].strip()+"\n")
                    
                    i2=random.randrange(0,len(sentence))
                    if len(sentence[i2])<SENTENCE_MIN:continue#←filter
                    if i2-i<2 and -2<i2-i:continue#←Correct answer excluded
                    with open(output_file_pic, "a",encoding="utf-8") as fp2:
                        fp2.write(title+"_"+str(i)+"\t"+"0"+"\t"
                                 +sentence[i].strip()+"\t"+sentence[i2].strip()+"\n")
                

    print("finish!")
    