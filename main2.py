import numpy as np

list = [0,0,7,5,4, 1, 1, 1, 1, 1, 1,1,1, 1, 1, 2, 3, 4, 5, 7,7]
#      [2, 4, 1, 5, 3, 2]

def compress_row(row):
    total_len = len(row)
    def compress_row_once(lst):
        dex = 0
        out = []
        if lst.count(0) != 0:
            lst.remove(0)
        while dex != len(lst):
            if dex == len(lst)-1:
                out.append(lst[dex])
            elif lst[dex] == lst[dex+1]:
                out.append(lst[dex]+1)
                dex += 1
            elif lst[dex] == 0:
                pass
            else:
                out.append(lst[dex])

            dex += 1
        return out

    row = compress_row_once(row)
    while row != compress_row_once(row):
        row = compress_row_once(row)
    while len(row) != total_len:
        row.append(0)
    return row


print(compress_row(list))