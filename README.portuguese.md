<p>
  <img  src="https://img.shields.io/github/stars/BEPb/image_to_ascii" />
  <img src="https://img.shields.io/github/contributors/BEPb/image_to_ascii" />
  <img src="https://img.shields.io/github/last-commit/BEPb/image_to_ascii" />
  <img src="https://visitor-badge.laobi.icu/badge?page_id=BEPb.image_to_ascii" />
  <img src="https://img.shields.io/github/languages/count/BEPb/image_to_ascii" />
  <img src="https://img.shields.io/github/languages/top/BEPb/image_to_ascii" />

  <img src="https://img.shields.io/badge/license-MIT-blue.svg?color=f64152" />
  <img  src="https://img.shields.io/github/issues/BEPb/image_to_ascii" />
  <img  src="https://img.shields.io/github/issues-pr/BEPb/image_to_ascii" />
</p>


# Convertendo uma imagem para um arquivo de texto
Leia em outros idiomas: [Русский](README.ru.md), [हिन्दी](README.hindi.md), [中國人](README.chinese.md), [English](README.md)

## Como funciona

Tudo é muito simples: você baixa um arquivo de imagem ou especifica seu link ao executar um script python e
saída, você obtém um arquivo de texto e pode visualizar imediatamente na linha de comando como ele ficará
o resultado da sua conversão.

## Processo para preparar e trabalhar com o bot

* Clone o repositório ou baixe o arquivo do GitHub ou use os seguintes comandos na linha de comando

   ```commandline
   $ cmd
   $ git clone https://github.com/BEPb/image_to_ascii
   $ cd image_to_ascii
   ```

### Aplicando o repositório
* Instale as dependências de um arquivo, para isto, insira o seguinte código na linha de comando:

```shell
$ pip3 install -r requirements.txt
````

* Meio geral de inicializar o programa

```shell
$ python3 img_to_txt_rus.py [file/url] [size]
```

* Argumentos:

```shell
[file/url]: Arquivo local ou uma URL de imagem online.
[size]: A largura do texto de saída em caracteres - um número inteiro, Quanto maior o tamanho, mais clara a imagem.
```

### Exemplo
```shell
$ python3 img_to_txt.py https://i.postimg.cc/t4Cmn7wC/py.png
```

Ao executar este comando, você receberá um arquivo na atual pasta 'texts' chamado `out.txt` e você verá a saída no console:


<img src="./pictures/py.png" alt="Bot logo" width="300" height="356.5">

<img src="./pictures/png.png" alt="Bot logo" width="600" height="600">


## Conversor de vído para texto
O princípio é similar, exceto que o arquivo de texto resultante não existe. 

```commandline
cd C:\Users\root\PycharmProjects\image_to_ascii 
python video_to_txt.py animations\filin.gif 150
```

<img src="./animations/filin.gif" alt="Bot logo" width="800" height="600">

<img src="./animations/gif.gif" alt="Bot logo" width="800" height="600">



### Licença
[Licença MIT](LICENSE)