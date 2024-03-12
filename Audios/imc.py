from moviepy.editor import VideoFileClip
import os

def cortar_audio(video_path, output_folder):
    # Carregar o vídeo
    video = VideoFileClip(video_path)
    
    # Duração total do vídeo em segundos
    duracao_total = video.duration
    
    # Duração de cada segmento de áudio em segundos (10 minutos)
    duracao_segmento = 10 * 60
    
    # Calcular o número total de segmentos
    num_segmentos = int(duracao_total // duracao_segmento)
    
    # Criar a pasta de saída, se ainda não existir
    os.makedirs(output_folder, exist_ok=True)
    
    audios_cortados = []
    
    for i in range(num_segmentos):
        # Calcular o tempo de início e fim do segmento
        inicio = i * duracao_segmento
        fim = inicio + duracao_segmento
        
        # Cortar o áudio
        segmento_audio = video.subclip(inicio, fim).audio
        
        # Salvar o áudio cortado
        output_path = os.path.join(output_folder, f'segmento_{i}.mp3')
        segmento_audio.write_audiofile(output_path, codec='mp3')
        
        audios_cortados.append(f'segmento_{i}.mp3')

    # Lidar com o último segmento, que pode ter uma duração diferente
    inicio_ultimo = num_segmentos * duracao_segmento
    fim_ultimo = duracao_total
    segmento_audio_ultimo = video.subclip(inicio_ultimo, fim_ultimo).audio
    output_path_ultimo = os.path.join(output_folder, f'segmento_{num_segmentos}.mp3')
    segmento_audio_ultimo.write_audiofile(output_path_ultimo, codec='mp3')
    
    audios_cortados.append(f'segmento_{num_segmentos}.mp3')

    return audios_cortados
