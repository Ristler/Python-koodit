from flask import Flask
isPrime = False

app = Flask(__name__)
@app.route('/alkuluku/<nro>')

def alkuluku(nro):

    nro = int(nro)
    for i in range(2, nro):
        if nro % i == 0:
            isPrime = False
            break
    else:
        if nro < 2:
            isPrime = False
        else:
            isPrime = True

    vastaus = {
        "Number" : nro, "isPrime:" : isPrime
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)