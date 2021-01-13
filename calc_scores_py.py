import numpy as np
import scipy
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
sparse_matrix = scipy.sparse.load_npz('./sparse_matrix.npz')



similarities_sparse = cosine_similarity(sparse_matrix , dense_output=False)

print(similarities_sparse.getrow(8))
