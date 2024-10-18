# Filtro de Áudio usando a Transformada de Fourier (FFT) e um filtro Passa-Banda.

## 📋 Introdução 

Este repositório contém um script em Python para processar arquivos de áudio, aplicando a Transformada de Fourier (FFT) e filtrando através de um filtro passa-banda frequências específicas de acordo com os parâmetros definidos.

## 🚩  Funcionalidades

- Carrega um arquivo de áudio (formato `.wav`).
- Aplica a Transformada Rápida de Fourier (FFT) para converter o áudio do domínio do tempo para o domínio da frequência.
- Filtra frequências indesejadas em uma faixa de frequência específica (passa-banda).
- Gera gráficos comparativos da Transformada de Fourier original e filtrada.
- Salva o áudio filtrado em um novo arquivo `.wav`.

## 🛠️ Dependências

Para rodar o script, é necessário ter o Python 3 instalado, além das seguintes bibliotecas:

- `numpy`
- `matplotlib`
- `scipy`

## 📝 Parâmetros de Filtragem
O filtro é configurado para atuar em uma faixa de frequência específica (exemplo: 20 Hz a 250 Hz, para realçar as frequências graves). Esses valores podem ser ajustados diretamente no código, nas variáveis lower_cutoff e upper_cutoff.
## ⚙️ Configuração da plotagem do Gráfico
Os gráficos gerados pelo script permitem a visualização das frequências do áudio antes e depois da filtragem.

### 📈 Ajuste dos Parâmetros do Gráfico:

- **Limite de frequência no eixo X**: O código está configurado para mostrar até 500 Hz no gráfico. Isso pode ser ajustado nas linhas onde `plt.xlim(0, 500)` é usado. Se quiser ver frequências mais altas ou mais baixas, altere o valor máximo de `500`.
  
  ```python
  plt.xlim(0, 500)  # Altere o valor 500 para o limite desejado
  ```

- **Títulos e Rótulos**:
O título, os rótulos do eixo X e Y também podem ser alterados diretamente no código, caso queira personalizar a plotagem.

    ```python
    plt.title('Transformada de Fourier - Faixa de 0 a 500 Hz')
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Magnitude')
    ```

## 📊 Exemplo dos Gráficos 
![](<Assets\image.png>)
- No exemplo acima, foi utilizada a música Believer da banda Imagine Dragons.

## ✅ Conclusão

O projeto **Audio_Filter** oferece uma ferramenta eficaz para a análise e processamento de sinais de áudio utilizando a Transformada de Fourier. Ao permitir a filtragem de frequências específicas, o script é útil em diversas aplicações, como a melhoria da qualidade do som, a remoção de ruídos indesejados e a análise de características espectrais de gravações de áudio.

Além disso, a visualização gráfica das frequências antes e depois da filtragem proporciona uma compreensão clara do impacto da filtragem aplicada. Os usuários podem facilmente modificar os parâmetros de filtragem e a configuração dos gráficos para atender às suas necessidades específicas.
