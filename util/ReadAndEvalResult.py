'''
用来查看存储成txt文本文件形式的PageRank result;
注意nx包和我自己写的算法的结果可能有出入, 这是由于nx没有设定rate, 而我有设定taxation rate=0.8;
'''

persistenceFilename = '/Users/Chen/Desktop/计算社会学/0527_PrSmallWithPypyCompatible_V2.txt'  #存放结果的地址
# persistenceFilename = '/Users/Chen/Desktop/计算社会学/0526_prSmall_nx02.txt'  #存放结果的地址
# persistenceFilename = '/Users/Chen/Desktop/计算社会学/0526_prSmallWithList_my02.txt'  #存放结果的地址
# persistenceFilename = '/Users/Chen/Desktop/计算社会学/pr_small_0525_my01.txt'  #存放结果的地址

def getDictFromFile():
    f = open(persistenceFilename)
    string = f.read()
    return eval(string)


if __name__ == "__main__":
    d = getDictFromFile()
    print(d[118740773])