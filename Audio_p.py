import pyaudio
import wave
import os
formato=pyaudio.paInt16
canal=1
frecuencia=44100
chunk=1024
tiempo=5
nombre="grabacion.wav"
## tenemos una instancia en formato audio
audio=pyaudio.PyAudio()

grabar=audio.open(format=formato,
           channels=canal,
           rate=frecuencia,
           input=True,
           frames_per_buffer=chunk)
print(f"Grabando")
frames=[]
for i in range(0,int( 5*frecuencia/chunk)):
    data=grabar.read(chunk)
    frames.append(data)

grabar.stop_stream()
grabar.close()
audio.terminate()
print(f"se termino de grabar")
with wave.open(nombre,"wb") as wf :
    wf.setnchannels(canal)
    wf.setsampwidth(audio.get_sample_size(formato))
    wf.setframerate(frecuencia)
    wf.writeframes(b"".join(frames))

if os.name == 'nt':
    os.system(f"start {nombre}")
else:
    os.system(f"aplay {nombre}")