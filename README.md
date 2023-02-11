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


# Converting an image to a .txt file
Read in other languages: [Русский](README.ru.md), [हिन्दी](README.hindi.md), [中國人](README.chinese.md)

## How it works?

Everything is very simple: you either download a picture file or specify its link when running a python script, and
output you get a text file, and you can immediately view on the command line how it will look
the result of your conversion.

## Procedure for preparing and working with the bot

* Clone the repository or download the archive from github or using the following commands on the command line

   ```commandline
   $ cmd
   $ git clone https://github.com/BEPb/image_to_ascii
   $ cd image_to_ascii
   ```

### Applying the repository
* Install dependencies from a file, for this, enter the following code in the command line：

```shell
$ pip3 install -r requirements.txt
````

* general form of program launch：

```shell
$ python3 img_to_txt.py [file/url] [size]
```

* arguments:

```shell
[file/url]: Local file path or online image URL.
[size]: The width of the output txt image in characters - an integer, The larger the size, the clearer the picture.
```

### Example
```shell
$ python3 img_to_txt_rus.py https://i.postimg.cc/t4Cmn7wC/py.png
```
By executing this command, you will get a file in the current 'texts' folder named `out.txt` and you will see the output of the line in the console:


<img src="./pictures/py.png" alt="Bot logo" width="300" height="356.5">

<img src="./pictures/png.png" alt="Bot logo" width="600" height="600">


## Video to Text Converter
The principle is similar, except that the resulting text file does not exist.

```commandline
cd C:\Users\root\PycharmProjects\image_to_ascii 
python video_to_txt_rus.py animations\filin.gif 150
```

<img src="./animations/filin.gif" alt="Bot logo" width="800" height="600">

<img src="./animations/gif.gif" alt="Bot logo" width="800" height="600">



### License
MIT lience
