from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

veriler = []
veri_id = 0
aylik_gelir = 0  # GELİRİ SAKLAYAN DEĞİŞKEN

@app.route('/')
def index():
    return render_template('gelir.html')

@app.route('/basla', methods=['POST'])  # ← BU ARTIK DOĞRU YERDE
def basla():
    global aylik_gelir
    gelir = request.form.get('gelir')
    if gelir:
        aylik_gelir = float(gelir.replace(",", "."))
        return redirect(url_for('form_sayfasi'))
    return redirect(url_for('index'))

@app.route('/form')
def form_sayfasi():
    harcamalar_toplami = sum(float(v['tutar'].replace(",", ".")) for v in veriler)
    kalan_para = aylik_gelir - harcamalar_toplami
    return render_template('form.html', veriler=veriler, kalan=kalan_para)

@app.route('/add', methods=['POST'])
def add():
    global veri_id
    miktar = request.form.get('miktar')
    miktar = miktar.replace(",", ".")

    description = request.form.get('description')

    if miktar and description:
        veriler.append({
            'id': veri_id,
            'tutar': miktar,
            'aciklama': description
        })
        veri_id += 1

    return redirect(url_for('form_sayfasi'))

@app.route('/sil/<int:veri_id>')
def sil(veri_id):
    global veriler
    veriler = [v for v in veriler if v['id'] != veri_id]
    return redirect(url_for('form_sayfasi'))

if __name__ == '__main__':
    app.run(debug=True)
