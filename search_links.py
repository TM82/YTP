import pandas as pd
import numpy as np

links = pd.read_csv('links5.csv',index_col=0).drop_duplicates(['from','to'])
nodes = pd.read_csv('nodes5.csv',index_col=0)
labels = pd.read_csv('labels5.csv',index_col=0)
nodes = pd.merge(nodes,labels,on='index')

# while(True):
print("Enter the query you want to search\n")
query = input()
node = nodes[nodes['query']==query]
print('-----------------------------------------\n{0}のノード情報'.format(node['query'].values[0]))
if len(node):
    print("名称：  " + node['query'].values[0])
    print("所属:   " + nodes[nodes['index']==node['label'].values[0]]['query'].values[0])
    print("最短ステップ数：  " + str(node['shortest_step'].values[0]))
    # print("その他大学との距離： {0} | {1} | {2} | {3} | {4} ".format(node['from_ut'].values[0],node['from_ky'].values[0],node['from_wa'].values[0],node['from_ko'].values[0],node['from_me'].values[0]))

    next_querys= list(links[links['from']==query]['to'])
    print('-----------------------------------------\nリンク先のノード情報')
    if len(next_querys):
        for next_query in next_querys:
            next_node = nodes[nodes['query']==next_query]
            print("名称：  " + next_query)
            print("所属:   " + nodes[nodes['index']==next_node['label'].values[0]]['query'].values[0])
            print("最短ステップ数  " + str(next_node['shortest_step'].values[0]))
            # print("その他大学との距離： {0} | {1} | {2} | {3} | {4}".format(next_node['from_ut'].values[0],next_node['from_ky'].values[0],next_node['from_wa'].values[0],next_node['from_ko'].values[0],next_node['from_me'].values[0]))

            related_querys = list(links[links['from']==next_query]['to'])
            if len(related_querys):
                print("<<関係が予想される単語>>")
                for related_query in related_querys:
                    related_node = nodes[nodes['query']==next_query]
                    print("{0}: ".format(related_query),end=' ')
                    print(nodes[nodes['index']==related_node['label'].values[0]]['query'].values[0])
                print()
                print('--')
            else:
                print("関係する単語に該当する情報がありません")
                print('--')
    else:
        print("There's no consequent query in this network")
    print()
    print()
else:
    print("There's no such query in this network.")
