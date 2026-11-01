"""Plot contours of the dimensionless CR3BP effective potential."""

import matplotlib.pyplot as plt
import numpy as np

# Demonstration value for visualisation only; not the Earth-Sun value.
MU = 0.05


def potential(x: np.ndarray, y: np.ndarray, mu: float) -> np.ndarray:
    """Return the dimensionless effective potential in the rotating frame."""
    r_s = np.sqrt((x + mu) ** 2 + y**2)
    r_e = np.sqrt((x - 1 + mu) ** 2 + y**2)

    # Avoid division by zero at the idealised point-mass locations.
    r_s = np.where(r_s == 0, 1e-10, r_s)
    r_e = np.where(r_e == 0, 1e-10, r_e)

    return -(
        (1 - mu) / r_s
        + mu / r_e
        + 0.5 * (x**2 + y**2)
    )


def main() -> None:
    """Generate and display a 2D contour map of the effective potential."""
    x = np.linspace(-1.5, 1.5, 500)
    y = np.linspace(-1.5, 1.5, 500)
    X, Y = np.meshgrid(x, y)
    Z = potential(X, Y, MU)

    plt.figure(figsize=(9, 7))

    levels = np.concatenate(
        [
            np.linspace(-15, -3, 15),
            np.linspace(-2.9, -1.2, 35),
        ]
    )

    contours = plt.contour(
        X,
        Y,
        Z,
        levels=levels,
        cmap="coolwarm",
        linewidths=1.2,
    )
    plt.clabel(contours, inline=True, fontsize=8, fmt="%.1f")
    plt.colorbar(contours, label="Potential V(x, y)")

    plt.scatter(
        [-MU], [0],
        color="red",
        s=180,
        edgecolors="black",
        zorder=5,
        label="Sun (-mu, 0)",
    )
    plt.scatter(
        [1 - MU], [0],
        color="deepskyblue",
        s=90,
        edgecolors="black",
        zorder=5,
        label="Earth (1 - mu, 0)",
    )

    plt.title("Effective Potential Contour Map")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color="gray", linestyle="--", linewidth=0.8)
    plt.axvline(0, color="gray", linestyle="--", linewidth=0.8)
    plt.legend(loc="upper right")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
