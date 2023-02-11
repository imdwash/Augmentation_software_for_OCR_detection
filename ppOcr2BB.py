import ast
import json
import re
import argparse
import sys

parser=argparse.ArgumentParser()
parser.add_argument('--pp_txt=',type=str)
parser.add_argument('--out_dir=',type=str)
args=parser.parse_args()

pp_txt=vars(args)['pp_txt=']
out_dir=vars(args)['out_dir=']

# pp_txt="C:/innate2/ocrUnilever/det_db/predicts_db.txt"    ############## Put location of ppocr label txt
# out_dir='C:/innate2/ocrUnilever/det_db/outtxt/' ########## put output directory where txt are to be saved

f=open(pp_txt,'rb')
l=len(f.readlines())
f.close()
u=0
for j in range(0,l):

    f=open(pp_txt,'rb')

    txtname=str(f.readlines()[j]).split('.jpg')[0].split('/')[-1]
    f.close()
    f=open(pp_txt,'rb')
    points=str(f.readlines()[j]).split('.jpg')[1].replace('\t','').replace('\n','')

    points=re.findall(r'\d+', points)
    f.close()

    a=int(len(points)/8)
    for i in range(0,a):
        b=str(points[0+8*i:8+8*i]).replace("[","").replace("'","").replace("]","")
        f=open(out_dir+txtname+'.txt','a')
        f.write(b)
        f.write('\n')
    u=u+1
    print("number of conversion completed: ",u)
    f.close()

print("COMPLETED")