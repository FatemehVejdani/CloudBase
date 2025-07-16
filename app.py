from flask import Flask, render_template, redirect, url_for, request, session, flash
from models import *
from utils import *


app=Flask(__name__)
app.secret_key ="secrestkey"

@app.before_request
def _connect_db():
    db.connect(reuse_if_open=True)

@app.teardown_request
def _close_db(exc):
    if not db.is_closed():
        db.close()



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        create_table(User)
        create_table(DBinfo)
        User.create(username=request.form['username'],password = request.form['password'])
        return redirect(url_for('login'))
    
    return render_template('signup.html')




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        try:
            user = User.get(User.username == username)

            if user.password == password:
                session['user_id'] = user.id
                session['username'] = user.username
                session['is_admin'] = user.is_admin
                return redirect(url_for('dashboard'))  


        except DoesNotExist:
            flash('کاربری با این نام یافت نشد.', 'danger')

    return render_template('login.html')




@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        Base, db_info = Base_new()
        user = User.get(User.username == session['username'])
        db_info['user'] = user
        DBinfo.create(**db_info)


        Base.create(
            volume=request.form['volume'],
            cores=request.form['cores'],
            location=request.form['location'],
            domain=request.form['domain']
        )
        return redirect(url_for('dashboard'))

    return render_template('home.html')



@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    user = User.get(User.username == username)
    dbinfos = DBinfo.select().where(DBinfo.user == user)

    all_data = []

    for dbinfo in dbinfos:
        peewee_db = PooledMySQLDatabase(
            dbinfo.db_name,
            user=dbinfo.db_user,
            password=dbinfo.db_pass,
            host='localhost'
        )

        class Base(Model):
            volume = CharField(max_length=100)
            cores = IntegerField()
            location = CharField(max_length=100)
            domain = CharField(max_length=255)

            class Meta:
                database = peewee_db

        peewee_db.connect()
        try:
            base_data = []
            for record in Base.select():
                base_data.append({
                    "volume": record.volume,
                    "cores": record.cores,
                    "location": record.location,
                    "domain": record.domain
                })

            all_data.append({
                "db_name": dbinfo.db_name,
                "db_user": dbinfo.db_user,
                "db_pass": dbinfo.db_pass,
                "base_records": base_data
            })
        finally:
            peewee_db.close()

    return render_template("dashboard.html", data=all_data)



# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))



app.run(debug=True)