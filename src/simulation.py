"""Illustrative 2D Brownian motion tracking with a linear Kalman filter.

Independent educational reconstruction inspired by thesis topics; not original thesis code.
"""
import numpy as np
import matplotlib.pyplot as plt


def simulate(steps=150, seed=42, process_std=0.35, measurement_std=1.8):
    rng = np.random.default_rng(seed)
    truth = np.zeros((steps, 2))
    for i in range(1, steps):
        truth[i] = truth[i - 1] + rng.normal(0, process_std, 2)
    measurements = truth + rng.normal(0, measurement_std, (steps, 2))
    estimates = np.zeros_like(truth)
    x = np.zeros(2)
    P = np.eye(2) * 5
    Q = np.eye(2) * process_std**2
    R = np.eye(2) * measurement_std**2
    I = np.eye(2)
    for i, z in enumerate(measurements):
        P = P + Q
        K = P @ np.linalg.inv(P + R)
        x = x + K @ (z - x)
        P = (I - K) @ P @ (I - K).T + K @ R @ K.T
        estimates[i] = x
    return truth, measurements, estimates


def main():
    from pathlib import Path
    truth, measurements, estimates = simulate()
    out = Path(__file__).resolve().parents[1] / 'results'
    out.mkdir(exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(truth[:, 0], truth[:, 1], label='True trajectory')
    ax.scatter(measurements[:, 0], measurements[:, 1], s=8, alpha=0.35, label='Noisy observations')
    ax.plot(estimates[:, 0], estimates[:, 1], label='Kalman estimate')
    ax.set(xlabel='X (arbitrary units)', ylabel='Y (arbitrary units)', title='Illustrative mobile eavesdropper tracking')
    ax.legend()
    fig.tight_layout()
    fig.savefig(out / 'trajectory.png', dpi=180)
    plt.close(fig)
    raw_rmse = np.sqrt(np.mean(np.sum((measurements - truth)**2, axis=1)))
    filtered_rmse = np.sqrt(np.mean(np.sum((estimates - truth)**2, axis=1)))
    print(f'Measurement RMSE: {raw_rmse:.3f}; Kalman RMSE: {filtered_rmse:.3f}')


if __name__ == '__main__':
    main()
