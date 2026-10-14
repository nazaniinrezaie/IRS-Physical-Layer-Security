
import numpy as np

def secrecy_rate(h_bob, h_eve, noise_power=0.1):
    """Calculate a simplified secrecy rate in bits/s/Hz."""
    snr_bob = np.abs(h_bob) ** 2 / noise_power
    snr_eve = np.abs(h_eve) ** 2 / noise_power

    return max(
        0.0,
        np.log2(1 + snr_bob) - np.log2(1 + snr_eve)
    )


def optimize_irs(num_elements=16, trials=2000, seed=42):
    """Random-search optimization of IRS phase shifts."""
    rng = np.random.default_rng(seed)

    # Simplified complex channel coefficients
    bob_channel = (
        rng.normal(size=num_elements)
        + 1j * rng.normal(size=num_elements)
    ) / np.sqrt(2 * num_elements)

    eve_channel = (
        rng.normal(size=num_elements)
        + 1j * rng.normal(size=num_elements)
    ) / np.sqrt(2 * num_elements)

    def evaluate(phases):
        reflection = np.exp(1j * phases)
        h_bob = np.sum(bob_channel * reflection)
        h_eve = np.sum(eve_channel * reflection)
        return secrecy_rate(h_bob, h_eve)

    baseline = evaluate(np.zeros(num_elements))

    best_rate = baseline
    best_phases = np.zeros(num_elements)

    for _ in range(trials):
        phases = rng.uniform(0, 2 * np.pi, num_elements)
        rate = evaluate(phases)

        if rate > best_rate:
            best_rate = rate
            best_phases = phases.copy()

    return baseline, best_rate, best_phases


if __name__ == "__main__":
    baseline, optimized, _ = optimize_irs()

    print(f"Baseline secrecy rate: {baseline:.4f} bits/s/Hz")
    print(f"Optimized secrecy rate: {optimized:.4f} bits/s/Hz")
    print(f"Improvement: {optimized - baseline:.4f} bits/s/Hz")
