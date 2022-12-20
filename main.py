from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def reference():
  return render_template('reference.html')



app.run()