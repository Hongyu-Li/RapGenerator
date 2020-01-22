import re


def validate_input_rhyme(input_rhyme):
    if len(input_rhyme) > 4:
        print('Hey！输入的词语太长了哦～')
        return False
    elif len(re.findall(u'[\u4e00-\u9fff]', input_rhyme)) != len(input_rhyme):
        print('Hey！请输入中文词语哦～')
        return False
    else:
        return True



