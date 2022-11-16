import sys


class config:
    def __init__(self):
        self.include=''
        self.output=''
    def load(self):
        for i in sys.argv:
            if '-i' in i or '--include' in i:
                self.include=(i.replace('-i=', '')).replace('--include=', '')
            if '-o' in i or '--output' in i:
                self.output=(i.replace('-o=', '')).replace('--output=', '')


