import wave 
import numpy as np
name="grabacion.wav"
with wave.open(name,"rb") as wf:
    parametros=wf.getparams()
    frames=wf.readframes(parametros.nframes)
    audio=np.frombuffer(frames,dtype=np.int16)
    amplificado=np.clip(audio*5,-2**16/2,2**16/2-1).astype(np.int16)
    with wave.open("salida.wav","wb") as wf:
        wf.setparams(parametros)
        wf.writeframes(amplificado.tobytes())
        
