import MeCab
from sklearn.feature_extraction.text import CountVectorizer
import unicodedata
import re
import pandas as pd
import numpy as np



# MeCabの初期化
mecab = MeCab.Tagger("-Owakati")

# ファイルを開いて全文を読み込み加工する
with open('data/hashire_merosu.txt', mode='r', encoding='UTF-8') as f:
    title = f.readline()

# 改行を無くし全文をつなげる
content = ' '.join(content.split())
# 文章を正規化する
content = unicodedata.normalize('NFKC', content)

# 本文以外に該当する部分を切り離す
pattern = re.compile(r'^.+(#地から1字上げ].+#地から1字上げ]).+$')
body =re.match(pattern, content).group(1)

# 本文のみにクリーニングする
hashire_merosu_body = body.replace('#地から1字上げ] -------------------------------------------------------', '')
hashire_merosu_body = body.replace(' [#地から1字上げ]', '')

hashire_merosu = hashire_merosu_body
