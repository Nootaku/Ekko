import queue
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from modules.callback import updatePlot
from modules.helpers import setQueue, getQueue

# Device info:
device = sd.default.device
device_info = sd.query_devices('default', 'input')

# Sample info:
sr = device_info['default_samplerate']  # Sampler rate
interval = 30    # Minimum time between plot updates (in ms)
downsample = 10  # display every nth sample
duration = 200   # Window duriation size (in ms)
blocksize = 1024 * 4
length = int(duration * sr / (1000 * downsample))

# Channels info
channels = [1]
channel_map = [c - 1 for c in channels]
n = len(channels)

# Initiate Queue
q = queue.Queue()


def audioCallback(indata, frames, time, status):
    """Callback function. Called from a separate thred for each audio block.

    indata is a np.array()
    np.array()[::n, x] means that for the entire array, we will keep only all
    nth samples of the xth dimension (or column)
    """
    # Put item into the queue.
    q.put(indata[::downsample, channel_map])


def tuner():
    """
    sr: Sample rate
    channels: Input channels to be used
    d: Window duration size (in ms)
    update: Minimum time between plot updates (in ms)
    downsample: Display every nth sample
    """
    # Create initial plot data
    global plotdata
    global lines
    plotdata = np.zeros((length, n))

    # Create plot
    fig, ax = plt.subplots()
    lines = ax.plot(plotdata)

    # If we need to retreive info from multiple channels:
    if n > 1:
        ax.legend(
            ['Channel {}'.format(c) for c in channels],
            loc="lower left",
            ncol=len(channels)
        )

    # Set plot visual information
    ax.axis((0, len(plotdata), -1, 1))
    ax.yaxis.grid(True)
    ax.tick_params(bottom=False, top=False, labelbottom=False,
                   right=False, left=True, labelleft=True)
    ax.xaxis.set_view_interval(0, duration)
    fig.tight_layout(pad=1)

    # Create an Audio Stream Object
    stream = sd.InputStream(
        samplerate=44100,
        blocksize=blocksize,
        device=None,
        channels=None,
        dtype=None,
        latency=None,
        extra_settings=None,
        callback=audioCallback,
        finished_callback=None,
        clip_off=None,
        dither_off=None,
        never_drop_input=None,
        prime_output_buffers_using_stream_callback=None
    )

    # Create a Plot-Update caller
    """class matplotlib.animation.FuncAnimation(
        fig, func, frames=None,
        init_func=None, fargs=None, save_count=None,
        *, cache_frame_data=True, **kwargs)
    """
    ani = FuncAnimation(
        fig,              # the figure that will be animated
        func=updatePlot,       # the function used to animate the plot
        interval=interval,
        blit=True,         # is blitting used to optimize drawing ?
        fargs=(q, lines, plotdata,)
    )

    with stream:
        plt.show()


if __name__ == "__main__":
    tuner()
