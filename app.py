from flask import Flask, render_template

# Flask uygulamasını başlat
app = Flask(__name__)

# Ana sayfa (/) rotasını tanımla
@app.route('/')
def index():
    # templates/index.html dosyasını render et (göster)
    return render_template('index.html')

# Uygulamayı çalıştır (Sadece bu dosya doğrudan çalıştırıldığında)
if __name__ == '__main__':
    # Debug=True ile hata ayıklama modunu aç
    app.run(debug=True)