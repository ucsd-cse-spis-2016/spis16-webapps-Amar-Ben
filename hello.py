from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hey dude"

@app.route('/ftoc')
def renderResult():
    try:
        print "request.args['fTemp']",request.args['fTemp']
        ftemp = float(request.args['fTemp'])
        ctemp = ftoc(ftemp)
        return render_template('celsiusResult.html', fTemp=ftemp, cTemp=ctemp)
    except ValueError:
        return "Sorry: something went wrong."

def ftoc(ftemp):
   return (ftemp-32.0)*(5.0/9.0)

if __name__ == "__main__":
    app.run(debug=False)
