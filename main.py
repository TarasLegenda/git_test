from flask import Flask, render_template, url_for, request
from proxy import get_proxy
from dos import dos

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		n_prox = request.form['n_prox']
		n_loop = request.form['n_loop']
		url = request.form['url']
		
		dos(url=url, number=int(n_loop), proxy_list=get_proxy(int(n_prox)))
		
		return 1
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)