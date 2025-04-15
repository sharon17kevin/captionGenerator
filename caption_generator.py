import math
import os
import pickle
import re
from collections import defaultdict
from pathlib import Path

import gradio as gr 
import numpy as np
import pandas as pd
from torch import nn
from PIL import Image
import torch
import torchvision
from torchvision import transforms
from torch.nn import CrossEntropyLoss
from torch.optim.lr_scheduler import CosineAnnealingLR
from torch.utils.data import DataLoader, Dataset
from torchvision.models import convnext_small
from torch.utils.tensorboard import SummaryWriter
from torchmetrics.text import ROUGEScore
from torchvision.transforms import Normalize, ToPILImage, ToTensor
from transformers import GPT2Tokenizer


