#!/usr/bin/python3
import traceback
import codecs
import os


def convert(filename, in_enc="GBK", out_enc="utf-8"):
    try:
        content = codecs.open(filename, encoding=in_enc).read()
        new_content = content
        codecs.open(filename, 'w', out_enc).write(new_content)
        return True
    except:
        traceback.print_exc()
        return False


def convertEncodeTo(path, fileName, out_enc="utf-8"):
    convertFilePath = os.path.join(path, fileName)
    try:
        import chardet
        import codecs
        deChar = {}
        with open(convertFilePath, 'rb') as f:
            deChar = chardet.detect(f.read())
            if deChar['encoding'] == 'UTF-16LE':
                deChar['encoding'] = 'UTF-16'
            if deChar['encoding'] != out_enc:
                print("%s \n    |---->   的编码从 %-10s --> %-10s" % (fileName,deChar['encoding'] ,out_enc))
                convert(convertFilePath, in_enc=deChar['encoding'], out_enc=out_enc)
            else:
                print("%s \n    |---->   的编码为 %-10s 跳过" % (fileName,out_enc))
    except:
        print(convertFilePath)
        traceback.print_exc()
        return False


if __name__ == "__main__":
    from functools import partial
    getPath = os.path.join(os.path.abspath(os.path.pardir), 'srt')
    for root, dirs, files in os.walk(getPath):
        files = list(filter(lambda x: x.split('.')[-1] == 'srt', files))
        if len(files) > 0:
            convertEncodeByRoot = partial(convertEncodeTo, root)
            list(map(convertEncodeByRoot, files))
