# Hugging Face Examples

This repository contains a few small experiments using the [Hugging Face](https://huggingface.co/) ecosystem. Each script demonstrates a different API or model from Hugging Face.

## Text examples

- **Emotion.py** – Uses `sentence-transformers/all-MiniLM-L6-v2` to compare sentence similarity.
- **Sentence.py** – Runs sentiment analysis with `distilbert-base-uncased-finetuned-sst-2-english`.
- **Sentence_make.py** – Generates text with the `gpt2` model.
- **chat.py** – Answers questions using `deepset/roberta-base-squad2`.

## Image examples

- **Image_mk.py** – Generates an image with `stable-diffusion-v1-4`.
- **MPS_acc.py** – Classifies images from a small dataset using `microsoft/resnet-18`.
- **GPU_acc.py** and **cuda_ver.py** – Check PyTorch installation and CUDA availability.

Sample datasets are provided in the `datasets` directory.

## Usage

Install the required Python packages and run the scripts as needed:

```bash
pip install torch transformers diffusers datasets requests
python GAN/Image_mk.py
```

Several scripts require a Hugging Face API token. Edit the `API_TOKEN` variable in each script before running.
