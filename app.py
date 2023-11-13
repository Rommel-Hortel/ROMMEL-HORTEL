from flask import Flask

app = Flask(__name__)
studentlist:list = [
	{
		"idno":"1000",
		"lastname":"durano",
		"firstname":"dennis",
		"course":"bscpe",
		"level":"4",
		
	},	
]
@app.route("/")
def main ()->None:
	return "Hello Flask"
	
if __name__ == "__main__":
	app.run(debug=True)
		
