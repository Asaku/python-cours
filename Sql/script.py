import _mysql

cnx = _mysql.connect(
                        user='root',
                        host='127.0.0.1',
                        db='chevre'
)
cursor = cnx.cursor()

print(cursor)







