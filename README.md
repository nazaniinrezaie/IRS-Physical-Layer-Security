# Mobile Eavesdropper Tracking — Python Reconstruction

An **independent educational reconstruction** inspired by the themes of my MSc thesis, *Physical Layer Security Analysis with a Mobile Eavesdropper in the Presence of Reconfigurable Intelligent Surfaces* (Shahid Beheshti University, 2025).

## Scope

This initial project simulates a two-dimensional Brownian random walk for a mobile eavesdropper and uses a discrete linear Kalman filter to estimate position from noisy observations. It plots the actual trajectory, noisy measurements, and filtered estimates.

**Important:** This is newly written demonstration code, **not** the original MATLAB thesis implementation. Its parameters and numerical results are illustrative and **do not reproduce or validate** the thesis results. The model is a simplified position-only random walk, not a complete wireless propagation or IRS security simulation. No IRS phase optimization, artificial-noise power allocation, or secrecy-rate calculation is implemented yet.

## Run

Requires Python 3.10+.

```bash
python -m pip install -r requirements.txt
python -m src.simulation
python -m unittest discover -s tests -v
```

The plot is saved to `results/trajectory.png`. The terminal reports observation and filtered position RMSE for the illustrative scenario.

## Next steps

- Document the specific motion and observation assumptions against the thesis model.
- Add Monte Carlo experiments across noise levels and seeds.
- Independently implement a clearly scoped secrecy-rate / IRS example after verifying equations and permission to reuse thesis-specific material.

## Academic context

The thesis studied physical-layer security in the presence of a mobile eavesdropper, using location estimation, reconfigurable intelligent surfaces, artificial noise, and optimization. This repository currently demonstrates **only the tracking component**.
