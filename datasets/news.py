from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import jieba
import time

RawFile="./raw/raw_news.txt"
ParsedFile="./data/parsed_news.txt"
GensimFile="./data/model_news.txt"
VectorFile="./data/vector_news.txt"

def processraw():
	content = open(RawFile,"rb").read()
	words = " ".join(jieba.cut(content))

	t1 = time.time()
        words = " ".join(jieba.cut(content))

        t2 = time.time()
        tm_cost = t2-t1

        log_f = open(ParsedFile,"wb")
        log_f.write(words.encode('utf-8'))

def getparsed():
	return ParsedFile

def getmodelfile():
	return GensimFile

def getvectorfile():
	return VectorFile
