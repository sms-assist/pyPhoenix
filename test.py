import pyphoenix

database_url = 'http://149.202.166.145:8765/'
conn = pyphoenix.connect(database_url)

cursor = conn.cursor()

req = "SELECT COLUMN_NAME, DATA_TYPE, NULLABLE " \
"FROM system.catalog " \
"WHERE TABLE_SCHEM = ? " \
"AND table_name = ? " \
"AND COLUMN_NAME is not null"
"ORDER BY ORDINAL_POSITION"


params = ['PROD_FR', 'BI_BI_STATS']

cursor.execute(req, params)
print cursor.fetchall()

