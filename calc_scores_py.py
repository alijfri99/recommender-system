import numpy as np
import scipy
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
sparse_matrix = scipy.sparse.load_npz('./sparse_matrix.npz')


# print(sparse_matrix.getrow(8))
# print()
# print(sparse_matrix.getrow(278854))

# print(sparse_matrix.nonzero())

# print(corr)
row_8 = sparse_matrix.getrow(254) 

corr = cosine_similarity(row_8,sparse_matrix)
top10 = np.argsort(corr[0])[-10:]
print(cosine_similarity(row_8 ,sparse_matrix.getrow(40795) ))
print(top10)
# for i in range(10000):
#     row = sparse_matrix.getrow(i+9) 
#     # corr = cosine_similarity(sparse_matrix)
#     # corr = np.corrcoef(row,row_8)
#     corr = row_8.dot(row.transpose()).data
#     if len(corr) > 0:
        
#         corr = cosine_similarity(row_8,row)
#         print(f'rownum = {i+9} : correaltion = {corr}')