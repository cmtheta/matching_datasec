from itertools import product
import random
import networkx as nx  # https://networkx.org/documentation/stable/index.html

# 重み付き最小マッチングを行っている
def matching(edges: list):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    matching = sorted(nx.min_weight_matching(G))
    return matching

def make_edges(hopes: list):
    # 公平になるように、処理の順番をランダムにしている
    # 処理の順番で結果がある程度決まるっぽい
    random.shuffle(hopes)

    edges = list()
    for (name, articles) in hopes:
        for ((rank, article), num) in product(enumerate(articles), [1,2]):
            edges.append((name, f'{article}_{str(num)}', rank+1))
    return edges

def main():
    # 入力 (名前,(論文１,論文２,論文３))
    hopes = [(input(),(input(), input(), input())) for i in range(6)]

    # グラフの辺を作成
    edges = make_edges(hopes)

    # マッチング
    result = matching(edges)

    # 入力表示（左から希望が高い順）
    print('入力表示（左から希望が高い順）。あってますか？')
    for hope in hopes:
        print(f'{hope[0]} {hope[1][0]}   {hope[1][1]}   {hope[1][2]}')

    # 結果表示
    print('\n結果')
    for res in map(sorted, result):
        print(f'{res[1]} -> {res[0]}')

if __name__ == '__main__':
    main()
