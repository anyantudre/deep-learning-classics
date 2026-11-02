<h1 align="center">Deep Learning Classics</h1>

<p align="center">Read, review and recode the papers that shaped deep learning.</p>

This repository collects landmark deep learning papers. Each one gets a short summary and a from-scratch PyTorch implementation, written for learning rather than performance. The `courses/` folder holds notes and notebooks from the deep learning courses I followed.

## Contents

- [Repository layout](#repository-layout)
- [Paper list](#paper-list)
  - [Foundations](#foundations)
  - [Convolutional networks](#convolutional-networks)
  - [Sequence models](#sequence-models)
  - [Transformers and attention](#transformers-and-attention)
  - [Large language models](#large-language-models)
  - [GANs](#gans)
  - [VAEs, flows and autoregressive models](#vaes-flows-and-autoregressive-models)
  - [Diffusion and flow matching](#diffusion-and-flow-matching)
  - [Graph neural networks](#graph-neural-networks)
  - [Self-supervised learning](#self-supervised-learning)
- [Courses](#courses)
- [Resources](#resources)
- [License](#license)

## Repository layout

| Folder | Contents |
|---|---|
| [`ConvNets/`](ConvNets) | [ResNet](ConvNets/ResNets) summary and code, [YOLO](ConvNets/YOLO) summary |
| [`GANs/`](GANs) | [DCGAN](GANs/DCGAN) trained on MNIST to generate handwritten digits |
| [`GNNs/`](GNNs) | Reading list on graph neural networks: books, articles, courses and videos |
| [`courses/`](courses) | FIDLE, Machine Learnia, from-scratch notebooks and the OxML 2025 summer school |

A category folder is created when work on its first paper starts. Each paper lives in `<Category>/<Model>/` and contains:

- `README.md`: summary and notes on the paper
- the paper PDF, when it is publicly available
- `implementation.py`: the from-scratch implementation
- `notebook.ipynb`: a small demo, when useful

## Paper list

Years are the first public release (usually arXiv), not the conference year. Status is **Done**, **In progress**, or empty when not started.

### Foundations

Folder: `Foundations/`

| Model | Paper | Year | Status |
|---|---|---|---|
| Backpropagation | [Learning representations by back-propagating errors](https://doi.org/10.1038/323533a0) | 1986 | |
| Dropout | [Dropout: A Simple Way to Prevent Neural Networks from Overfitting](https://jmlr.org/papers/v15/srivastava14a.html) | 2014 | |
| Adam | [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980) | 2014 | |
| Batch Normalization | [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167) | 2015 | |
| Layer Normalization | [Layer Normalization](https://arxiv.org/abs/1607.06450) | 2016 | |

### Convolutional networks

Folder: [`ConvNets/`](ConvNets)

| Model | Paper | Year | Status |
|---|---|---|---|
| LeNet-5 | [Gradient-Based Learning Applied to Document Recognition](https://doi.org/10.1109/5.726791) | 1998 | |
| AlexNet | [ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) | 2012 | |
| VGG | [Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/abs/1409.1556) | 2014 | |
| GoogLeNet (Inception v1) | [Going Deeper with Convolutions](https://arxiv.org/abs/1409.4842) | 2014 | |
| [ResNet](ConvNets/ResNets) | [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) | 2015 | In progress |
| U-Net | [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/abs/1505.04597) | 2015 | |
| [YOLO v1](ConvNets/YOLO) | [You Only Look Once: Unified, Real-Time Object Detection](https://arxiv.org/abs/1506.02640) | 2015 | In progress |
| DenseNet | [Densely Connected Convolutional Networks](https://arxiv.org/abs/1608.06993) | 2016 | |
| ConvNeXt | [A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545) | 2022 | |

### Sequence models

Folder: `SequenceModels/`

| Model | Paper | Year | Status |
|---|---|---|---|
| Elman RNN | [Finding Structure in Time](https://doi.org/10.1207/s15516709cog1402_1) | 1990 | |
| LSTM | [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735) | 1997 | |
| word2vec | [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781) | 2013 | |
| GRU | [Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation](https://arxiv.org/abs/1406.1078) | 2014 | |
| Seq2Seq | [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215) | 2014 | |
| Bahdanau attention | [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) | 2014 | |
| Mamba | [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) | 2023 | |

### Transformers and attention

Folder: `Transformers/`

| Model | Paper | Year | Status |
|---|---|---|---|
| Transformer | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | 2017 | |
| GPT | [Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | 2018 | |
| BERT | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805) | 2018 | |
| ViT | [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929) | 2020 | |
| Swin Transformer | [Swin Transformer: Hierarchical Vision Transformer using Shifted Windows](https://arxiv.org/abs/2103.14030) | 2021 | |

### Large language models

Folder: `LLMs/`

| Model | Paper | Year | Status |
|---|---|---|---|
| GPT-2 | [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) | 2019 | |
| Scaling laws | [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) | 2020 | |
| GPT-3 | [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) | 2020 | |
| LoRA | [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) | 2021 | |
| Chinchilla | [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) | 2022 | |
| InstructGPT | [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) | 2022 | |
| LLaMA | [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971) | 2023 | |

### GANs

Folder: [`GANs/`](GANs)

| Model | Paper | Year | Status |
|---|---|---|---|
| GAN | [Generative Adversarial Networks](https://arxiv.org/abs/1406.2661) | 2014 | |
| Conditional GAN | [Conditional Generative Adversarial Nets](https://arxiv.org/abs/1411.1784) | 2014 | |
| [DCGAN](GANs/DCGAN) | [Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks](https://arxiv.org/abs/1511.06434) | 2015 | Done |
| Pix2Pix | [Image-to-Image Translation with Conditional Adversarial Networks](https://arxiv.org/abs/1611.07004) | 2016 | |
| WGAN | [Wasserstein GAN](https://arxiv.org/abs/1701.07875) | 2017 | |
| WGAN-GP | [Improved Training of Wasserstein GANs](https://arxiv.org/abs/1704.00028) | 2017 | |
| CycleGAN | [Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks](https://arxiv.org/abs/1703.10593) | 2017 | |
| StyleGAN | [A Style-Based Generator Architecture for Generative Adversarial Networks](https://arxiv.org/abs/1812.04948) | 2018 | |

### VAEs, flows and autoregressive models

Folder: `LikelihoodModels/`

| Model | Paper | Year | Status |
|---|---|---|---|
| VAE | [Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114) | 2013 | |
| PixelRNN / PixelCNN | [Pixel Recurrent Neural Networks](https://arxiv.org/abs/1601.06759) | 2016 | |
| RealNVP | [Density estimation using Real NVP](https://arxiv.org/abs/1605.08803) | 2016 | |
| VQ-VAE | [Neural Discrete Representation Learning](https://arxiv.org/abs/1711.00937) | 2017 | |
| VQGAN | [Taming Transformers for High-Resolution Image Synthesis](https://arxiv.org/abs/2012.09841) | 2020 | |

### Diffusion and flow matching

Folder: `Diffusion/`

| Model | Paper | Year | Status |
|---|---|---|---|
| NCSN | [Generative Modeling by Estimating Gradients of the Data Distribution](https://arxiv.org/abs/1907.05600) | 2019 | |
| DDPM | [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) | 2020 | |
| DDIM | [Denoising Diffusion Implicit Models](https://arxiv.org/abs/2010.02502) | 2020 | |
| Score SDE | [Score-Based Generative Modeling through Stochastic Differential Equations](https://arxiv.org/abs/2011.13456) | 2020 | |
| Latent Diffusion | [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752) | 2021 | |
| Classifier-free guidance | [Classifier-Free Diffusion Guidance](https://arxiv.org/abs/2207.12598) | 2022 | |
| Flow Matching | [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747) | 2022 | |
| DiT | [Scalable Diffusion Models with Transformers](https://arxiv.org/abs/2212.09748) | 2022 | |

### Graph neural networks

Folder: [`GNNs/`](GNNs), which also has a [reading list](GNNs/README.md).

| Model | Paper | Year | Status |
|---|---|---|---|
| GCN | [Semi-Supervised Classification with Graph Convolutional Networks](https://arxiv.org/abs/1609.02907) | 2016 | |
| MPNN | [Neural Message Passing for Quantum Chemistry](https://arxiv.org/abs/1704.01212) | 2017 | |
| GraphSAGE | [Inductive Representation Learning on Large Graphs](https://arxiv.org/abs/1706.02216) | 2017 | |
| GAT | [Graph Attention Networks](https://arxiv.org/abs/1710.10903) | 2017 | |
| GIN | [How Powerful are Graph Neural Networks?](https://arxiv.org/abs/1810.00826) | 2018 | |
| Graphormer | [Do Transformers Really Perform Bad for Graph Representation?](https://arxiv.org/abs/2106.05234) | 2021 | |

### Self-supervised learning

Folder: `SelfSupervised/`

| Model | Paper | Year | Status |
|---|---|---|---|
| MoCo | [Momentum Contrast for Unsupervised Visual Representation Learning](https://arxiv.org/abs/1911.05722) | 2019 | |
| SimCLR | [A Simple Framework for Contrastive Learning of Visual Representations](https://arxiv.org/abs/2002.05709) | 2020 | |
| BYOL | [Bootstrap your own latent: A new approach to self-supervised Learning](https://arxiv.org/abs/2006.07733) | 2020 | |
| CLIP | [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) | 2021 | |
| DINO | [Emerging Properties in Self-Supervised Vision Transformers](https://arxiv.org/abs/2104.14294) | 2021 | |
| MAE | [Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377) | 2021 | |

## Courses

| Folder | Source | Contents |
|---|---|---|
| [`FIDLE/`](courses/FIDLE) | FIDLE deep learning course (French) | Notes on chapter 1, "Mathematics & Gradients everywhere", with slide captures, and Kaggle notebooks on gradients and an MNIST CNN in Keras |
| [`Machine-Learnia/`](courses/Machine-Learnia) | Machine Learnia deep learning series on YouTube (French) | Code from the videos: a first artificial neuron, a cat vs dog classifier, two-layer and deep networks, MNIST with TensorFlow |
| [`From-Scratch/`](courses/From-Scratch) | Own notebooks | Perceptrons, a neural network from scratch, Fashion-MNIST classification with Keras |
| [`OxML-MLxFundamentals/`](courses/OxML-MLxFundamentals) | Oxford Machine Learning Summer School 2025, MLx Fundamentals | Lecture slides and notes for each of the four days, plus the LLM and supervised fine-tuning practicals |

## Resources

Books
- [Understanding Deep Learning](https://udlbook.github.io/udlbook/) by Simon J. D. Prince, with notebooks and figures
- [Deep Learning with Python](https://deeplearningwithpython.io/) by François Chollet and Matthew Watson
- [Dive into Deep Learning](https://d2l.ai/)
- [Deep Learning](https://www.deeplearningbook.org/) by Ian Goodfellow, Yoshua Bengio and Aaron Courville

Courses and tutorials
- [CS231n: Deep Learning for Computer Vision](https://cs231n.github.io/) (Stanford course notes)
- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) by Andrej Karpathy
- [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) (Harvard NLP)

Practice
- [Deep-ML](https://www.deep-ml.com/)

Hackathon platforms
- [Codabench](https://www.codabench.org/)
- [TensorTonic](https://www.tensortonic.com/)

## License

MIT, see [LICENSE](LICENSE). The paper PDFs and the OxML lecture slides belong to their authors.
