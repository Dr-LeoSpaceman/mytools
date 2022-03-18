import mysql.connector as mysql
from os import environ

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = environ["PASSWRD"],
    database="dev"
)
conn = db.cursor()
query = "SELECT * FROM devdata;"

logs = []
with conn as cur:
    cur.execute(query)
    results = cur.fetchall()
    for data in results:
        email = data[1]
        success = data[2]
        failed = data[3]
        get_total = f"total = ({success} + {failed}) / {failed}"
        exec(get_total, globals())
        logs.append(f"User {email} -> {total}")


with open("/tmp/logs.log", "w") as f:
    for log in logs:
        f.write(f"{log}\n")
