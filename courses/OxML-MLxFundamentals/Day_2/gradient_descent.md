# Gradient descent from the perspective of optimizing a smooth upper bound given by the 2nd order Taylor expansion

### Goal:

Minimize a smooth function $f: \mathbb{R}^d \to \mathbb{R}$, i.e.

$$
\min_{x \in \mathbb{R}^d} f(x).
$$

---

## Step 1: Prerequisites

1. **Smoothness assumption (L-smoothness):**
   $f$ is differentiable, and its gradient $\nabla f$ is Lipschitz continuous with constant $L > 0$. Formally,

$$
\|\nabla f(x) - \nabla f(y)\| \leq L \|x - y\|, \quad \forall x,y.
$$

2. **Twice differentiability:**
   We assume $f$ is twice differentiable so Taylor expansions apply.
   The Hessian $\nabla^2 f(x)$ exists and is bounded in spectral norm by $L$:

$$
\|\nabla^2 f(x)\|_2 \leq L, \quad \forall x.
$$

---

## Step 2: The 2nd order Taylor expansion at a point $x_k$

For any $x$,

$$
f(x) \approx f(x_k) + \nabla f(x_k)^T (x - x_k) + \frac{1}{2} (x - x_k)^T \nabla^2 f(x_k) (x - x_k).
$$

---

## Step 3: Using the smoothness assumption to get an **upper bound**

Since $\nabla^2 f(x_k) \preceq L I$ (meaning the Hessian is bounded above by $L$ times the identity matrix), we can bound the quadratic term by:

$$
(x - x_k)^T \nabla^2 f(x_k) (x - x_k) \leq L \|x - x_k\|^2.
$$

Therefore, an **upper bound** on $f(x)$ near $x_k$ is:

$$
f(x) \leq f(x_k) + \nabla f(x_k)^T (x - x_k) + \frac{L}{2} \|x - x_k\|^2.
$$

---

## Step 4: Interpretation — The quadratic model as a surrogate function

Define the surrogate function:

$$
Q(x; x_k) := f(x_k) + \nabla f(x_k)^T (x - x_k) + \frac{L}{2} \|x - x_k\|^2.
$$

* $Q$ upper bounds $f$ locally: $f(x) \leq Q(x; x_k)$ for all $x$.
* $Q$ is a **smooth quadratic** easier to minimize.

---

## Step 5: Gradient descent step as minimizing this upper bound surrogate

At iteration $k$, gradient descent picks

$$
x_{k+1} = \arg\min_x Q(x; x_k).
$$

Minimize $Q$ over $x$:

$$
\min_x f(x_k) + \nabla f(x_k)^T (x - x_k) + \frac{L}{2} \|x - x_k\|^2.
$$

Discard constant $f(x_k)$, equivalent to:

$$
\min_x \nabla f(x_k)^T (x - x_k) + \frac{L}{2} \|x - x_k\|^2.
$$

---

## Step 6: Find the minimum by setting derivative to zero

Take derivative w\.r.t $x$:

$$
\nabla f(x_k) + L (x - x_k) = 0,
$$

which implies

$$
x = x_k - \frac{1}{L} \nabla f(x_k).
$$

This is exactly a gradient descent step with step size $\eta = \frac{1}{L}$.

---

## Step 7: Summary and conclusion

* Gradient descent with step size $\eta = \frac{1}{L}$ can be viewed as **minimizing a smooth quadratic upper bound $Q(x;x_k)$ on the original function $f$** constructed from the 2nd order Taylor expansion with Hessian bounded by $L$.
* This interpretation explains the choice of step size and guarantees that $f(x_{k+1}) \leq Q(x_{k+1}; x_k) \leq Q(x_k; x_k) = f(x_k)$, so the function value decreases at each step.
* It links the first-order method (gradient descent) to a 2nd order surrogate optimization without computing Hessians explicitly.