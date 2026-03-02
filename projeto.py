import whisper
import os
import sys
import subprocess

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
ffmpeg_bin = os.path.join(diretorio_atual, "ffmpeg", "bin")
ffmpeg_exe = os.path.join(ffmpeg_bin, "ffmpeg.exe")

os.environ["PATH"] = ffmpeg_bin + os.pathsep + os.environ["PATH"]

print(f"--- DIAGNÓSTICO ---")
print(f"Pasta do projeto: {diretorio_atual}")
print(f"Buscando executável em: {ffmpeg_exe}")

try:
    resultado = subprocess.run([ffmpeg_exe, "-version"], capture_output=True, text=True, check=True)
    print("✅ FFmpeg detectado e funcionando com sucesso!")
except Exception as e:
    print(f"❌ ERRO CRÍTICO: O Windows não permitiu abrir o FFmpeg.")
    print(f"Detalhe técnico: {e}")
print(f"-------------------\n")

def transcrever_audio(caminho_audio):

    if not os.path.exists(caminho_audio):
        print(f"Erro: O arquivo '{caminho_audio}' não foi encontrado!")
        return

    print("Carregando modelo de IA... Aguarde.")
    model = whisper.load_model("base")
    
    print(f"Iniciando a transcrição de: {caminho_audio}")
    result = model.transcribe(caminho_audio, fp16=False, language="pt")
    
    nome_txt = os.path.splitext(caminho_audio)[0] + ".txt"
    with open(nome_txt, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    print("\n" + "="*30)
    print("SUCESSO!")
    print(f"Texto salvo em: {nome_txt}")
    print("="*30)

arquivo_de_audio = "teste_transcricao.m4a" 
transcrever_audio(arquivo_de_audio)