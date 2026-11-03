<h1 align="center">Optional Papers</h1>

<p align="center">Papers to read after the <a href="README.md#paper-list">main list</a>.</p>

These papers are worth knowing but come second: they extend a main paper, are harder to recode at small scale, or matter mostly for history. Years are the first public release, as in the main list.

## Contents

- [Foundations](#foundations)
- [Convolutional networks](#convolutional-networks)
- [Transformers and attention](#transformers-and-attention)
- [Large language models](#large-language-models)
- [GANs](#gans)
- [VAEs, flows and autoregressive models](#vaes-flows-and-autoregressive-models)
- [Diffusion and flow matching](#diffusion-and-flow-matching)
- [Graph neural networks](#graph-neural-networks)
- [Self-supervised learning](#self-supervised-learning)

## Foundations

| Model | Paper | Year | What it adds |
|---|---|---|---|
| Kaiming init / PReLU | [Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification](https://arxiv.org/abs/1502.01852) | 2015 | Weight initialization that keeps the variance stable in ReLU networks, and the learnable PReLU activation |

## Convolutional networks

| Model | Paper | Year | What it adds |
|---|---|---|---|
| Faster R-CNN | [Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks](https://arxiv.org/abs/1506.01497) | 2015 | Two-stage detector where a region proposal network shares features with the detection head; introduced anchor boxes |
| MobileNet | [MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/abs/1704.04861) | 2017 | Depthwise separable convolutions with width and resolution multipliers for small, fast models |

## Transformers and attention

| Model | Paper | Year | What it adds |
|---|---|---|---|
| DETR | [End-to-End Object Detection with Transformers](https://arxiv.org/abs/2005.12872) | 2020 | Detection as set prediction with a Transformer, learned object queries and Hungarian matching, without anchors or NMS |

## Large language models

| Model | Paper | Year | What it adds |
|---|---|---|---|
| T5 | [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683) | 2019 | Every NLP task framed as text-to-text, span-corruption pretraining on C4, and a large study of pretraining choices |
| DPO | [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) | 2023 | Trains on preference pairs with a simple classification-style loss, without a reward model or PPO |

## GANs

| Model | Paper | Year | What it adds |
|---|---|---|---|
| ProGAN | [Progressive Growing of GANs for Improved Quality, Stability, and Variation](https://arxiv.org/abs/1710.10196) | 2017 | Grows the generator and discriminator from 4x4 to 1024x1024 during training; minibatch stddev and equalized learning rate |
| SNGAN | [Spectral Normalization for Generative Adversarial Networks](https://arxiv.org/abs/1802.05957) | 2018 | Bounds the discriminator's Lipschitz constant by dividing each weight by its largest singular value |

## VAEs, flows and autoregressive models

| Model | Paper | Year | What it adds |
|---|---|---|---|
| NICE | [NICE: Non-linear Independent Components Estimation](https://arxiv.org/abs/1410.8516) | 2014 | First deep normalizing flow: additive coupling layers with exact log-likelihood |
| Gated PixelCNN | [Conditional Image Generation with PixelCNN Decoders](https://arxiv.org/abs/1606.05328) | 2016 | Vertical and horizontal stacks that remove the PixelCNN blind spot, plus class conditioning |
| Glow | [Glow: Generative Flow with Invertible 1x1 Convolutions](https://arxiv.org/abs/1807.03039) | 2018 | ActNorm and invertible 1x1 convolutions on top of RealNVP-style flows |
| VAR | [Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction](https://arxiv.org/abs/2404.02905) | 2024 | Autoregressive image generation as coarse-to-fine next-scale prediction over a multi-scale VQ tokenizer |

## Diffusion and flow matching

| Model | Paper | Year | What it adds |
|---|---|---|---|
| Diffusion probabilistic models | [Deep Unsupervised Learning using Nonequilibrium Thermodynamics](https://arxiv.org/abs/1503.03585) | 2015 | The original diffusion model: a fixed forward process destroys structure and a learned reverse chain restores it |
| Rectified Flow | [Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow](https://arxiv.org/abs/2209.03003) | 2022 | An ODE learned along straight paths between noise and data, with "reflow" steps for few-step generation |

## Graph neural networks

| Model | Paper | Year | What it adds |
|---|---|---|---|
| GNN | [The Graph Neural Network Model](https://doi.org/10.1109/TNN.2008.2005605) | 2008 | The original GNN: node states updated by a shared function until they reach a fixed point |
| DeepWalk | [DeepWalk: Online Learning of Social Representations](https://arxiv.org/abs/1403.6652) | 2014 | Node embeddings from random walks treated as sentences and trained with skip-gram |
| ChebNet | [Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering](https://arxiv.org/abs/1606.09375) | 2016 | Spectral graph convolution with Chebyshev polynomial filters; GCN is its first-order simplification |

## Self-supervised learning

| Model | Paper | Year | What it adds |
|---|---|---|---|
| CPC | [Representation Learning with Contrastive Predictive Coding](https://arxiv.org/abs/1807.03748) | 2018 | Predicts future latent states and introduces the InfoNCE contrastive loss |
