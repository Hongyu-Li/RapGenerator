import pandas as pd
from pypinyin.style._utils import get_finals


def get_rhymes_table(input_filepath, output_filepath):
    dataset = pd.read_csv(input_filepath, header=None, sep='\t', encoding='utf-8',
                          names=['words', 'pronunciation', 'frequency'])
    rhymes = {}
    for _, data in dataset.iterrows():
        word_rhyme = ''
        for character in data['pronunciation'].split("'"):
            rhyme_with_tone = get_finals(character, strict=False)
            rhyme_without_tone = rhyme_with_tone[0:-1]
            word_rhyme += rhyme_without_tone + "'"
        word_rhyme = word_rhyme[0:-1]
        if word_rhyme in rhymes.keys():
            rhymes[word_rhyme].append([data['words'], data['frequency']])
        else:
            rhymes[word_rhyme] = [[data['words'], data['frequency']]]

    rhymes_df = pd.DataFrame({key:pd.Series(value) for key, value in rhymes.items()})
    rhymes_df.to_csv(output_filepath,sep=",", header=True)


if __name__ == "__main__":
    get_rhymes_table('./words-table.txt', './rhymes-table.csv')

