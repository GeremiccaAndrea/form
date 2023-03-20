from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/') # L'utente richiede l'home page
def benvenuto():
  return render_template("form.html")

@app.route('/controlla') # L'utente richiede l'home page
def controlla():
  return "pagina di controllo"

@app.route('/login') # L'utente richiede l'home page
def login():
  nome = request.args.get('nome')
  cognome = request.args.get('cognome')
  
  if nome == 'admin' and cognome == 'xxx123##': 
    return render_template('login.html' , nome = nome , cognome = cognome) 
  else: 
    return render_template('errorePassword.html') 
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)