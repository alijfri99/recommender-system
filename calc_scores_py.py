import numpy as np
import scipy
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
sparse_matrix = scipy.sparse.load_npz('./sparse_matrix.npz')
sparse_matrix.eliminate_zeros()





# for i in range(27678611):
for i in range(1,1000):
    current_row = sparse_matrix.getrow(i) 
    if(current_row.count_nonzero() > 0 ):
        corr = cosine_similarity(current_row,sparse_matrix)
        top10_indices = np.argsort(corr[0])[-11:-2]
        (corr[0]).sort()
        top10_values = (corr[0])[-11:-2]
        # print(f'i = {i} : indices : {top10_indices}')
        # print(f'          values : {top10_values}')


