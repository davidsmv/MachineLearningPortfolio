# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Notebook-first machine learning portfolio. Each top-level folder groups projects by ML technique. All work happens in Jupyter notebooks except HackerRank scripts which use stdin/stdout.

## Architecture

- `linear_regression_projects/` – regression notebooks (CLTV, House Price)
- `classification_projects/` – classification notebooks (Obesity Risk)
- `dimensionality_reduction/` – dimensionality-reduction notebooks
- `coding_challenges/` – practice scripts and notebooks (Codewars, HackerRank)
- `data/` – per-project subfolders with datasets, submissions, and output plots

Notebooks reference data via relative paths: `../data/<project_name>/`.

## Dependency Management

Uses **pip-compile** from pip-tools. PyTorch is pinned to CUDA 12.1 wheels.

- `requirements.in` – edit this to add/remove dependencies
- `requirements.txt` – generated lockfile, do not edit by hand

```bash
pip-compile --extra-index-url=https://download.pytorch.org/whl/cu121 requirements.in
pip install -r requirements.txt
```

## Key Libraries

pandas, scikit-learn, matplotlib, seaborn, plotly-express, statsmodels, scikit-optimize, umap-learn, ctgan, PyTorch (CUDA 12.1), torchvision, torchaudio.

## Conventions

- Notebook filenames: `<N> - <Title>.ipynb` (numbered, descriptive)
- New projects: create notebook in the appropriate technique folder, place data under `data/<project_name>/`
- `.csv` files are gitignored; generated outputs (plots, submissions) go in the project's data folder
- HackerRank `.py` files read from stdin to match their I/O format
- Python 3.11.9 with `.venv/` virtual environment
