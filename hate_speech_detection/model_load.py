# -*- coding: utf-8 -*-
"""model_load.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VjJ4-HQNsHlfGXQVOR9KljvqTrw-kKfS
"""

#load
from transformers import ElectraForTokenClassification, ElectraTokenizerFast
from google.colab import drive
import torch
drive.mount('/content/drive')


load_path = "/content/drive/MyDrive/yaife/detector3/model_checkpoint"

# 디바이스 설정
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = ElectraForTokenClassification.from_pretrained(load_path)
model.to(device)  # 모델을 GPU로 이동

tokenizer = ElectraTokenizerFast.from_pretrained(load_path)