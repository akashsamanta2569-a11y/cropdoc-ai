# 🌱 CropDoc AI — Autonomous Crop Health & Action Engine

**SENSE → UNDERSTAND → DECIDE → ACT**

CropDoc AI is an Edge AI smart-farming prototype developed for the **Arduino Edge AI Hackathon 2026**. It focuses on potato leaf disease classification and demonstrates how a local AI prediction can trigger a physical hardware response.

## 🎯 Problem

Crop diseases can damage harvests when they are not identified early. Many image classifiers stop at predicting a disease. CropDoc AI explores a complete pipeline that interprets leaf images, checks prediction confidence and stability, and communicates a decision to embedded hardware.

## 💡 Solution

CropDoc AI classifies potato leaf images into three categories:

- 🟢 Healthy
- 🟡 Early Blight
- 🔴 Late Blight
- 🔵 Unknown / Scanning when the system cannot accept a reliable diagnosis

The prototype combines computer vision, an Edge Impulse model, a decision engine, and Arduino UNO Q hardware control.

## 🏗️ Architecture

```text
Potato Leaf → Camera → OpenCV → Edge AI Model
                                  ↓
                     Confidence + Stability Checks
                                  ↓
                            Decision Engine
                                  ↓
                        Arduino Bridge / RPC
                                  ↓
                          STM32U585 MCU
                                  ↓
                              RGB LED
```

## 🧠 Model and Dataset

The model was trained using potato-leaf images from the PlantVillage dataset.

| Item | Details |
|---|---|
| Crop | Potato |
| Classes | Healthy, Early Blight, Late Blight |
| Training images | 1,722 |
| Separate test images | 430 |
| Total images | 2,152 |
| Model | MobileNetV2 transfer learning |
| Quantization | INT8 |
| Reported test accuracy | 97.44% |

**Evaluation note:** The reported 97.44% accuracy is from the separate 430-image test set. It is not a guarantee of the same accuracy in real farms; field validation is still required.

## 🛠️ Technology Stack

- Python
- OpenCV
- MobileNetV2
- Edge Impulse
- Arduino App Lab
- Arduino UNO Q
- Qualcomm Dragonwing QRB2210 Linux MPU
- STM32U585 MCU
- Arduino Bridge / RPC
- C++ for the embedded sketch

## ✨ Key Features

- Local AI inference after model deployment
- Three-class potato leaf classification
- Confidence and prediction-stability checks
- Unknown/scanning state
- Linux-to-microcontroller communication
- RGB LED feedback

## 📁 Repository Structure

```text
cropdoc-ai/
├── src/
│   ├── camera.py
│   ├── camera_test.py
│   ├── capture_test.py
│   ├── live_preprocess_test.py
│   ├── prepare_ei_dataset.py
│   └── preprocessing.py
├── tests/
│   └── test_preprocessing.py
├── make_potato_print_sheet.py
├── .gitignore
└── README.md
```

This initial repository contains the Windows-side source code and tests. The final Arduino App Lab application files and trained model binary are not included in this version.

## 🚀 Getting Started

Install Python 3 and create a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the packages used by the current Python utilities:

```powershell
python -m pip install opencv-python numpy pillow matplotlib
```

Run the preprocessing test:

```powershell
python -m tests.test_preprocessing
```

Camera utilities require an available camera source. Running the complete hardware demonstration requires the configured Arduino UNO Q application and compatible camera setup.

## 🌐 Offline Operation

The deployed model and decision logic are designed for local inference without a cloud inference API. During development, a laptop camera stream was used over a local network. A fully self-contained offline setup requires validating a compatible UVC USB webcam directly on the board with internet access disabled.

## ⚠️ Limitations

- The current model focuses on three potato-leaf categories.
- Dataset performance may differ from real-world field performance.
- Lighting, backgrounds, and camera quality can affect predictions.
- The RGB LED demonstrates a hardware response; it does not treat the crop.
- Field testing and agricultural expert validation are needed before practical farming use.

## 🔭 Future Scope

- Validate direct USB camera operation on the board.
- Test with real field images and varied lighting.
- Improve leaf-presence detection and confidence calibration.
- Expand to additional crops and disease classes.
- Explore safe, validated agricultural actuators.

## 👥 Team

**CropDoc AI — Arduino Edge AI Hackathon 2026**

- **Team Leader:** [Ananya Dutta](https://github.com/ananyadutta-tech)
- **Team Member:** [Akash Samanta](https://github.com/akashsamanta2569-a11y)
- **Team Member:** [Supriyo Adhikary](https://github.com/SupriyoAdhikary-2024)
- **Team Member:** [Rishika Gupta](https://github.com/RishikaGupta0803)


## 🙏 Acknowledgements

Thanks to the Arduino Edge AI Hackathon organizers, Brainware University, our mentors and judges, Edge Impulse, and the PlantVillage dataset contributors.

## 📄 License

No license has been selected yet. Review the code, model, dataset, and dependency terms before choosing a project license.
