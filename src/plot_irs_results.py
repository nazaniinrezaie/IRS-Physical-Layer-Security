
from pathlib import Path
import matplotlib.pyplot as plt

from src.irs_optimization import optimize_irs


def main():
    baseline, optimized, _ = optimize_irs(
        num_elements=16,
        trials=2000,
        seed=42,
    )

    output_dir = Path("results")
    output_dir.mkdir(exist_ok=True)

    fig, ax = plt.subplots(figsize=(7, 5))

    bars = ax.bar(
        ["Baseline", "Optimized IRS"],
        [baseline, optimized],
        color=["#94A3B8", "#2563EB"],
        width=0.5,
    )

    ax.set_ylabel("Secrecy Rate (bits/s/Hz)")
    ax.set_title("IRS Phase Optimization – Random Search")
    ax.set_ylim(0, optimized * 1.2)
    ax.grid(axis="y", alpha=0.2)

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.05,
            f"{height:.3f}",
            ha="center",
        )

    fig.tight_layout()
    fig.savefig(
        output_dir / "irs_optimization.png",
        dpi=200,
    )
    plt.close(fig)

    print("Saved: results/irs_optimization.png")


if __name__ == "__main__":
    main()
