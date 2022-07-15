from itertools import product
import random
import networkx as nx  # https://networkx.org/documentation/stable/index.html

def print_input_data(data: list):
    # 入力表示
    print('入力表示（左から希望度が高い順）。あってますか？')
    for (name, pref) in data:
        s = ', '.join(pref)
        print(f'{name:10} {s}')

def print_result(result: list):
    # 結果表示
    print('\n結果')
    for res in map(sorted, result):
        print(f'{res[1]} -> {res[0]}')
        
# 重み付き最小マッチングを行う
def matching(edges: list):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    matching = sorted(nx.min_weight_matching(G))
    return matching

def make_edges(data: list):
    edges = list()
    for (name, articles) in data:
        for ((rank, article), num) in product(enumerate(articles), [1,2]):
            edges.append((name, f'{article}_{str(num)}', rank))
    return edges

def run(data: list):
    # 公平になるように、処理の順番をランダムにしている
    # 処理の順番で結果がある程度決まるっぽい
    random.shuffle(data)

    # グラフの辺を作成
    edges = make_edges(data)

    # マッチング
    result = matching(edges)

    return result
    
def main():
    # 入力 
    # n: 人数, m:対象（論文）の数
    # [(名前, [対象１,対象２, ... ])]
    n, m = map(int, input().split())
    data = [(input(), [input() for _ in range(m)]) for _ in range(n)]

    # 入力表示
    print_input_data(data)

    # 実行
    result = run(data)

    # 結果表示
    print_result(result)

if __name__ == '__main__':
    main()
