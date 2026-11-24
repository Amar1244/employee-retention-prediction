# Employee Retention Prediction

A machine learning project that predicts whether an employee is likely to stay or leave, with a deployed Streamlit app and a Power BI dashboard. HR teams can enter an employee's details and get a prediction with its probability, to act on attrition risk early.

## What it does

- **Predicts attrition risk.** Classifies an employee as likely to stay or leave and shows the probability.
- **Compares several models.** Logistic Regression, Random Forest and XGBoost were trained and compared. XGBoost is the deployed model.
- **Handles class imbalance.** SMOTE balances the classes, and the final model reaches about 85% accuracy.
- **Live app for HR teams.** A Streamlit app takes inputs such as city, education, experience, company size and training hours, and returns the result instantly.
- **Dashboard.** A Power BI dashboard summarises attrition patterns in the data.

## Keywords

Machine Learning · Predictive Modeling · Classification · Employee Attrition · HR Analytics · XGBoost · Random Forest · Logistic Regression · SMOTE · Streamlit · Power BI · Data Science · Python

## Tech Stack

- Python, pandas, NumPy
- scikit-learn (preprocessing, Logistic Regression, Random Forest, label encoding)
- [XGBoost](https://xgboost.readthedocs.io/) for the final model
- imbalanced-learn (SMOTE) for class imbalance
- [Streamlit](https://streamlit.io/) for the deployed app
- Power BI for the dashboard

## Project Structure

| Folder / File | Purpose |
| :--- | :--- |
| `Model and Datasets_Employee_Rentenion_Predection/` | Training notebook and the train and test datasets |
| `Deployment Employee Retention Prediction/` | Streamlit app, trained XGBoost model and encoders |
| `Dashboard_Employee Retention Prediction/` | Power BI dashboard (`.pbix`) |
| `Description.docx` | Project description |

## Author

**Amar Chaurasiya**, Data Scientist working as an AI Engineer.

- Email: [amarchaurasiya124@gmail.com](mailto:amarchaurasiya124@gmail.com)
- LinkedIn: [linkedin.com/in/amar-chaurasiya-163788262](https://www.linkedin.com/in/amar-chaurasiya-163788262)
- Portfolio: [amarchaurasiya.vercel.app](https://amarchaurasiya.vercel.app)
