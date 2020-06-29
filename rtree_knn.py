import pickle
import time
from rtree import index
from Secuential_KNN.py import read_Face

QUERY = read_Face('./unknownFaces/jennifer_lopez.jpg')


def parse_row(d):
    l = d
    new_list = [x for pair in zip(l,l) for x in pair]
    return tuple(new_list)

def load_n(n):
    new_list = {}
    with open("result.pkl", "rb") as f:
        data = pickle.load(f)
        count = 0 
        for d in data:
            if (count == n):
                break
            new_list[d[0]] = parse_row(d[1])
            count += 1

    p = index.Property()
    p.dimension = 128
    p.dat_extension = "data"
    p.idx_extension = "index"
    idx = index.Index('3d_index' + str(n),properties=p, interleaved = False)
    c_id = 0
    for key in new_list:
        idx.insert(c_id, new_list[key], key)
        c_id+=1

    return idx


list_sizes = [100, 200, 400, 800, 1600, 3200, 6400, 12800] 
for n in list_sizes:
    idx = load_n(n)
    start_time = time.time()
    res = list(idx.nearest(parse_row(QUERY), 16))
    print("--- %s seconds ---" % (time.time() - start_time))
