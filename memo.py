import MeCab

text = "2年間連続売上１位の田中さんがついに部長に昇進した。"

tagger = MeCab.Tagger()
parse = tagger.parse(text)


print(parse)