import os
import re

import text_normalize


def make_dict(data_dir):
    word_dict = {}

    for data_file in os.listdir(data_dir):  # 迭代所有文件，利用OS接口，将该文件目录下所有的文件都迭代一遍
        data_path = '{}/{}'.format(data_dir, data_file) # 用format将文件目录地址组装在一起
        for line in open(data_path, encoding='utf-8'):  # 迭代每一行
            line = line.strip()
            if not line:   # 遇到空行跳过
                continue

            # 合并大粒度的实体词
            for entity in re.findall('\[.*?\]\w+', line):   # 通过split(' ')分隔，将entity分隔成各个term,每个term就是一个单独的单词（中国\n），然后再通过\分隔，只取第一个元素即可得到单词部分，再通过join函数将其合并到一起
                # join括号中的[]是将那一大段元素转成列表的意思，最右边的斜杠是回车转行的意思
                new_entity = ''.join([term.split('/')[0] for term in entity[1:entity.index(']')].split('  ')])  + \
                             '/' + entity[entity.index(']') + 1:]    # 通过index函数索引到右括号的下一位
                # print(entity, '->', new_entity)
                line = line.replace(entity, new_entity)

            # 全角转半角
            line = text_normalize.string_q2b(line)

            # 合并连续的nr t
            for continuous_t, _, continuous_nr, _ in re.findall('((\w+/t  ){2,})|((\w+/nr  ){2})', line):
                continuous_t, continuous_nr = continuous_t.strip(), continuous_nr.strip()
                if continuous_t:


                    new_t = ''.join([t.split('/')[0] for t in continuous_t.split('  ')]) + '/t'
                    # print(continuous_t, '->', new_t)
                    line = line.replace(continuous_t, new_t)
                if continuous_nr:
                    new_nr = ''.join([t.split('/')[0] for t in continuous_nr.split('  ')]) + '/nr'
                    # print(continuous_nr, '->', new_nr)
                    line = line.replace(continuous_nr, new_nr)

            # 去除开头
            line = line.split('  ', 1)[1]

            # 统计词库
            for term in line.split('  '):
                word, pos = term.rsplit('/', 1)
                if word not in word_dict:
                    word_dict[word] = {}
                if pos not in word_dict[word]:
                    word_dict[word][pos] = 0
                word_dict[word][pos] += 1
    # 将统计好的字典写入到文件中
    out = open('core_dict_people_daily.txt', 'w', encoding='utf-8')   # 文本路径位置，’w‘是指模式为写入模式
    for word in word_dict:
        i = 0
        for pos in word_dict[word]:
            if i == 0:
                out.write("{}\t{}\t{}\t".format(word,pos,str(word_dict[word][pos])))
                i += 1
            else:
                out.write("{}\t{}\t".format(pos, str(word_dict[word][pos])))
        out.write('\n')


if __name__ == '__main__':
    make_dict('people-daily-1998')

