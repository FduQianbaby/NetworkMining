# apply networkx

import time
import networkx as nx


'''some static vars need to set before pageRank goes'''
# filename = '/Users/Chen/Desktop/计算社会学/largeDataset/data/edges.csv'
filename = '/Users/Chen/Desktop/计算社会学/smallDataset/twitter_combined.csv'
persistenceFilename = '/Users/Chen/Desktop/计算社会学/pr_small_0526_nx01.txt'

linkOut = {1: {2:1, 3:1, 4:1}, 2: {1:1, 4:1}, 3: {1:1}, 4: {2:1, 3:1}}  #本地测试变量a
linkIn = {1: {2:1,3:1}, 2:{1:1,4:1}, 3:{1:1,4:1}, 4:{1:1, 2:1}}
testV = {1: 0, 2: 0, 3: 0, 4: 0}


def retrieveFromTest(G):
    for nodeOut in linkOut.keys():
        for nodeIn in linkOut[nodeOut].keys():
            G.add_edge(nodeOut, nodeIn)


def retrieveFromFile(G):
    global file
    with open(filename) as file:  # 可以理解成if xxx is okay : then do sth;
        for line in file:
            head, tail = [int(x) for x in line.split(',')]
            print(head, tail)
            G.add_edge(head, tail)


if __name__ == "__main__":
    'main part of program'
    beginTime = time.time();
    G = nx.DiGraph()
    retrieveFromTest(G)
    pr = nx.pagerank(G, alpha=0.80)

    # data persistence
    # with open(persistenceFilename) as file:
    #     file.write(str(pr))
    print("PageRank Result:", pr)
    print("elapsed time: ", time.time() - beginTime)