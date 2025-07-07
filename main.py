from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
# from static.DummyData.data import dummyData, dummyDonut

# Initialize Flask app
app=Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///panda.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning

# Create SQLAlchemy instance
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, )
    user_id = db.Column(db.String(80), primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email_id = db.Column(db.String(80), unique=True, nullable=False)
    mobile_no = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f'<User {self.user_id}>'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print('I am here')
        user_id = request.form['user_id']
        password = request.form['password']
        email_id = request.form['email_id']
        mobile_no = request.form['mobile_no']

        # Check if user_id already exists
        existing_user = User.query.filter_by(user_id=user_id).first()
        
        if existing_user:
            return "User ID already exists", 400
        # Create a new user instance
        new_user = User(user_id=user_id, password=password, email_id=email_id, mobile_no=mobile_no)
        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    
    return render_template('auth/register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():   
    if request.method == 'POST':
        print('I am here')
        username = request.form['username']
        password = request.form['password']
        # Here you would typically check the credentials against a database
        if username == 'admin' and password == 'hello':
            return redirect('/dashboard')
        else:
            return "Invalid credentials", 401
    return render_template('auth/login.html')

@app.route('/dashboard')
def dashboard(user):
    print(f"User: {user}")
    # Here you would typically fetch user-specific data from a database
    return render_template('user/dashboard.html', name=user)

if __name__ in "__main__":
    with app.app_context():  # Needed for DB operations
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)