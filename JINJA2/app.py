from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def hello_world():

 orang = {'nama': 'ashshiddiq', 'umur':'17thn'}

 komentar = [

  {

   'penulis': {'nama': 'Khalid'},

   'ucapan': 'hai armando, artikel yang bagus'

  },

  {

   'penulis': {'nama': 'Ariqa'},

   'ucapan': 'artikel ini cukup membantu saya'

  }

 ]

 return render_template('index.html', title='Beranda', orang=orang, komentar=komentar)