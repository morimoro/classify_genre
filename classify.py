# 参考にしたサイト
# https://qiita.com/hyo_07/items/ba3d53868b2f55ed9941

import MeCab
import os
from gensim import corpora
from csv import reader
from gensim import matutils

w_list = []
labels = []

# f_list = os.listdir("./text/")
# for lists in f_list:
#     with open("./text/"+ lists, 'r', encoding='UTF-8') as f:
#         w = f.read().replace('\u3000','').replace('\n','')
#         w_list.append(w)

# csvfileを読み込み
with open("PVeye_eye_sight.csv", 'r', encoding='utf_8_sig') as csv_file:
    csv_reader = reader(csv_file)
    list_of_rows = list(csv_reader)
    list_of_rows.pop(0)
    for list_of_row in list_of_rows:
        w_list.append(list_of_row[1] + list_of_row[2])

mecab = MeCab.Tagger('mecabrc')

# 形態素解析をして、名詞だけ取り出す
def tokenize(text):
    node = mecab.parseToNode(text)
    while node:
        if node.feature.split(',')[0] == '名詞':
            yield node.surface.lower()
        node = node.next

# 記事群のdictについて、形態素解析をしてリストに返す
def get_words(contents):
    ret = []
    for  content in contents:
        ret.append(get_words_main(content))
    return ret

# 一つの記事を形態素解析して返す
def get_words_main(content):
    return [token for token in tokenize(content)]

words = get_words(w_list)
print(words[0])


# コーパスの作成
# コーパス：言語学において、自然言語処理の研究に用いるため、自然言語の文章を構造化し大規模に集積したもの
dictionary = corpora.Dictionary(words)
dictionary.filter_extremes(no_below = 3, no_above = 0.5)
# チューニング
#   no_below : 単語が使われている文章の数が設定値未満の時、その単語を削除
#   no_above : 単語が使われている文章の割合が設定値以上のとき、その単語を削除
#dictionary.save_as_text("./tmp/dictionary.txt") で、作成した辞書を保存可能
#dictionary = corpora.Dictionary.load_from_text("./tmp/dictionary.txt") で読み込み
courpus = [dictionary.doc2bow(word) for word in words]
print(courpus)

# コーパスを特徴ベクトルへの変換
def vec2dense(vec, num_terms):
    return list(matutils.corpus2dense([vec], num_terms=num_terms).T[0])
data_all = [vec2dense(dictionary.doc2bow(words[i]),len(dictionary)) for i in range(len(words))]
print(data_all)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

#トレーニング・テストデータの設定
train_data = data_all
X_train, X_test, y_train, y_test = train_test_split(train_data, labels, test_size=0.4, random_state=1)

#データの標準化
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

#学習モデルの作成
clf = SVC(C = 1, kernel = 'rbf')
clf.fit(X_train_std, y_train)

score = clf.score(X_test_std, y_test)
print("{:.3g}".format(score))

# ラベルの仕分けが終わっていない！！