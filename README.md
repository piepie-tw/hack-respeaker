# One Days Workshop for Voice Control on Raspberry Pi 

## Intro
In this workshop, we will introudce how to hack [SeeedStudio ReSpeaker 2-Mics HAT](https://www.raspberrypi.com.tw/17528/71001/)
1. Introduction to ReSpeaker 2-Mic HAT
2. What is Linux ALSA
3. Embedded Google Assistant to Pi
4. Hack ReSpeaker 2-Mic HAT

The slide is available on [[speakerdeck] 改造 ReSpeaker 2-MIC HAT](https://speakerdeck.com/piepie_tw/hack-respeaker)


## Environment
[Raspberry Pi 4/2G 超值組](https://piepie.com.tw/product/raspberry-pi-4-model-b-2g-value-pack-pi-4-case-power-supply-microsd-case-hdmi) + [2021-05-07-raspios-buster-armhf.img](https://bit.ly/42iddHA)

## Prerequisite
### Install required package and Python module
```shell  
$ sudo apt-get update --allow-releaseinfo-change
$ sudo apt-get install -y vim git 
$ sudo apt-get install -y python3-pyaudio
$ sudo apt-get install -y sox flac libatlas-base-dev espeak mpg123
$ sudo pip3 install -U SpeechRecognition python-vlc gtts openai
$ sudo ln -s /usr/lib/arm-linux-gnueabihf/libpython3.7m.so.1.0 /usr/lib/arm-linux-gnueabihf/libpython3.5m.so.1.0
$ sudo pip3 install -U yt-dlp

$ sudo pip3 install -U google-cloud-dialogflow
$ sudo pip3 install grpcio-tools
$ sudo pip3 install -I --force-reinstall grpcio
```

### Install ReSpeaker Driver
```shell  
$ cd ~
$ git clone https://github.com/respeaker/seeed-voicecard.git
$ cd seeed-voicecard
$ sudo ./install.sh --compat-kernel
$ sudo reboot
```

## HackMD
[改造ReSpeaker 2-MIC HAT](https://hackmd.io/66rhYfscTFazn5wZzH3Uhg)

## Buy Raspberry Pi and Smeart Speaker Learning Kit
* [[產品] Raspberry Pi 4/2G 超值組](https://piepie.com.tw/product/raspberry-pi-4-model-b-2g-value-pack-pi-4-case-power-supply-microsd-case-hdmi)
* [[產品] 智慧喇叭語音學習套件 v2(支援 ChatGPT)](https://www.piepie.com.tw/30038/pi-smart-speaker-kit-v2)
