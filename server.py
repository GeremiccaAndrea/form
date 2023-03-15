from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') # L'utente richiede l'home page
def benvenuto():
  return render_template("home.html")

@app.route('/controlla') # L'utente richiede l'home page
def controlla():
  return "pagina di controllo"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)