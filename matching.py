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
    order = [0,1,2,3,4,5]
    random.shuffle(order)
    print(f'debug: 処理順{order}\n')

    edges = list()
    for i in order:
        name, articles = hopes[i]
        for rank,article in enumerate(articles):
            edges += [ (name,f'{article}_{str(num+1)}',rank+1) for num in range(2)]
            
    return edges

    
def main():
    hopes = list()
    for _i in range(6):
        # 入力
        hopes.append((input(),(input(), input(), input())))

    # グラフの辺を作成
    edges = make_edges(hopes)

    # マッチング
    result = matching(edges)

    # 結果の並び替え（データの整形）
    result = list(map(sorted, result))

    # 入力表示（左から希望が高い順）
    print('入力表示（左から希望が高い順）。あってますか？')
    for hope in hopes:
        print(f'{hope[0]} {hope[1][0]}   {hope[1][1]}   {hope[1][2]}')

    # 結果表示
    print('\n結果')
    for res in result:
        print(f'{res[1]} -> {res[0]}')

if __name__ == '__main__':
    main()
