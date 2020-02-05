#%%
O = input()
E = input()

import itertools
passwd = [o+e for o, e in itertools.zip_longest(O, E, fillvalue='')]
passwd = ''.join(passwd)
print(passwd)