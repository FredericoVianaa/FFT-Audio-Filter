import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fftpack import fft

# Carregar o arquivo de áudio
samplerate, data = wavfile.read('Músicas/Input/Imagine Dragons - Believer.wav')

# Verificar se o áudio é estéreo ou mono
if len(data.shape) > 1:
    data = data[:, 0]  # Se for estéreo, pegar apenas um canal (canal esquerdo)

# Aplicar a Transformada de Fourier
N = len(data)
T = 1.0 / samplerate
yf = fft(data)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

# Definir os limites do filtro passa-banda
lower_cutoff = 20
upper_cutoff = 250
#20 a 250 - Mostrar apenas Graves
#2000 a 20000 - Mostrar apenas Agudos

# Converter as frequências de corte para índices
lower_index = int(lower_cutoff * N / samplerate)
upper_index = int(upper_cutoff * N / samplerate)

# Filtrar frequências fora do intervalo de 20 Hz a 250 Hz (passa-banda)
yf_filtered = np.copy(yf)
yf_filtered[:lower_index] = 0  # Zerar abaixo de 20 Hz
yf_filtered[upper_index:] = 0  # Zerar acima de 250 Hz

# Criar uma figura para exibir os gráficos lado a lado
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plotar o gráfico da Transformada de Fourier original, limitando a faixa de 0 a 500 Hz
ax1.plot(xf, 2.0/N * np.abs(yf[:N//2]))
ax1.set_title('Transformada de Fourier - Original (0 a 500 Hz)')
ax1.set_xlabel('Frequência (Hz)')
ax1.set_ylabel('Magnitude')
ax1.set_xlim(0, 500)  # Limitar o eixo x até 500 Hz
ax1.grid()

# Plotar o gráfico da Transformada de Fourier filtrada, limitando a faixa de 0 a 500 Hz
ax2.plot(xf, 2.0/N * np.abs(yf_filtered[:N//2]))
ax2.set_title('Transformada de Fourier Filtrada - 20-250 Hz')
ax2.set_xlabel('Frequência (Hz)')
ax2.set_ylabel('Magnitude')
ax2.set_xlim(0, 500)  # Limitar o eixo x até 500 Hz
ax2.grid()

# Exibir os gráficos lado a lado
plt.tight_layout()
plt.show()

# Inverter a Transformada de Fourier para retornar ao domínio do tempo
filtered_data = np.fft.ifft(yf_filtered).real

# Normalizar os dados filtrados para o intervalo de -32768 a 32767 (faixa do áudio PCM)
filtered_data_normalized = np.int16(filtered_data / np.max(np.abs(filtered_data)) * 32767)

# Salvar o áudio filtrado em um novo arquivo WAV
wavfile.write('Músicas/Output/audio_filtrado_graves.wav', samplerate, filtered_data_normalized)

print("Áudio filtrado salvo como 'audio_filtrado_graves.wav'")
