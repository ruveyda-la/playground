from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def playground():
    return render_template('welcome.html')

@app.route('/play')
def play():
    return render_template('index.html', num=3,color='aqua')    

@app.route('/play/<int:num>')
def playtimes(num):
    return render_template('index.html', num=num, color='aqua')

@app.route('/play/<int:num>/<color>')
def color(color,num):
    
    return render_template('index.html', num=num, color=color)



if __name__=="__main__":
    app.run(debug=True)