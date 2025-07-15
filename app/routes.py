from flask import Blueprint, redirect, url_for, session, request

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))
    
    
    
@main_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

    

@main_bp.route('/dashboard')
def dashboard():
    if 'username' not in session:    
        
        
        
        
@main_bp.route('/home', methods=['GET', 'POST'])
def home():
    if 'username' not in session:
        
        
        
@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    
    
    
    
@main_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':