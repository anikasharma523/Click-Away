from flask import Flask, render_template, url_for, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date, time


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///sitedata.db'
db = SQLAlchemy(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

class Credentials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    last_login = db.Column(db.DateTime, default=datetime.utcnow)
    type = db.Column(db.String(20), nullable=False)
class library_bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    room = db.Column(db.String(20), nullable=False)
    capacity = db.Column(db.Integer)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    reason = db.Column(db.String(200))
    status = db.Column(db.String(20))
class isc_bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    area = db.Column(db.String(20), nullable=False)
    capacity = db.Column(db.Integer)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    reason = db.Column(db.String(200))
    status = db.Column(db.String(20))
class acadblock_bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    area = db.Column(db.String(20), nullable=False)
    capacity = db.Column(db.Integer)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    reason = db.Column(db.String(200))
    status = db.Column(db.String(20))
class sarc_bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    area = db.Column(db.String(20), nullable=False)
    capacity = db.Column(db.Integer)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    reason = db.Column(db.String(200))
    status = db.Column(db.String(20))
class office_bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    faculty = db.Column(db.String(20), nullable=False)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    reason = db.Column(db.String(200))
    status = db.Column(db.String(20))
class shuttle_bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    route = db.Column(db.String(20), nullable=False)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    reason = db.Column(db.String(200))
    status = db.Column(db.String(20))

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        try:
            user=Credentials.query.filter_by(username=username).first()
            if(password==user.password):
                print("got in")
                session["username"] = username
                if(user.type=="client"):
                    return redirect('/client/0')
                else:
                    return redirect('/admin')
            else:
                return 'incorrect password'
        except:
            return 'user not found'
    else:
        return render_template("index.html")


@app.route('/client/<int:service>', methods=['GET','POST'])
def client(service):
    if request.method=="POST":
        if service==1:
            username=session['username']
            room = str(request.form.get("area"))
            capacity = str(request.form.get("capacity"))
            Date = str(request.form.get("onDate"))
            Date = Date.split('-')
            Date = date(int(Date[0]),int(Date[1]),int(Date[2]))
            Time = str(request.form.get("duration"))
            Time = Time.split(':')
            Time = time(int(Time[0]),int(Time[1]),0)
            reason = str(request.form.get("message"))
            newRequest = isc_bookings(username=username,area=room,capacity=capacity,date=Date,time=Time,reason=reason,status="Waiting for Approval")
            db.session.add(newRequest)
            db.session.commit()
            return redirect('/client/0')
        elif service==2:
            username=session['username']
            room = str(request.form.get("room"))
            capacity = str(request.form.get("capacity"))
            Date = str(request.form.get("date"))
            Date = Date.split('-')
            Date = date(int(Date[0]),int(Date[1]),int(Date[2]))
            Time = str(request.form.get("time"))
            Time = Time.split(':')
            Time = time(int(Time[0]),int(Time[1]),0)
            reason = str(request.form.get("message"))
            newRequest = library_bookings(username=username,room=room,capacity=capacity,date=Date,time=Time,reason=reason,status="Waiting for Approval")
            db.session.add(newRequest)
            db.session.commit()
            return redirect('/client/0')
        elif service==3:
            username=session['username']
            room = str(request.form.get("room"))
            capacity = str(request.form.get("capacity"))
            Date = str(request.form.get("date"))
            Date = Date.split('-')
            Date = date(int(Date[0]),int(Date[1]),int(Date[2]))
            Time = str(request.form.get("time"))
            Time = Time.split(':')
            Time = time(int(Time[0]),int(Time[1]),0)
            reason = str(request.form.get("message"))
            newRequest = acadblock_bookings(username=username,area=room,capacity=capacity,date=Date,time=Time,reason=reason,status="Waiting for Approval")
            db.session.add(newRequest)
            db.session.commit()
            return redirect('/client/0')
        elif service==4:
            username=session['username']
            room = str(request.form.get("room"))
            capacity = str(request.form.get("capacity"))
            Date = str(request.form.get("date"))
            Date = Date.split('-')
            Date = date(int(Date[0]),int(Date[1]),int(Date[2]))
            Time = str(request.form.get("time"))
            Time = Time.split(':')
            Time = time(int(Time[0]),int(Time[1]),0)
            reason = str(request.form.get("message"))
            newRequest = sarc_bookings(username=username,area=room,capacity=capacity,date=Date,time=Time,reason=reason,status="Waiting for Approval")
            db.session.add(newRequest)
            db.session.commit()
            return redirect('/client/0')
        elif service==5:
            username=session['username']
            faculty = str(request.form.get("prof"))
            Date = str(request.form.get("date"))
            Date = Date.split('-')
            Date = date(int(Date[0]),int(Date[1]),int(Date[2]))
            Time = str(request.form.get("time"))
            Time = Time.split(':')
            Time = time(int(Time[0]),int(Time[1]),0)
            reason = str(request.form.get("message"))
            newRequest = office_bookings(username=username,faculty=faculty,date=Date,time=Time,reason=reason,status="Waiting for Approval")
            db.session.add(newRequest)
            db.session.commit()
            return redirect('/client/0')
        elif service==6:
            username=session['username']
            route = str(request.form.get("route"))
            Date = str(request.form.get("date"))
            Date = Date.split('-')
            Date = date(int(Date[0]),int(Date[1]),int(Date[2]))
            Time = str(request.form.get("time"))
            Time = Time.split(':')
            Time = time(int(Time[0]),int(Time[1]),0)
            reason = str(request.form.get("message"))
            newRequest = shuttle_bookings(username=username,route=route,date=Date,time=Time,reason=reason,status="Waiting for Approval")
            db.session.add(newRequest)
            db.session.commit()
            return redirect('/client/0')
    elif request.method=="GET":
        if service==0:
            reqs1 = isc_bookings.query.filter_by(username=session['username']).all()
            reqs2 = library_bookings.query.filter_by(username=session['username']).all()
            reqs3 = acadblock_bookings.query.filter_by(username=session['username']).all()
            reqs4 = sarc_bookings.query.filter_by(username=session['username']).all()
            reqs5 = office_bookings.query.filter_by(username=session['username']).all()
            reqs6 = shuttle_bookings.query.filter_by(username=session['username']).all()
            return render_template("client.html", username=session['username'],  requestsISC=reqs1, requestsLib=reqs2, requestsAcad=reqs3, requestsSarc=reqs4, requestsOffice=reqs5, requestsShuttle=reqs6)
        elif service==1:
            return "get"
        elif service==8:
            session['username']=None
            return redirect('/')
    else:
        return render_template("client.html", username=session['username'])

@app.route('/admin',methods=['GET','POST'])
def admin():
    if request.method=='POST':
        pass
    else:
        reqs1 = isc_bookings.query.order_by(isc_bookings.username).all()
        reqs2 = library_bookings.query.order_by(library_bookings.username).all()
        reqs3 = acadblock_bookings.query.order_by(acadblock_bookings.username).all()
        reqs4 = sarc_bookings.query.order_by(sarc_bookings.username).all()
        reqs5 = office_bookings.query.order_by(office_bookings.username).all()
        reqs6 = shuttle_bookings.query.order_by(shuttle_bookings.username).all()
        return render_template('admin.html', requestsISC=reqs1, requestsLib=reqs2, requestsAcad=reqs3, requestsSarc=reqs4, requestsOffice=reqs5, requestsShuttle=reqs6)
@app.route('/update/<int:service>', methods=['GET','POST'])
def update(service):
    if request.method=='POST':
        if session["username"]!="admin":
            return "Error: Unauthorized Access!"
        else:
            if service==1:
                for id in list(request.form):
                    record = isc_bookings.query.filter_by(id=id).one()
                    record.status=request.form.get(id)
                    db.session.commit()
            elif service==2:
                for id in list(request.form):
                    record = library_bookings.query.filter_by(id=id).one()
                    record.status=request.form.get(id)
                    db.session.commit()
            elif service==3:
                for id in list(request.form):
                    record = acadblock_bookings.query.filter_by(id=id).one()
                    record.status=request.form.get(id)
                    db.session.commit()
            elif service==4:
                for id in list(request.form):
                    record = sarc_bookings.query.filter_by(id=id).one()
                    record.status=request.form.get(id)
                    db.session.commit()
            elif service==5:
                for id in list(request.form):
                    record = office_bookings.query.filter_by(id=id).one()
                    record.status=request.form.get(id)
                    db.session.commit()
            elif service==6:
                for id in list(request.form):
                    record = shuttle_bookings.query.filter_by(id=id).one()
                    record.status=request.form.get(id)
                    db.session.commit()
            return redirect('/admin')
    else:
        return "Error: Unauthorized Access!"

if __name__=="__main__":
    app.run(debug=True)

"""<h2>Login</h2>
<form action="/login" method="POST">
  <label for="username">Username: </label>
  <input type="text" name="username" id="username">
  <br>
  <label for="password">Password: </label>
  <input type="password" name="password" id="password">
  <br>
  <input type="submit" name="submit" id="submit" value="Login">
</form>
"""
