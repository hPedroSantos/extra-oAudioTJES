from flask import Flask, render_template, request, jsonify, send_from_directory
from imc import cortar_audio
import os

app = Flask(__name__, static_url_path='/static')  # Definindo o caminho para arquivos estáticos

OUTPUT_FOLDER = 'audios_cortados'

@app.route('/')
def index():
    return render_template('site.html')

@app.route('/dividir_audio', methods=['POST'])
def dividir_audio():
    if 'arquivo' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'})
    
    arquivo = request.files['arquivo']
    if arquivo.filename == '':
        return jsonify({'error': 'Nenhum arquivo selecionado'})
    
    # Salvar o arquivo de vídeo temporariamente
    video_path = 'video.mp4'
    arquivo.save(video_path)
    
    # Cortar o áudio do vídeo
    audios_cortados = cortar_audio(video_path, OUTPUT_FOLDER)

    # Retornar os nomes dos arquivos de áudio cortados
    return jsonify({'audios': audios_cortados})

@app.route('/downloads/<path:filename>')
def download_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
