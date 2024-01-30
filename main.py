import unicodedata
import re
import pandas as pd

# ファイルを開いて全文、タイトル、著者を読み込む
with open('data/hashire_merosu.txt', mode='r', encoding='UTF-8') as f:
    title = f.readline()
    author = f.readline()
    content = f.read()

# 改行を無くし全文をつなげる
content = ' '.join(content.split())
# 文章を正規化する
content = unicodedata.normalize('NFKC', content)

# 本文以外に該当する部分を切り離す
pattern = re.compile(r'^.+(#地から1字上げ].+#地から1字上げ]).+$')
body =re.match(pattern, content).group(1)

# 本文のみにクリーニングする
body = body.replace('#地から1字上げ] -------------------------------------------------------', '')
body = body.replace(' [#地から1字上げ]', '')

# タイトルと著者を別途取って来る(改行を除外)
title = title.replace('\n', '')
print(title)
author = author.replace('\n', '')
print(author)


print(body)

