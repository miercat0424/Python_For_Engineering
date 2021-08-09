"""
Blitting is an old computer graphics technique where several graphical bitmaps
are combined into one. This way, only one needed to be updated at a time,
saving the computer from having to redraw the whole scene every time.
Matplotlib allows us to enable blitting in FuncAnimation, but it means we need
to re-write how some of the animate() function works. To reap the true benefits
of blitting, we need to set a static background, which means the axes can’t scale
and we can’t show moving timestamps anymore. This means that you have to
take the good with the bad. So you have to choose whats most important for
you un your simulations.
"""

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
x_len = 200         # Number of points to display
y_range = [-1,1]    # Range of Possible Y values to display

# Create figure for plotting
fig = plt.figure()
ax  = fig.add_subplot(1,1,1)
xs  = list(range(0,200))
ys  = [0] * x_len
ax.set_ylim(y_range)

# Create a Blank line . We will update the line in animate
line , = ax.plot(xs,ys)

# Add Labels
plt.title("Sine Wave")
plt.xlabel("Samples")
plt.ylabel("Amplitude")

# This function is called periodically from FuncAnimation

fs = 44100
f = int(input("Enter fundamental frequency: "))
t = float(input("Enter duration of signal (in seconds): "))

def animate(i,ys):

    sample = np.linspace(1, t, int(fs*t), endpoint=False)[i]

    rand_val = np.sin(2*np.pi*f*sample)  # Generate Random Values between 0 and 20

    temp_c = round(rand_val ,10)

    print(temp_c)

    # Add y to list
    ys.append(temp_c)

    # Limit y list to set number of items
    ys = ys[-x_len:]

    # Update line with new Y values 
    line.set_ydata(ys)

    return line ,

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate ,
    fargs       = (ys,),
    interval    = 10,
    blit=True
    )
plt.show()