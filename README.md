# Earth–Sun CR3BP Effective Potential Visualisation

A small Python script for plotting the dimensionless effective potential in the rotating frame of the circular restricted three-body problem (CR3BP).

## Model

The script evaluates the dimensionless effective potential:

`V(x, y) = -((1 - mu)/r1 + mu/r2 + 0.5*(x^2 + y^2))`

where the distances to the two primaries are:

`r1 = sqrt((x + mu)^2 + y^2)`

`r2 = sqrt((x - 1 + mu)^2 + y^2)`

The two primaries are located at:

- Sun: `(-mu, 0)`
- Earth: `(1 - mu, 0)`

These coordinates are in the normalised rotating reference frame.

## Important: mass parameter

The script currently sets `MU = 0.05` to produce a visually clear demonstration. **This is not the actual Earth–Sun mass parameter.** For an Earth–Sun model, use approximately:

`mu = 3.003905077e-6`

To plot the Earth–Sun case, change the `MU` constant near the top of `potential_visualisation.py` to that value. The resulting surface will have a much more extreme difference in scale near the smaller primary.

## Requirements

- Python 3.10 or later
- NumPy
- Matplotlib

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

## Run

```bash
python3 potential_visualisation.py
```

The script opens an interactive Matplotlib 3D surface plot. You can rotate the plot using the mouse.

## Files

- `potential_visualisation.py` — computes and plots the effective potential.
- `requirements.txt` — Python package dependencies.

## Scope and limitations

This is a visualisation of the idealised, dimensionless CR3BP effective potential. It is not a high-fidelity ephemeris model and does not include orbital eccentricity, additional celestial bodies, or perturbations.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
