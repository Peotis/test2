from flask import Flask

text = "Elon Musk juga menganjurkan regulasi jejaring sosial dan perlindungan data pribadi pengguna. Dia mengklaim bahwa jejaring sosial mengumpulkan sejumlah besar informasi tentang kita, yang kemudian dapat digunakan untuk memanipulasi pikiran dan perilaku kita"
app = Flask(__name__)

@app.route("/")
def index():
    return '<a href="/random_fact">View some fact here </a> <p href="/secret">View some secret here </p>'

@app.route("/random_fact")
def facts():
    return f'<p>{text}</p>'

@app.route("/secret")
def facts():
    return f'<p>secret</p>'

app.run(debug=True)
