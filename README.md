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

## 🧪 Signal Quality & Diagnostics

Each channel displays two label rows:

- **Row 1 (Signal Stats)**:
  - Peak-to-Peak (PTP), RMS, DC offset, flatness, kurtosis, skewness, and a status label.
  - Statuses include: `OK`, `NOISY`, `FLAT`, `SPIKY`, `HIGH RMS`.

- **Row 2 (Spectral Features)**:
  - Line Noise Ratio (LNR), Muscle Ratio (MR), Spectral Entropy, Band Power values.
  - Status includes `HUMAN EEG ALIKE`, `RANDOM NOISE ALIKE`.

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
