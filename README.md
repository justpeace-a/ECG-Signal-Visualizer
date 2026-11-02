## **ECG Signal Visualizer Using Python**

**Project Overview**

This project demonstrates the visualization and basic analysis of electrocardiogram (ECG) signals using Python.

It includes both simulated ECG signals and real ECG recordings obtained from the MIT-BIH Arrhythmia Database on PhysioNet.

The project was developed to explore biomedical signal processing, ECG waveform visualization, R-peak detection, and heart rate estimation.

**Features**

1. Generate and visualize simulated ECG signals.
2. Add noise to simulated ECG signals.
3. Apply moving-average filtering to reduce noise.
4. Load real ECG recordings from PhysioNet.
5. Detect R peaks using SciPy.
6. Calculate RR intervals and estimate heart rate.
7. Display ECG waveforms and detected R peaks using Matplotlib.

**Technologies Used**

- **Python** (Programming language)
- **NumPy** (Numerical calculations and signal generation)
- **Matplotlib** (ECG visualization)
- **SciPy** (Signal processing and peak detection)
- **WFDB** (Accessing real ECG recordings from PhysioNet)

**Dataset**

Real ECG recordings are obtained from the MIT-BIH Arrhythmia Database, available through PhysioNet.

The project also includes a CSV file containing simulated ECG measurements.

**How to Run**

1. Install Python on your computer.

2. Install the required libraries:

   pip install numpy matplotlib scipy wfdb

3. To run the simulated ECG program:

   python ecg_visualizer.py

4. To run the real ECG program:

   python real_ecg.py

Note: An internet connection may be required to retrieve real ECG recordings from PhysioNet.

**Learning Outcomes**

Through this project, I gained practical experience in:

- Working with biomedical signals using Python.
- Understanding ECG waveforms and R peaks.
- Applying basic digital signal processing techniques.
- Calculating heart rate from RR intervals.
- Visualizing and analyzing real physiological data.

## Disclaimer

This project is intended for educational purposes and is not designed for clinical diagnosis.
