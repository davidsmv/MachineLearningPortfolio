# Machine Learning Portfolio

Personal machine learning portfolio with notebook-based projects focused on regression, classification, and dimensionality reduction, plus a small coding-challenges section.

## Repository Overview

```text
MachineLearningPortfolio/
├── classification_projects/
│   └── 1 - Obesity_Risk_with_classifications.ipynb
├── linear_regression_projects/
│   ├── 1 - CLVT_with_linear_regression.ipynb
│   ├── 2 - House_Price_with_Linear_Regression.ipynb
│   └── pairplot_df.png
├── dimensionality_reduction/
│   └── High_Dimensional_Datascape.ipynb
├── coding_challenges/
│   ├── codewars/
│   │   ├── battery.ipynb
│   │   ├── polynomial_regression_office_prices.py
│   │   └── tests.ipynb
│   └── HackerRank/
│       └── test.ipynb
├── data/
│   ├── CLTV_project/
│   ├── house_price_project/
│   ├── obesity_risk_project/
│   └── high_dimensional_datascape_proyect/
├── requirements.in
├── requirements.txt
└── LICENSE
```

## Projects

### Linear Regression
- **[CLTV with Linear Regression](linear_regression_projects/1%20-%20CLVT_with_linear_regression.ipynb)**  
  Predicts Customer Lifetime Value (CLTV) from historical customer features.
- **[House Price with Linear Regression](linear_regression_projects/2%20-%20House_Price_with_Linear_Regression.ipynb)**  
  Builds and evaluates a house-price prediction workflow.

### Classification
- **[Obesity Risk with Classification](classification_projects/1%20-%20Obesity_Risk_with_classifications.ipynb)**  
  Trains classification models for obesity-risk prediction.

### Dimensionality Reduction
- **[High Dimensional Datascape](dimensionality_reduction/High_Dimensional_Datascape.ipynb)**  
  Explores high-dimensional data reduction and visualization techniques.

### Coding Challenges
- Extra practice notebooks and scripts live under `coding_challenges/` (Codewars and HackerRank exercises).

## Data

Project datasets and generated outputs are grouped by project under `data/`.  
Each subfolder contains the files needed by its corresponding notebook (for example `train.csv`, `test.csv`, submissions, and plots).

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/davidsmv/MachineLearningPortfolio.git
   cd MachineLearningPortfolio
   ```
2. (Optional) Create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Launch Jupyter and open any notebook from a project folder.

## Notes

- `requirements.in` is the source dependency list.
- `requirements.txt` is the pinned environment file used for reproducible installs.

## Author

David Martínez  
GitHub: [@davidsmv](https://github.com/davidsmv)  
Email: david-martinezv@outlook.com

## License

Licensed under the MIT License. See [LICENSE](LICENSE) for details.

