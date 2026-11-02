import wfdb
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

# Load a real ECG recording from PhysioNet (record 103 from the MIT-BIH Arrhythmia Database)

record = wfdb.rdrecord(
    "100", #record number 100
    pn_dir="mitdb", # retrieve the recording from PhysioNet
    sampto=1800 # first 1800 samples of the record
)

print("Sampling rate:", record.fs, "Hz")
print("Signal shape:", record.p_signal.shape)
print("ECG channels:", record.sig_name)

# Select all samples from the first ECG channel (MLII)
real_ecg = record.p_signal[:, 0]
# Convert sample positions into time in seconds
real_time = np.arange(len(real_ecg)) / record.fs

# Detect ECG peaks that are at least 0.4 secs apart
peaks, properties = find_peaks(real_ecg, distance=int(0.4 * record.fs), prominence=0.5, height=0.6) #distance must be at least 0.4 seconds apart, prominence=0.5(peaks must stand out from their surroundings), and height(peaks must reach atleast 0.6 mV)
peak_times = real_time[peaks] #Get R peak times in seconds

#Calculate RR intervals
rr_intervals = np.diff(peak_times)

# Calculate heart rate
heart_rate = 60 / np.mean(rr_intervals)
print("Heart rate:", round(heart_rate, 2), "bpm")

# show average RR interval
print("Average RR interval:", round(np.mean(rr_intervals), 3), "seconds")

plt.plot(real_time, real_ecg)
plt.plot(real_time[peaks], real_ecg[peaks], "x", color="red", markersize=10, label="Detected R Peaks")

plt.xlabel("Time (seconds)", fontsize=14, family="Arial", fontweight="bold", color="#030b51")
plt.ylabel("ECG Amplitude (mV)", fontsize=14, family="Arial", fontweight="bold", color="#030b51")
plt.title("Real ECG Signal (MIT-BIH Record 100)", 
          fontsize=20,
          family="Arial",
          fontweight="bold",
          color="#030b51")

plt.grid(True)
plt.text(0.98, 0.94, f"Heart Rate: {heart_rate:.1f} bpm", transform=plt.gca().transAxes, fontsize=10, family="Arial", fontweight="bold", color="#030b51", ha="right")
plt.legend()

# Save ECG graph
plt.savefig("real_ecg_graph.png", dpi=300, bbox_inches="tight")

plt.show()