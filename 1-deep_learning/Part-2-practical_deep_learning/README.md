# Part 2: Practical deep learning and deep learning engineering


## Introduction

This part of the module takes you on a guided tour through some of the landscape of practical deep learning. See the accompanying lecture slides for an overview of the content.

We'll meet the idea that non-image data can be turned into images that can be fed to computer vision-based models, use the fact that deep neural networks are representation learners to extract _task-specific representations_ of data, indicate the importance and usefulness of _fusing_ multiple sources of data when constructing predictive models, try out some basic techniques from _explainable AI_, stress the importance of _domain knowledge_ for data augmentation, and more.

We'll end by discussing an often underappreciated but crucial aspect of deep learning and machine learning more generally: the many parts necessary to actually _deploy_ a machine learning-powered system and thus give it actual impact beyond a proof-of-concept research stage. In other words, what's sometimes called _machine learning engineering_.

## Slides and recordings

Intro-slides from 13.05.22: [DLN-AI-2022 - Module 1 - Deep learning, Part 2, 130522](https://docs.google.com/presentation/d/e/2PACX-1vTCIrUX_yA9xzw6slbfU288-bXMwe5dVsX8ejaeIve8kBM97UMVoFp_R2iRSVYl5pZR-UZ_m0jVqIEC/pub?start=false&loop=false&delayms=3000)

Medical AI engineering slides from 13.05.22: [HVL-DLN-AI-2022-Deep_Learning-Part2-MLEngineering.pdf](../../slides/HVL-DLN-AI-2022-Deep_Learning-Part2-MLEngineering.pdf)

Recording of the lecture, 13.05.22: [HVL-MMIV-DLN-AI-2022, Deep Learning, Part 2.2, 130522](https://youtu.be/cwjs4szpy3M) 

## Notebooks

| Notebook    |      1-Click Notebook      |
|:----------|------|
|  [2.1.0-representations-get_molecular_fingerprints_and_images.ipynb](https://nbviewer.org/github/MMIV-ML/HVL-MMIV-DLN-AI-2022/blob/master/1-deep_learning/Part-2-practical_deep_learning/nbs/2.1.0-representations-get_molecular_fingerprints_and_images.ipynb)  | [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MMIV-ML/HVL-MMIV-DLN-AI-2022/blob/master/1-deep_learning/Part-2-practical_deep_learning/nbs/2.1.0-representations-get_molecular_fingerprints_and_images.ipynb)
|  [2.1.1-representations-representing_data_as_images.ipynb](https://nbviewer.org/github/MMIV-ML/HVL-MMIV-DLN-AI-2022/blob/master/1-deep_learning/Part-2-practical_deep_learning/nbs/2.1.1-representations-representing_data_as_images.ipynb)  | [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MMIV-ML/HVL-MMIV-DLN-AI-2022/blob/master/1-deep_learning/Part-2-practical_deep_learning/nbs/2.1.1-representations-representing_data_as_images.ipynb)
|  [2.1.2-representations-CNNs-as-feature_extractors.ipynb](https://nbviewer.org/github/MMIV-ML/HVL-MMIV-DLN-AI-2022/blob/master/1-deep_learning/Part-2-practical_deep_learning/nbs/2.1.2-representations-CNNs-as-feature_extractors.ipynb)  | [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MMIV-ML/HVL-MMIV-DLN-AI-2022/blob/master/1-deep_learning/Part-2-practical_deep_learning/nbs/2.1.2-representations-CNNs-as-feature_extractors.ipynb)
|  [2.2.0-asl-image_classification-tumor_grading.ipynb](https://nbviewer.org/github/MMIV-ML/HVL-MMIV-DLN-AI-2022/blob/master/1-deep_learning/Part-2-practical_deep_learning/nbs/2.2.0-asl-image_classification-tumor_grading.ipynb)  | [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MMIV-ML/HVL-MMIV-DLN-AI-2022/blob/master/1-deep_learning/Part-2-practical_deep_learning/nbs/2.2.0-asl-image_classification-tumor_grading.ipynb)
|  [2.2.1-asl-segmentation-cell_segmentation.ipynb](https://nbviewer.org/github/MMIV-ML/HVL-MMIV-DLN-AI-2022/blob/master/1-deep_learning/Part-2-practical_deep_learning/nbs/2.2.1-asl-segmentation-cell_segmentation.ipynb)  | [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MMIV-ML/HVL-MMIV-DLN-AI-2022/blob/master/1-deep_learning/Part-2-practical_deep_learning/nbs/2.2.1-asl-segmentation-cell_segmentation.ipynb)
|  [2.2.2-asl-segmentation-brain_tumor_segmentation.ipynb](https://nbviewer.org/github/MMIV-ML/HVL-MMIV-DLN-AI-2022/blob/master/1-deep_learning/Part-2-practical_deep_learning/nbs/2.2.2-asl-segmentation-brain_tumor_segmentation.ipynb)  | [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MMIV-ML/HVL-MMIV-DLN-AI-2022/blob/master/1-deep_learning/Part-2-practical_deep_learning/nbs/2.2.2-asl-segmentation-brain_tumor_segmentation.ipynb)

## Install Python environments

### RDKit
To run notebook 2.1.0 on your own computer, install our RDKit environment using Anaconda:

```bash
conda env update -f environment-rdkit.yml
conda activate rdkit
python -m ipykernel install --user --name rdkit --display-name "RDKit"
conda deactivate
```

### fastai
To run notebooks 2.1.1--2.2.1, install our fastai environment: 

```bash
conda env update -f environment-fastai.yml
conda activate fastai
python -m ipykernel install --user --name fastai --display-name "fastai"
conda deactivate
```

### MONAI and torch.io
To run notebook 2.2.2--2.2.3, install our MONAI and TorchIO environment:
```bash
conda env update -f environment-monai.yml
conda activate monai
python -m ipykernel install --user --name monai --display-name "MONAI"
conda deactivate
```
