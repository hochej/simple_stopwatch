import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# number of points for the outer circle, not relevant
n = 100
# radius of the clock
radius = 6
# number of time steps and frames
nsteps = 300
# linewidth of the outer circle
linewidth = 25
# start time, the units are specified below
start_time = 0
# end time (inclusive)
end_time = 1
# suffix that is displayed after the time
unit = "ps"
# number of decimal places that are displayed
decimals = 2
# font size of the text
fontsize = 50
# directory to save the images
directory = "IMAGES/"
# color palette that is used for the outer ring as a progress bar
color_palette = "Spectral"
# figure size in inch
figsize = (5, 5)
dpi = 150

r = np.zeros([n]) + radius
circle = np.linspace(0, 2 * np.pi, n)
colors = sns.color_palette(color_palette, nsteps)
progress_bar = np.linspace(np.pi/2, np.pi/2 - 2*np.pi, nsteps)
times = np.linspace(start_time, end_time, nsteps)
times = np.round(times, decimals=decimals)
times = np.array(times, dtype=str)
for i in range(len(times)):
    if len(times[i].split(".")[-1]) < decimals:
        times[i] += "0"
    times[i] += " " + unit
r2 = np.zeros([nsteps]) + radius


for i in range(nsteps):
    fig = plt.figure(figsize=figsize)
    ax = plt.subplot(1, 1, 1, projection='polar')
    ax.plot(circle, r, c="lightgrey", lw=linewidth)
    ax.plot(progress_bar[:i], r2[:i], color=colors[i], lw=linewidth)
    ax.text(0, 0, times[i], ha="center", va="center", fontsize=fontsize)
    plt.axis('off')
    plt.savefig(f"{directory}{str(i).zfill(4)}.jpg", dpi=dpi)
    plt.close()
