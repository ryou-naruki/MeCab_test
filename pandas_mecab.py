import unicodedata
import re
import pandas as pd

# =====================================================================

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

author = author.replace('\n', '')

# =====================================================================

# ファイルを開いて全文を読み込む
with open('data/hashire_merosu.txt', mode='r', encoding='UTF-8') as f:
    content = f.readlines()

# データフレームに全文を1行ずつ入れる
df = pd.DataFrame(content, columns=['text'])
df['text'] = df['text'].str.replace('\n', '')

# 公開日と修正日について
date = df[(df['text'].str.contains('日公開'))|(df['text'].str.contains('日修正'))].copy()

date['text'] = date['text'].str.replace('公開', '')
date['text'] = date['text'].str.replace('修正', '')

date['text'] = date['text'].str.replace('年', '/')
date['text'] = date['text'].str.replace('月', '/')
date['text'] = date['text'].str.replace('日', '')

date['text'] = pd.to_datetime(date['text'])
date.dtypes

# 取得した日時と計算結果
release_date = date.iat[0, 0]
update_date = date.iat[1, 0]
# print(release_date)
# print(update_date)

date = update_date - release_date


# 取得項目を格納したデータフレーム
booklist = pd.DataFrame([[title, author, release_date, update_date, body]],
columns = ['title', 'author', 'release_date', 'update_date', 'body'])

print(booklist)