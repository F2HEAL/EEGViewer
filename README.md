# 🧠 EEG Viewer User Manual

## Overview

**EEG Viewer** is a real-time EEG visualization and analysis tool built in Python using BrainFlow, PyQt5, and pyqtgraph. It supports data acquisition from BrainFlow-compatible devices or playback from a CSV file, and provides dynamic filtering, spectral analysis (PSD), and a customizable UI.

---

## ⚙️ Requirements

- Python 3.8–3.12
- Required Python packages:
  - `brainflow`
  - `pyqt5`
  - `pyqtgraph`
  - `scipy`
  - `numpy`

Install them via:

```bash
pip install brainflow pyqt5 pyqtgraph scipy numpy
```

---

## 🚀 How to Run

### From a real device:
```bash
python eeg_viewer_main.py --serial-port COM5 --board-id 17
```

### From a playback file:
```bash
python eeg_viewer_main.py --playback-file path/to/data.csv --board-id 17
```

> 📌 `--board-id` should match the device used to record the data. Use `--board-id 17` for FreeEEG32.

---

## 🖥️ User Interface Components

### 1. **Time-Series Plots**
- Displays live EEG traces from up to 8 EXG channels and one virtual differential channel (C3–C4).
- Each channel is labeled (e.g., C3, FC4, etc.).
- Colored lines help differentiate channels; virtual channel has a dashed blue line.

### 2. **Channel Controls**
- A checkbox panel allows toggling each channel's visibility.
- Located on the right side of the interface.

### 3. **Y-Axis Controls**
- Located above the filter settings.
- Set manual Y-axis limits or enable auto-scaling.
- Click **“Apply Y Range”** to update.

### 4. **PSD Plot (Power Spectral Density)**
- Shows the frequency distribution of EEG signals.
- Logarithmic scale for power.

### 5. **Band Power Bar Chart**
- Visualizes power in standard EEG bands:
  - δ (Delta), θ (Theta), α (Alpha), β (Beta), h-β (High Beta), γ (Gamma), h-γ (High Gamma)

### 6. **Filter Panel**
- Toggle filters via checkboxes:
  - **Detrend**, **Realtime High-Pass (RTHP)**, **Bandpass**, **Notch Filters** (fixed and real-time)
- Customize bandpass frequency range.

---
## 🧪 Signal Quality & Diagnostics – In Detail

Each EEG channel shows two status lines:

### 🟦 Line 1: Signal Statistics

| Metric | Description | Good Range (Typical) | Interpretation |
|--------|-------------|----------------------|----------------|
| **PTP (Peak-to-Peak)** | Max - Min value over the window. Reflects amplitude. | **10–1000 μV** | Too low → flat or disconnected; too high → motion/noise artifacts. |
| **RMS (Root Mean Square)** | Power of the signal. Related to signal intensity. | **10–100 μV** | Too high → muscle noise; too low → weak contact or bad channel. |
| **DC (Offset)** | Mean signal level. Not informative in AC-coupled systems. | ~**0 μV** (± few μV) | High offset might suggest drift or poor connection. |
| **Flat** | % of samples with tiny variation (Δ < 3μV). Measures inactivity. | **< 0.95 (i.e., <95%)** | High flatness = flatlined channel (disconnected/shorted). |
| **Kurtosis** | Measures "spikiness" — extreme outliers. | **< 10** | High kurtosis → spike artifacts (e.g., eye blinks, muscle spikes). |
| **Skewness** | Asymmetry of the waveform. | **-2 to +2** | Very high/low → unusual or non-biological patterns. |

#### ➕ Status Tag Examples

- **OK**: All metrics in acceptable range.
- **FLAT**: Flatness > 0.95 or PTP < 10 → likely disconnected.
- **NOISY**: PTP > 1000 → possibly muscle/EMG/motion artifact.
- **SPIKY**: Kurtosis > 10 → sharp transients, maybe eye/muscle artifacts.
- **HIGH RMS**: RMS > 100 → possibly muscle tension.

