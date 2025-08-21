# 🌊 Sea Level Predictor

This project predicts **future sea level rise** using statistical modeling techniques.  
It is designed as part of a data analysis and prediction exercise to study climate change impacts on global sea levels.  

---

## 📌 Project Overview
Rising sea levels are a major consequence of climate change. This project analyzes sea level data and applies regression techniques to estimate future trends.  
The implementation follows a modular approach with:
- **Data analysis and regression in `sea_level_predictor.py`**
- **Execution and visualization in `main.py`**
- **Unit tests in `test_module.py`**

---

## 🚀 Features
- Reads and processes sea level dataset (historical data).
- Creates scatter plots for observed sea levels.
- Fits linear regression lines to predict sea level rise:
  - For the entire dataset.
  - For data after the year 2000 (to check recent trends).
- Extends prediction up to the year 2050.
- Includes testing module for validation.

---

## 🛠️ Tech Stack
- **Language**: Python 3
- **Libraries**:
  - `pandas`
  - `matplotlib`
  - `scipy`
  - `pytest` (for testing)

---

## 📦 Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/harshitt486/sealevelpredictor.git
   cd sealevelpredictor
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
(If requirements.txt is not available, install manually: pip install pandas matplotlib scipy pytest)

▶️ Usage
Run the predictor:

bash
Copy
Edit
python main.py
This will:

Load the dataset.

Generate a scatter plot with regression lines.

Save the output plot as sea_level_plot.png.

🧪 Testing
Run the unit tests:

bash
Copy
Edit
pytest test_module.py
📊 Example Output
The project generates a plot showing:

Historical sea level data (scatter points).

Regression line (1880–present).

Regression line (2000–present).

Predictions extended to 2050.

🔮 Future Improvements
Use advanced time-series models (ARIMA, LSTM).

Incorporate global temperature data for multi-variable prediction.

Deploy as a web app using Flask/Streamlit.
