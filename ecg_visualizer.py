import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

time = np.linspace(0, 5, 500)
sampling_interval = time[1] - time[0]
sampling_rate = 1 / sampling_interval

NOISE_LEVEL = 0.3
FILTER_WINDOW = 15
MIN_PEAK_DISTANCE_SECONDS = 1.0

print("Sampling rate:", round(sampling_rate, 2), "Hz")

repeated_ecg = np.zeros_like(time)

r_positions = []

for beat in range(3):
    r_position = 1.0 + beat * 1.5
    r_positions.append(r_position)
    r_wave_new = 1.0 * np.exp(-((time - r_position) ** 2) / (2 * 0.03 ** 2))

    p_position = r_position - 0.5
    p_wave_new = 0.2 * np.exp(-((time - p_position) ** 2) / (2 * 0.1 ** 2))

    q_position = r_position -0.08
    q_wave_new = -0.15 * np.exp(-((time - q_position) ** 2) / (2 * 0.02 ** 2))

    s_position = r_position + 0.08
    s_wave_new = -0.25 * np.exp(-((time - s_position) ** 2) / (2 * 0.02 ** 2))

    t_position = r_position + 0.35
    t_wave_new = 0.35 * np.exp(-((time - t_position) ** 2) / (2 * 0.15 ** 2))
    
    repeated_ecg += p_wave_new + q_wave_new + r_wave_new + s_wave_new + t_wave_new

# Calculate RR intervals
rr_intervals = np.diff(r_positions) 
print("RR intervals:", rr_intervals)

# Calculate average RR interval
average_rr = np.mean(rr_intervals) 
print("Average RR interval:", average_rr)

# Calculate heart rate in beats per minute
heart_rate = 60 / average_rr 
print("Expected Heart rate:", heart_rate, "bpm")

# finding R peaks
peaks, properties = find_peaks(repeated_ecg, height=0.7)
detected_r_times = time[peaks]
detected_rr = np.diff(detected_r_times)
average_detected_rr = np.mean(detected_rr)
detected_heart_rate = 60 / average_detected_rr


# noise interference
np.random.seed(42)
noise = np.random.normal(0, 0.3, len(time))
# print("First 10 noise values:", noise[:10])

noisy_ecg = repeated_ecg + noise

# filtered signal
window_size = 15
kernel = np.ones(window_size) / window_size
filtered_ecg = np.convolve(noisy_ecg, kernel, mode="same")

# Save ECG data to a CSV file
ecg_data = np.column_stack((
    time,
    repeated_ecg,
    noisy_ecg,
    filtered_ecg
))

np.savetxt(
    "ecg_data.csv", 
    ecg_data, 
    delimiter=",", 
    header="Time,Clean ECG,Noisy ECG,Filtered ECG", 
    comments="", 
    fmt="%.6f"
)

print("ECG data saved to successfully")

# Load ECG data from the CSV file
loaded_ecg_data = np.loadtxt(
    "ecg_data.csv",
    delimiter=",",
    skiprows=1
)

print("Loaded ECG data shape:", loaded_ecg_data.shape)

# Extract time and clean ECG from the loaded CSV data
loaded_time = loaded_ecg_data[:, 0]
loaded_clean_ecg = loaded_ecg_data[:, 1]


# Detect R peaks in the filtered signal
filtered_peaks, filtered_properties = find_peaks(
    filtered_ecg, 
    height=0.3,
    distance=int(1.0 * sampling_rate))

# Count how many R peaks were detected
print("Number of filtered R-peaks:", len(filtered_peaks))
print("Filtered R-peak times:", np.round(time[filtered_peaks], 2))

# display the detected R-peak times
if len(filtered_peaks) >= 2:
    filtered_r_times = time[filtered_peaks]
    filtered_rr = np.diff(filtered_r_times)
    filtered_heart_rate = 60 / np.mean(filtered_rr)

    print("Filtered ECG heart rate:", round(filtered_heart_rate, 2), "bpm")

else:
    print("Not enough R-peaks detected in the filtered signal to calculate heart rate.")

print("Detected R-wave times:", np.round(time[peaks], 2))
print("Detected RR intervals:", np.round(detected_rr, 2))
print("Detected heart rate:", np.round(detected_heart_rate, 2), "bpm")

#Original clean ECG signal
plt.plot(time, repeated_ecg, label="Clean ECG signal", color="#39F5FB") 

#ECG signal with random noise
plt.plot(time, noisy_ecg, color="#536f05", alpha=0.4, label="Noisy ECG Signal")

# ECG signal after moving-average filtering
plt.plot(time, filtered_ecg, color="#ab4075", alpha=0.5, label="Filtered ECG Signal")

# R wave peaks
plt.scatter(
    time[peaks], 
    repeated_ecg[peaks], 
    color="red", 
    s=50, 
    edgecolors="black", 
    label="R-peaks(Clean ECG)"
    )

plt.scatter(
    time[filtered_peaks], 
    filtered_ecg[filtered_peaks], 
    color="blue", 
    s=50, 
    edgecolors="black", 
    label="R-peaks(Filtered ECG)"
    )

plt.title(
    "ECG Signal Visualization", 
    fontsize=20,
    family="Arial",
    fontweight="bold",
    color="#030b51"
    )

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.text(0.48, 0.22, "P", color="Red", fontweight="bold")
plt.text(0.85, -0.18, "Q", color="Red", fontweight="bold")
plt.text(1.0, 1.05, "R", color="Red", fontweight="bold")
plt.text(1.09, -0.18, "S", color="Red", fontweight="bold")
plt.legend()
plt.show()