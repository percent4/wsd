import os
import jieba

# 对示例句子分词
#sent = '我今天买了一只小米手机。'
sent = '他早上喝了碗小米粥。'
#sent = '雷军创办了小米公司。'
#sent= '小米的配置怎样？'
wsd_word = '小米'

#sent = '乔布斯是苹果的前任CEO。'
#sent = '苹果营养丰富，好吃好看。'
#sent = '我吃了个苹果。'
#wsd_word = '苹果'

#sent = '火箭的哈登今天表现很好。'
#sent = '钱学森是中国的火箭之父。'
#wsd_word = '火箭'

#sent = '现在的韩国总统是谁？'
#sent = '韩非子是韩国人。'
#wsd_word = '韩国'

jieba.add_word(wsd_word)
sent_cut = list(jieba.cut(sent, cut_all=False))
print(sent_cut)

# 去掉停用词
stopwords = ['我', '你', '它', '他', '她', '了', '是', '的', '啊', '谁', \
             '都', '很', '个', '之', '人', '。', '，', '！', '？']+[wsd_word]
for stopword in stopwords:
    if stopword in sent_cut:
        sent_cut.remove(stopword)

# 读取例句
def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = [_.strip() for _ in f.readlines()]
        return lines

wsd_dict = {}
for file in os.listdir('.'):
    if wsd_word in file:
        wsd_dict[file.replace('.txt', '')] = read_file(file)

for k,v in wsd_dict.items():
    overlap_count = 0
    for word in sent_cut:
        word_count = 0
        for item in v:
            example = list(jieba.cut(item, cut_all=False))
            overlap_count += example.count(word)
            word_count += example.count(word)

        if word_count:
            print(word, word_count)

    print(k, overlap_count)

#print(wsd_dict)