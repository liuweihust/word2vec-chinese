import jieba
import time
import sys
import argparse
from os import listdir
from os.path import isfile, join
from datasets import data_factory

allwords=''.encode('utf-8')

def parse_txt(infile,outfile):
	jieba.enable_parallel(8)

	content = open(infile,"rb").read()
	t1 = time.time()
	words = " ".join(jieba.cut(content))

	t2 = time.time()
	tm_cost = t2-t1

	log_f = open(outfile,"wb")
	log_f.write(words.encode('utf-8'))

	print('speed %s bytes/second' % (len(content)/tm_cost))

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-d','--dataset',  help='news',default='news')
	args = parser.parse_args()

	dc = data_factory.get_dataset(args.dataset)
	dc.processraw()

