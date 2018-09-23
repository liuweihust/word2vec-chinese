from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import jieba
import time

RAWFILE="./raw/raw_news.txt"
PARSEDFILE="./data/parsed_news.txt"

def processraw():
	content = open(RAWFILE,"rb").read()
	words = " ".join(jieba.cut(content))

	t1 = time.time()
        words = " ".join(jieba.cut(content))

        t2 = time.time()
        tm_cost = t2-t1

        log_f = open(PARSEDFILE,"wb")
        log_f.write(words.encode('utf-8'))

def getparsed():
	return PARSEDFILE