### 🟥 Line 2: Frequency & Spectral Quality

| Metric | Description | Good Range (Typical) | Interpretation |
|--------|-------------|----------------------|----------------|
| **LNR (Line Noise Ratio)** | Power at 50 Hz / total power. | **< 0.2** (Europe) | Higher → power line interference (electrical noise). |
| **MR (Muscle Ratio)** | Gamma / (Alpha+Beta). | **< 1.0** | Higher → excessive gamma = EMG artifact. |
| **Entropy** | Spectral entropy (flatness of spectrum). | **2.5 – 4.8** | Low = structured (e.g., EEG); high = noise/random. |

### 🧠 Band Power Levels

These give relative power in each EEG band:

| Band | Range (Hz) | What it indicates |
|------|------------|-------------------|
| **δ (Delta)** | 1–4 Hz | Deep sleep or brain injury. |
| **θ (Theta)** | 4–8 Hz | Drowsiness, meditation. |
| **α (Alpha)** | 8–13 Hz | Relaxed wakefulness, closed eyes. |
| **β (Beta)** | 13–20 Hz | Alertness, problem-solving. |
| **h-β (High Beta)** | 20–30 Hz | Stress, tension. |
| **γ (Gamma)** | 30–60 Hz | High-level cognition, sensory binding. |
| **h-γ (High Gamma)** | 60–100 Hz | Possible EMG artifact or high attention load. |

These are normalized to total power and shown in a bar chart.

### ✅ Summary of Healthy EEG Ranges

| Parameter      | Typical EEG Signal |
|----------------|---------------------|
| PTP            | 50–100 μV           |
| RMS            | 10–50 μV            |
| DC Offset      | ~0 μV               |
| Flatness       | < 0.8               |
| Kurtosis       | ~3–8                |
| Skewness       | -2 to +2            |
| LNR            | < 0.2               |
| MR             | < 1.0               |
| Entropy        | 2.5–4.8             |

### 🧠 Common Artifacts You Might See

| Artifact Type    | Indicators |
|------------------|-----------|
| **Loose electrode** | Flat signal (Flat > 0.95, low PTP/RMS) |
| **Muscle noise (EMG)** | High RMS, high gamma/h-gamma, high MR |
| **Power line noise** | High LNR at 50/60 Hz |
| **Eye blink / movement** | High kurtosis and skewness, transient spikes |
| **Disconnected sensor** | Flat + PTP near 0 μV |

---

---

## 🧩 Custom Features

- **Virtual Channel**: Computes the differential signal between **C3 and C4** (C3–C4).
- **Filter logic**: Combines both real-time and offline filtering.
- **Dynamic UI**: Updates plots every 250 ms with smooth rendering.
- **Color Consistency**: Time-series and PSD plots share consistent color codes.

---

## 🧯 Troubleshooting

| Issue | Solution |
|-------|----------|
| GUI flashes and disappears | Ensure `app.exec_()` is called properly in main loop. |
| Blank window | Avoid overwriting the main widget inside `PlotManager`. |
| Filters don’t apply | Check if the checkbox is ticked and values are valid. |
| Axis range not updating | Click the **Apply** button after entering values. |
| Colors don’t match | Use the same `pen` object for both time and PSD plots. |

---

## 🛠️ Developer Notes

- Main entry point: `eeg_viewer_main.py`
- Core modules:
  - `controller.py`: Initializes GUI and handles board data.
  - `plot_manager.py`: Handles plotting and updates.
  - `filters.py`: Contains real-time and batch filters.
  - `ui.py`: Builds control panels.
- Virtual channel is always appended last and referenced by `virtual_index`.

---

## 📞 Support / Contributing

If you'd like to extend this tool with:

- Event marking
- Signal classification
- Session saving/loading
- Channel montages

Let us know, or fork the repo and start customizing!
