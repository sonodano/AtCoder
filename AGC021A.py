#%%
in_list = list(map(int, list(str(input()))))

ans = 9 * (len(in_list) - 1) + in_list[0] - 1 # 先頭の位の数を一つ下げて、他が全部9が最大のはず
print(max(ans, sum(in_list))) # そのまま足した方がいいやつ(99とか)もあるので比較
