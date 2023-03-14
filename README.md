# RPM BASED
```
sudo yum install python3
sudo yum install python3-pip
sudo yum install python3-devel portaudio-devel

// Maybe you will need to install RPM fusion repository if you haven't in order to be able to download this package
sudo dnf install ffmpeg
```

# DEB BASED
```
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt-get install python3-dev portaudio19-dev

sudo add-apt-repository universe
sudo apt-get update
sudo apt-get install ffmpeg

```

## Running the script

With the audio file in the folder of the project do:

```
python audioToText.py
```