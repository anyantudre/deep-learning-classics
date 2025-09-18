# OxML Day 1, Intro to ML, Biwei Huang

## Introduction to Core Concepts
Machine learning enables systems to learn patterns from data. This guide covers key topics:
- **Supervised Learning**: Linear regression/classification, empirical risk minimization
- **Neural Networks**: MLPs, CNNs, autoencoders
- **Advanced Concepts**: Feature maps, radial basis functions (RBFs)

---

## 1. Supervised Learning with Linear Models

### 1.1 Problem Setup
**Example**: Predict movie ratings using friends' ratings (5 friends → 5D feature vector).

**Key Components**:
- Input `x ∈ ℝᵈ` (features)
- Output `y` (numeric for regression, class labels for classification)
- Hypothesis function `h(x)` to predict `y`

### 1.2 Empirical Risk Minimization (ERM)
3-step pipeline:
1. **Choose Hypothesis Class**  
   *Linear models*: `h(x) = w₀ + w₁x₁ + ... + wₖxₖ`
2. **Select Loss Function**  
   Common choices:  
   ```python
   Squared Loss = (h(x_i) - y_i)²  
   Absolute Loss = |h(x_i) - y_i|
   ```
3. **Minimize Expected Loss**  
   Closed-form solution for linear regression:  
   `w* = (XᵀX)⁻¹Xᵀy`  
   Where design matrix `X` includes bias term.

### 1.3 Classification Extension
For binary classification (e.g., ripe vs unripe mangoes):
- Use sign function: `ŷ = sign(h(x))`
- Decision boundary: `h(x) = 0` hyperplane

---

## 2. Feature Maps & Nonlinear Patterns

### 2.1 Motivating Example
**Problem**: Parking availability prediction with nonlinear data pattern.  
**Solution**: Create new features via basis functions:
```python
z₁ = |x₁ - noon_time|  # Time feature
z₂ = |x₂ - 70|         # Temperature feature
```
Transforms data to linearly separable space.

### 2.2 Basis Function Framework
1. Map input `x ∈ ℝᵈ` to `ϕ(x) ∈ ℝᵈ'`
2. Train linear model on transformed space:  
   `h(x) = wᵀϕ(x)`

**Common Basis Functions**:
- Polynomial: `ϕ(x) = [x, x², x³]`
- **Gaussian RBF**:  
  `ϕ_j(x) = exp(-||x - μⱼ||²/(2σ²))`  
  Measures similarity to center `μⱼ` with bandwidth `σ`.

---

## 3. Neural Networks

### 3.1 Multilayer Perceptrons (MLPs)
**Architecture**:
```
Input → Hidden Layers (with activation) → Output
```
**Key Components**:
- **Activation Functions**:
  ```python
  ReLU(z) = max(0,z)        # Most common
  Sigmoid(z) = 1/(1+e⁻ᶻ)    # For probabilities
  ```
- **Forward Propagation**:
  ```python
  zⁱ = Wⁱaⁱ⁻¹ + bⁱ  
  aⁱ = g(zⁱ)  # g = activation
  ```

### 3.2 Convolutional Neural Networks (CNNs)
**Core Idea**: Learn spatial hierarchies through filters.

**Convolution Operation**:
```python
# 3x3 vertical edge filter example
filter = [[1, 0,-1],
          [1, 0,-1],
          [1, 0,-1]]
```
- Slide filter across image computing dot products
- Output feature maps capture patterns (edges, textures)

**Architecture**:
```
Input → [Conv → ReLU → Pool]×N → Flatten → Dense → Output
```

---

## 4. Autoencoders: Representation Learning

**Goal**: Learn compressed data encoding while minimizing reconstruction error.

**Structure**:
```
Encoder: x → z (latent space)  
Decoder: z → x̃ (reconstructed input)
```
**Loss**: `L = ||x - x̃||²`

**Applications**: Dimensionality reduction, denoising, pretraining.

---

## Key Takeaways
1. **Linear Models**: Foundation with ERM framework
2. **Nonlinearity**: Achieved via feature maps/RBFs
3. **Neural Networks**: Learn hierarchical representations
4. **CNNs**: Specialized for spatial data
5. **Autoencoders**: Unsupervised representation learning

*Future Directions*: Explore causality, transformers, and reinforcement learning.