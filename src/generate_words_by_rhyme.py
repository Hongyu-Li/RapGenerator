import pandas as pd
from pandas.errors import DtypeWarning
from pip._vendor.distlib.compat import raw_input
from pypinyin.style._utils import get_finals
from pypinyin import lazy_pinyin
from src.utils import validate_input_rhyme
import numpy as np
import ast
import sys
import warnings
warnings.simplefilter(action='ignore', category=DtypeWarning)


def generate_words_by_rhyme(input_word):
    rhymes_df = pd.read_csv('./dataset/rhymes-table.csv', sep=',', header=0, encoding='utf-8')
    rhymes_df = rhymes_df.iloc[:, 1:]
    word_rhyme = ''
    for rhyme in lazy_pinyin(input_word):
        rhyme_without_tone = get_finals(rhyme, strict=False)
        word_rhyme += rhyme_without_tone + "'"
    word_rhyme = word_rhyme[0:-1]
    if word_rhyme in rhymes_df.columns:
        rhymes_without_nan = [i for i in list(rhymes_df[word_rhyme]) if i == i]
        np.random.shuffle(rhymes_without_nan)
        corresponding_rhyme = [ast.literal_eval(i)[0] for i in rhymes_without_nan]
        corresponding_frequency = np.asarray([ast.literal_eval(i)[1] for i in rhymes_without_nan])
        normalized_frequency = corresponding_frequency - np.min(corresponding_frequency) / np.max(corresponding_frequency) - np.min(corresponding_frequency)
        sample_num = min(3, len(corresponding_rhyme))
        words = np.random.choice(corresponding_rhyme, size=sample_num, replace=False, p=normalized_frequency)
        print('匹配的韵脚是：')
        for word in words:
            print(word)
    else:
        print('Sorry! 好像没有找到押韵的词语哦～')



if __name__ == '__main__':
    input_word = raw_input("请输入一个中文词语（不超过四个字哟～）: ")
    if validate_input_rhyme(input_word):
        generate_words_by_rhyme(input_word)
    else:
        sys.exit()
