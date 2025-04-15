# 🖼️ Image Caption Generator

[![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)  
[![TensorFlow](https://img.shields.io/badge/-TensorFlow-FF6F00?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)  
![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white)  
![NumPy](https://img.shields.io/badge/-NumPy-013243?logo=numpy&logoColor=white)  
![Jupyter](https://img.shields.io/badge/-Jupyter-F37626?logo=jupyter&logoColor=white)  
[![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B)](https://www.streamlit.io/)

---

## 📖 Table of Contents

- [Live Demo](#live-demo)
- [Overview](#overview)
- [Dataset](#dataset)
- [Setup Instructions](#setup-instructions)
- [Deploying with Streamlit](#deploying-with-streamlit)
- [Folder Layout](#folder-layout)
- [Contributing / Issues](#contributing--issues)
- [Planned Improvements](#planned-improvements)

---

## 🚀 Live Demo

Check out the app here:  
👉 [Live App](https://imgcaptiongen.streamlit.app/)

> ⚠️ If the app doesn’t load, it might be paused or facing deployment issues.

If you like the project, feel free to ⭐️ the repo!

![Demo](resource/demo.gif)

---

## 📝 Overview

This project generates image captions using deep learning. It leverages:

- A pretrained **VGG16** model (or **MobileNetV2** for lighter setups)
- A custom **LSTM with attention** for generating descriptions
- The **Flickr8k** dataset as training data

MobileNetV2 is used in the deployed version for faster performance with reduced memory usage.

### Key Features:

- Extracts image features
- Tokenizes and prepares text data
- Generates captions using attention-based LSTM
- Comes with a web interface using Streamlit

---

## 📊 Dataset

We use the [Flickr8k dataset](https://www.kaggle.com/adityajn105/flickr8k), which contains over 8,000 images with five captions each.

**Expected directory structure:**
flickr8k/ ├── Images/ └── captions.txt

---

## ⚙️ Setup Instructions

**Requirements:**
- Python 3.10.12
- All packages in `requirements.txt`

To install and run:

```bash
git clone https://github.com/Sajid030/image-caption-generator.git
cd image-caption-generator
pip install -r requirements.txt
```

---

## 🚀 Deploying on Streamlit Cloud

Want to share your project live? Here's how to deploy it on [Streamlit Cloud](https://streamlit.io/cloud):

1. Fork or clone this repository.
2. Sign in to your Streamlit account and create a new app.
3. Point it to your GitHub repo.
4. Add a `.streamlit/config.toml` file with the following configuration:

```toml
[server]
headless = true
port = $PORT
enableCORS = false

---

## 🚀 Future Improvements

Here are some ideas for enhancing this project:

- **Model Optimization:** Fine-tune the model or integrate transformer-based architectures (e.g., ViT + BERT) for more accurate captioning.
- **Multilingual Support:** Expand the model’s capabilities to generate captions in multiple languages.
- **User Feedback Loop:** Add functionality for users to rate or edit captions, which could be used to further train and improve the model.
- **Image Preprocessing Controls:** Allow users to adjust preprocessing steps (e.g., cropping, resizing) before generating captions.
- **Batch Uploads:** Enable support for multiple image uploads and caption generation at once.
- **Offline Mode:** Package the model in a way that it can run offline via a desktop or mobile app version.
- **Enhanced UI:** Improve the design and interactivity of the Streamlit interface.

Feel free to contribute or suggest more ideas!

---

## 🙌 Acknowledgements

- [Streamlit](https://streamlit.io) for their awesome framework
- The creators of the Flickr8k dataset
- [TensorFlow](https://www.tensorflow.org/) and [Keras](https://keras.io/) for the deep learning tools
- Everyone in the open-source community who shares knowledge and code ❤️

---

Thanks for checking out this project! 🌟
