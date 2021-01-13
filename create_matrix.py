import numpy as np
import scipy
from scipy.sparse import csr_matrix
import pymysql

# Open database connection
db = pymysql.connect("localhost","root","","ir_assignment" )

# prepare a cursor object using cursor() method
cursor = db.cursor()


select_query = "SELECT bookid,`User-ID`,`Book-Rating` FROM new_rating"
cursor.execute(select_query)

ratings_table = cursor.fetchall()




books = [ book for (book , user , rating) in ratings_table]
users = [ user for (book , user , rating) in ratings_table]
rating = [ rating for (book , user , rating) in ratings_table]


sparse_arr = csr_matrix((rating, (users,books) ), shape=(279000, 272000), dtype=np.int8)

scipy.sparse.save_npz('./sparse_matrix.npz', sparse_arr)

print(books[100])