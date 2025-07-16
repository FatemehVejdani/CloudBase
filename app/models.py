from peewee import *
from playhouse.pool import PooledMySQLDatabase
import secrets
import string

temp_db = PooledMySQLDatabase(
    'mysql',
    user='root',
    password='root123',
    host='localhost'
)

with temp_db.connection_context():
    temp_db.execute_sql("CREATE DATABASE IF NOT EXISTS userdatabase CHARACTER SET utf8mb4")


db = PooledMySQLDatabase(
    'userdatabase',
    user='root',
    password='root123',
    host='localhost',
    max_connections=8,
    stale_timeout=300,
)

class User(Model):
    username=CharField(max_length=100)
    password=CharField(max_length=100)
    is_admin=BooleanField(default=False)
    class Meta:
        database=db


class DBinfo(Model):
    user = ForeignKeyField(User, backref='databases')
    db_name=CharField(max_length=100)
    db_user=CharField(max_length=100)
    db_pass=CharField(max_length=100)
    class Meta:
        database = db


def random_str(prefix, length=6):
    chars = string.ascii_lowercase + string.digits
    return prefix + ''.join(secrets.choice(chars) for _ in range(length))

def random_pass(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(chars) for _ in range(length))




def Base_new():
    db_name = random_str('db_')
    db_user = random_str('user_')
    db_pass = random_pass()

    with temp_db.connection_context():
        temp_db.execute_sql(f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET utf8mb4")
        temp_db.execute_sql(f"CREATE USER IF NOT EXISTS '{db_user}'@'localhost' IDENTIFIED BY '{db_pass}'")
        temp_db.execute_sql(f"GRANT ALL PRIVILEGES ON {db_name}.* TO '{db_user}'@'localhost'")
        temp_db.execute_sql("FLUSH PRIVILEGES")

    peewee_db = PooledMySQLDatabase(
        db_name,
        user=db_user,
        password=db_pass,
        host='localhost',
        max_connections=8,
        stale_timeout=300
    )


    class Base(Model):
        volume = CharField(max_length=100)
        cores = IntegerField()
        location = CharField(max_length=100)
        domain = CharField(max_length=255)

        class Meta:
            database = peewee_db


            
    peewee_db.connect()
    peewee_db.create_tables([Base])
    peewee_db.close()

    return Base, {
        "db_name": db_name,
        "db_user": db_user,
        "db_pass": db_pass
    }


