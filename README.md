# Atcoderとその周辺

## テクニック

- 桁数が多い整数の処理

途中で割り算が入る場合、桁数が大きくなると`float`の精度が保たれなくなる。確実に`int`になる`//`を使うべし
例: ABC139 D  
x: int(n*(n-1)/2)  
o: n*(n-1)//2

