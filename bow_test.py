import MeCab
import pandas as pd
import gensim

def parse(tweet):
    t_list=[]
    t=MeCab.Tagger()
    temp1=t.parse(tweet)
    temp2=temp1.split("\n")
    for word in temp2:
        if word not in ["EOS",""]:
            word_sp=word.split("\t")
            word_sp=word_sp[:1]+word_sp[1].split(",")[:7]
            t_list.append(word_sp)
    return t_list

parse_doc=parse("私はリンゴを食べる。")
print(parse_doc)
