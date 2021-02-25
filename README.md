# Ekko

## Project description
Ekko is a project born from my passion of music and my will to learn programming with a hands-on approach. My objective is to dive in the world of Music Information Retrieval (MIR), Audio Processing and Machine Learning (ML). I want to do this while doing something that might be useful to me (and other musicians): scoring audio files.

As I have very quickly discovered, the documentation for handeling audio files in python is very limited. This is why I have decided to document all my steps one by one in this project.

The final objective is to create a program capable of analyzing an audio-file and writing a score for each instrument in the file. I know this is very unlikely to become a reality, but hey: "Aim for the moon, reach the stars" - right ?

### Dependencies
We will discover **Librosa 0.8.0**. This version is important as there have been minor changes between 0.7 and 0.8 that made some of the existing documentation obsolete.

## Documentation has been compiled from the following sources
- [musicinformationretrieval.com](https://musicinformationretrieval.com/index.html)

## First approach to reading, visualizing, writing and playing audio
*Please go to the file: '01_readAudio.ipynb'*

### Reading
The original approach to reading any file in python is to use the `open()` function. The underlying idea is to open a file, read its content in binary, push the binary to a numpy array and analyze the data from the array.

This workflow ended up being correct. However, **[Librosa](https://librosa.org/doc/0.8.0/index.html)** (package designed for music and audio analysis) already provides with a shortcut to this solution. The `librosa.load(path)` function returns both an array-like object as well as the sample rate of the path as an integer.

### Visualizing
Visualizing an audio file is very straightforward. Using **[matplotlib](https://matplotlib.org/tutorials/index.html)** we simpely graph the data of the array-like objects that we have generated when reading the file.

Again, a nice addition to the **Librosa** package is the `librosa.display.waveplot(data, samplerate)` method that allows to make the visualization easier. (documentation [here](https://librosa.org/doc/0.8.0/generated/librosa.display.waveplot.html))

Finally, can also call the `librosa.display.specshow(data, samplerate)` that allows us to visualize the specrogram of the audio file. (documentation [here](https://librosa.org/doc/0.8.0/generated/librosa.display.specshow.html))

### Writing

Writing audio is done with a dependency of Librosa called **[PySoundFile](https://librosa.org/doc/0.8.0/ioformats.html?highlight=write#write-out-audio-files)** and its method `soundfile.write(path, data, samplerate)`.

### Playing

Playing audio is done with **IPython** built-in `IPython.display` module. This module contains the `Audio(path)` function that generates a player in a Jupyter notebook.



