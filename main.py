from pyscript import document, display
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import MaxNLocator

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
absences = [0, 0, 0, 0, 0]

def addData(event=None):
    output_div = document.getElementById("output")
    output_div.innerHTML = ""

    selected_day = document.getElementById("day").value
    try:
        absence_value = int(document.getElementById("absences").value)
    except ValueError:
        absence_value = 0

    index = days.index(selected_day)
    absences[index] = absence_value

    fig, ax = plt.subplots()
    ax.plot(days, absences, marker='o', linestyle='-')
    ax.set_title("Weekly Attendance (Absences)")
    ax.set_xlabel("Days")
    ax.set_ylabel("Number of Absences")
    ax.set_ylim(bottom=0)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    display(fig, target="output", append=False)