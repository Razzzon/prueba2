import wave
import numpy as np 
from scipy import signal
import matplotlib.pyplot as plt

with wave.open("salida.wav","rb") as wf:
    parametros=wf.getparams()
    frames=wf.readframes(parametros.nframes)
    audio=np.frombuffer(frames,dtype=np.int16)
    
    fs=parametros.framerate
    frecuencia_nyquist=fs*0.5
    frecuencia_corte=3000

    frecuencia_normalizada=frecuencia_corte/frecuencia_nyquist
    b,a=signal.butter(6,frecuencia_normalizada,btype="low")
    w, h = signal.freqz(b, a, worN=8000, fs=fs)

    # Graficar la respuesta en frecuencia
    plt.figure(figsize=(10, 6))
    plt.plot(w, 20 * np.log10(np.abs(h)), 'b')
    plt.title('Respuesta en Frecuencia del Filtro Pasa Bajo')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Ganancia (dB)')
    plt.grid()
    plt.show()
    audio_filtrado=signal.filtfilt(b,a,audio)
    audio_filtrado=np.clip(audio_filtrado,-2**15,2**15-1).astype(np.int16)
    with wave.open("filtrado.wav","wb") as wff:
        wff.setparams(parametros)
        wff.writeframes(audio_filtrado.tobytes())
