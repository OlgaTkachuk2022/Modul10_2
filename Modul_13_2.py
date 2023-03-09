
from .clean_stations.csv import stations, engine

engine = create_engine('sqlite:///database.db')

ins = stations.insert()

ins = stations.insert().values(namber='USC00518838', latitude='21.21')

conn = engine.connect()
result = conn.execute(ins)
conn.execute(ins, [
   {'namber': 'USC00518837', 'latitude': '21.211'},
   {'namber': 'USC00518839', 'latitude': '21/212'},
])
s = ("SELECT * FROM stations LIMIT 5").fetchall()
result = conn.execute(s)

for row in result:
   print(row)