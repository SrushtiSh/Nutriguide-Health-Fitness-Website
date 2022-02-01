from flask  import Flask,render_template,request
app=Flask(__name__)
app.static_folder='templates/assets'
@app.route("/")
@app.route("/home")
def home():
	return render_template("Grill_home.html")
@app.route("/adminlogin")
def adminlogin():
	return render_template("log_in.html")

@app.route("/doLogin",methods=["POST"])
def doLogin():
	if request.method=="POST":
		credentials = request.form
		adminId = credentials["idTb"] 
		adminPass = credentials["passTb"]
		if(adminId=="9930" and adminPass=="******"):
			return render_template("user_input.html")
		else:
			print("hey invalid password enetered please enter right password its very easy ....have more badams ! ")
			return "hey invalid password enetered please enter right password its very easy ....have more badams ! "

if __name__=='__main__':
    app.run(debug=True)
