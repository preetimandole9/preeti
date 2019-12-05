#  k-nearest neighbors on the Iris Flowers Dataset
from csv import reader


# Load a text file
def load_text(filename):
    data = list()
    with open(filename, 'rt') as textfile:
        file_reader = reader(textfile)
        for obvrow in file_reader:
            if not obvrow:
                continue
            data.append(obvrow)
    return data

# Convert obv string to float
def obvcolumn_string_to_float(data, obvcol):
    for obvrow in data:
        obvrow[obvcol] = float(obvrow[obvcol].strip())


# Convert obv string to integer
def obvcol_string_to_int(data, obvcol):
    cl_val = [obvrow[obvcol] for obvrow in data]
    uniq = set(cl_val)
    res = dict()
    for i, val in enumerate(uniq):    
        res[val] = i
        print('[%s] = %d' % (val, i))
    for obvrow in data:
        obvrow[obvcol] = res[obvrow[obvcol]]
    return res

# Find the minimum and maximum values for each column in the dataset
def data_col_minmax(data):
    col_minmax = list()
    for i in range(len(data[0])):
        col_val = [obvrow[i] for obvrow in dataset]
        col_val_min = min(col_val)
        col_val_max = max(col_val)
        col_minmax.append([col_val_min, col_val_max])
    return col_minmax

# find minimum and maximum  dataset col val
def maxmin_dataset(data, col_maxmin):
    for obvrow in data:
        for i in range(len(obvrow)):
            obvrow[i] = (obvrow[i] - col_maxmin[i][0]) / (col_maxmin[i][1] - col_maxmin[i][0])

# the Euclidean distance 
def euclidean_dist(obvrow1, obvrow2):
    dist = 0.0
    for x in range(len(obvrow1)-1):
        dist += (obvrow1[x] - obvrow2[x])**2
    return (dist)**(1/2)

# find the nearest observations
def get_near_obv(obv_train, ob_test, k):
    dist = list()    
    for obvrow in obv_train:
        distance=euclidean_dist(ob_test,obvrow)
        dist.append((obvrow, distance))
    dist.sort(key=lambda tup: tup[1])
    nearest= list()
    for i in range(k):
        nearest.append(dist[i][0])
    return nearest

#  prediction with nearest observations
def nearest_predict(obv_train, ob_test, k):
    near_obv = get_near_obv(obv_train, ob_test,k)
    out_val = [obvrow[-1] for obvrow in near_obv]
    predict = max(set(out_val), key=out_val.count)
    return predict

# prediction with KNN on Iris Dataset
filename = 'iris.txt'
data = load_text(filename)
for i in range(len(data[0])-1):
    obvcolumn_string_to_float(data, i)
obvcol_string_to_int(data, len(data[0])-1)
# define model parameter
k = 5
# define a new record
obvrow = [5.7,2.9,4.2,1.3]


# find label
l = nearest_predict(data, obvrow, k)
print('obv_row=%s, class: %s' % (obvrow, l))