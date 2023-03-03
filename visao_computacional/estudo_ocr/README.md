Marçal Henrique Moreira  
Discente em Engenharia de Computação pelo IFMG - Campus Bambuí  
GitHub: [github.com/marcalhenrique](https://github.com/marcalhenrique)  
Março, 2023  
---

--- 

<h1> Reconhecimento de texto com OCR e OpenCV </h1>

Documento gerado a partir do estudo de reconhecimento de texto com OCR e OpenCV.


# Introdução
OCR ou Optical Character Recognition (Reconhecimento Óptico de Caracteres) é uma tecnologia capaz de reconhecer e converter caracteres em imagens digitalizadas em texto editável.  
Basicamente é uma técnica de visão computacional que utiliza algoritmos e técnicas de processamento de imagens para identificar e extrair caracteres de uma imagem.  
O OCR é amplamente utilizado em diversas aplicações, como digitalização de documentos, reconhecimento de faturas, processamento de formulários, entre outras.  
Neste estudo será utilizado o Pyteseract, uma biblioteca de OCR escrita em Python, que utiliza o Tesseract OCR Engine, um software de reconhecimento de caracteres de código aberto e também o OpenCV, uma biblioteca de visão computacional.

# 1. OCR com Pyteseract
O Pyteseract é uma biblioteca de OCR escrita em Python que utiliza o Tesseract OCR Engine, um software de reconhecimento de caracteres de código aberto desenvolvido pela Google.  
Com o Pytesseract, é possível realizar o reconhecimento de caracteres em imagens e arquivos PDF, além de poder especificar o idioma dos caracteres a serem reconhecidos.  
Link para a documentação: [pypi.org/project/pytesseract](https://pypi.org/project/pytesseract/)

# 2. OpenCV
OpenCV é uma biblioteca de código aberto voltada para a visão computacional e processamento de imagens.   
A biblioteca oferece diversas funções e algoritmos para o processamento de imagens, incluindo reconhecimento de padrões, detecção de objetos, rastramento de movimento, entre outras. Ela é escrita em C++, mas também possui suporte para outras linguagens de programação, como Python.  
O OpenCV é bastante utilizado em áreas como a robótica, reconhecimento facial, processamento de imagens médicas, entre outras.

# 3. Segmentação de Imagens
Segmentação de imagens é um processo de dividir uma imagem em várias regiões, cada uma representando um objeto ou parte do objeto de interesse. O objetivo da segmentação de imagens é simplificar a representação da imagem, de modo que as informações relevantes possam ser facilmente extraídas e manipuladas.  
A segmentação de imagens é uma técnica fundamental em processamento de imagens e visão computacional. Ela pode ser realizada de diversas maneiras, desde técnicas simples, como limiarização de detecção de bordas, até técnicas mais avançadas, como clustering, segmentação por crescimento de região e segmentação baseada em contorno.

# 5. Anotações
- O OpenCV por padrão utiliza o sistema de canais BGR para representar as cores das imagens, enquanto o Pyteseract utiliza o sistema RGB.
- Até o presente momento o Pytesseract se da melhor com imagens em escala de cinza.
- O PSM (Page Segmentation Mode) é um parâmetro que pode ser passado para o Pytesseract para indicar o modo de segmentação da página. Existe 14 modos de segmentação.
- O PSM pode errar o padrão de segmentação.
- É de suma importância entender como o texto está disposto na imagem, para escolha do padrão correto.
- OSD (Orientation and Script Detection) é uma ferramenta do Tesseract que pode ser utilizada para detectar a orientação e o script de um texto.