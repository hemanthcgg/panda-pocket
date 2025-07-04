from flask import Flask, render_template, request, redirect

# from static.DummyData.data import dummyData, dummyDonut

app=Flask(__name__)


@app.route('/')
def index():
    # pageDate = {
    #     "tasks": dummyData, 
    #     "dummyDonut": dummyDonut, 
    #     "donut_lables" : list(dummyDonut.keys()), 
    #     "donut_values": list(dummyDonut.values())
    # }
    # return render_template('dashboard/dashboard.html', name="Someone", data=pageDate)
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():   
    if request.method == 'POST':
        print('I am here')
        username = request.form['username']
        password = request.form['password']
        # Here you would typically check the credentials against a database
        if username == 'admin' and password == 'hello':
            return redirect('/{{username}}/dashboard')
        else:
            return "Invalid credentials", 401
    return render_template('auth/login.html')

@app.route('/<user>/dashboard')
def dashboard(user):
    print(f"User: {user}")
    # Here you would typically fetch user-specific data from a database
    return render_template('user/dashboard.html', name=user)

if __name__ in "__main__":
    app.run(debug=True)