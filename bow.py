# インポート類
import numpy as np
import pandas as pd
import MeCab
import unicodedata
import re

text_paths = ["data/hashire_merosu.txt","data/rashomon.txt","data/gakumonno_susume.txt"]
documents = []

for i in text_paths:
    # ファイルを開いて全文、タイトル、著者を読み込む
    with open(i, mode='r', encoding='UTF-8') as f:
        content = f.read()

        # 改行を無くし全文をつなげる
        content = ' '.join(content.split())
        # 文章を正規化する
        content = unicodedata.normalize('NFKC', content)

        documents.append(content)
print(documents)




# 単語のリストを作る
words_list = []

# MeCabを初期化する
tagger = MeCab.Tagger()

# 生成する辞書
word2int = {}
i = 0

# 形態素解析して辞書に入れていく
for sentence in documents:
    sentence_parced = tagger.parse(sentence)
    words_in_sentence = []

    print(sentence_parced)
    for line in sentence_parced.splitlines()[:-1]:
        words_in_sentence.append(line.split('\t')[0])
        if line.split('\t')[0] not in word2int:
            word2int[line.split('\t')[0]] = i
            i += 1
    words_list.append(words_in_sentence)


# BoWを作る
bow = np.zeros((len(words_list), len(word2int)), dtype=np.int64)
for i, words in enumerate(words_list):
    for word in words:
        bow[i, word2int[word]] += 1

# pandas形式にする
df_bow = pd.DataFrame(bow, columns=list(word2int))

# 表示(Jupyterで回す場合は、displayのほうが見やすい形式で出力できる)
print(df_bow)
