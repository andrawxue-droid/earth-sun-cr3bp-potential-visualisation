"""
Visualise the effective potential in the circular restricted three-body problem.

The default mass parameter (MU = 0.05) is chosen for a clearly visible
demonstration plot. It is not the Earth-Sun mass parameter.
"""

import matplotlib.pyplot as plt
import numpy as np

# Demonstration value for visualisation only.
MU = 0.05


def effective_potential(x: np.ndarray, y: np.ndarray, mu: float) -> np.ndarray:
    """Return the dimensionless effective potential in the rotating frame."""
    r_sun = np.sqrt((x + mu) ** 2 + y**2)
    r_secondary = np.sqrt((x - 1 + mu) ** 2 + y**2)

    # Avoid division by zero at the idealised point-mass locations.
    r_sun = np.maximum(r_sun, 1e-10)
    r_secondary = np.maximum(r_secondary, 1e-10)

    return -(
        (1 - mu) / r_sun
        + mu / r_secondary
        + 0.5 * (x**2 + y**2)
    )


def main() -> None:
    """Generate and display a 3D surface plot of the effective potential."""
    x = np.linspace(-1.5, 1.5, 500)
    y = np.linspace(-1.5, 1.5, 500)
    X, Y = np.meshgrid(x, y)
    V = effective_potential(X, Y, MU)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection="3d")

    # Clipping improves visibility while retaining the overall surface shape.
    V_clipped = np.clip(V, -3.5, -1.2)
    surface = ax.plot_surface(
        X,
        Y,
        V_clipped,
        cmap="viridis",
        edgecolor="none",
        alpha=0.95,
    )

    fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5, label="Potential V")
    ax.view_init(elev=35, azim=-60)
    ax.set_title("3D Effective Potential Surface")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("V(x, y)")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
