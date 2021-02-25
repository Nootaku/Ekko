import queue
import numpy as np
from modules.helpers import getQueue, setQueue


def updatePlot(frame, q, lines, plotdata):
    """Function called by matplotlib for each plot update.
    Normally, the audioCallback() happens more often thatn the updatePlot(),
    therefore, the queue tends to contain multiple blocks of audio data.
    """
    # create global variable
    # global plotdata

    while True:
        try:
            # Remove and return an item from the queue.
            data = q.get_nowait()
        except queue.Empty:
            break

        shift = len(data)

        # shift the position of the points 'shift' to the left
        plotdata = np.roll(plotdata, -shift, axis=0)

        # change the value of the 'shift'-latest points to those of
        # the data
        plotdata[-shift:, :] = data

    # lines will be the name of the plot created by the main function
    for column, line in enumerate(lines):
        line.set_ydata(plotdata[:, column])

    return lines
