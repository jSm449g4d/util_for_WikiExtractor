import json
import os
import argparse
import io
import urllib.request

input_folder_json="./wikijson"
output_file_cola="./wikicola.txt"

def ffzk(input_dir):#Relative directory for all existing files
    imgname_array=[];input_dir=input_dir.strip("\"\'")
    for fd_path, _, sb_file in os.walk(input_dir):
        for fil in sb_file:imgname_array.append(fd_path.replace('\\','/') + '/' + fil)
    if os.path.isfile(input_dir):imgname_array.append(input_dir.replace('\\','/'))
    return imgname_array

if __name__ == '__main__':
    imgname_array=ffzk(input_folder_json)
    
    for imgname in imgname_array:
        with open(imgname, "r",encoding="utf-8") as fp:
            json_load = json.load(fp)
            for title in json_load.keys():
                for sentence in json_load[title].translate(str.maketrans("。",".","\n")).split("."):
                    with open(output_file_cola, "a",encoding="utf-8") as fp:
                        fp.write(title+"\t"+"1"+"\t_\t"+sentence+"\n")
    print("finish!")
    