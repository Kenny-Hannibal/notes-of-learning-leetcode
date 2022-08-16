import math
import re


class TextSplitter(object):
    """
    文本分句
    分词应该在子句中进行（词不可能跨句）
    """

    def __init__(self, stops='([，。？?！!；;：:\n ])'):   # 实例化时就将中断的标记插入其中
        """
        通过正则，设置分句的分隔符

        [] 里面设置分隔符，表示或者的意思；()表示split的时候，返回分隔符，主要防止索引错位
        """
        self.stops = stops
        self.re_split_sentence = re.compile(self.stops)  # 提前编译正则，加速，re.compile用于构造正则表达式对象，以这里为例，后续的正则操作都直接以re_split_sentence进行操作，而re.compile括号中的参数则是后续操作的依据，后续调用时，函数括号中填的则是对象，这里括号填的则是依据什么对对象执行相应的操作

    def split_sentence_for_seg(self, content, max_len=512):
        """
        使用正则regex.split分句

        限制子句的最大长度max_len（防止异常数据对分词器产生较大影响），比如像链接这种很长的文本
        """
        sentences = []

        for sent in self.re_split_sentence.split(content):  # 分句，这里的sent就是调用了正则化的split之后产生的分句单元，split是从re_split_sentence调用的，所以所使用的参数对应上面的re.compile(self.stops)，对象则是函数传进来的参数content
            if not sent:  # 跳过空的句子
                continue
            for i in range(math.ceil(len(sent) / max_len)):  # 对子句进行max_len分段，如果sent的长度比max-len要长的话，这个循环就会成立，因为比1大，然后就会对这个子句进行分段
                sent_segment = sent[i * max_len:(i + 1) * max_len]  # 各段子句应该怎么取
                sentences.append(sent_segment)
        return sentences


if __name__ == '__main__':
    text_splitter = TextSplitter()
    content = '我是谁。我在哪里。你又是谁？119.2 。29,220.20元！你说：”我很好！是吗?”'
    print('split sentence for seg\n')
    for i, sent in enumerate(text_splitter.split_sentence_for_seg(content)):    # 这里的enumerate函数起到的是粘合作用，括号中的各个元素赋值到sent中去，而i则自动从0开始计数，呈递增排列
        print('sent:{} {}'.format(i, sent))     # 这里的format则将其合在一起进行打印
    print('\n')
