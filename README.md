# wine_choice
# Spanish Wine Dashboard

This project aims to provide a web application dashboard for exploring Spanish wine data. The dashboard allows users to visualize various aspects of Spanish wines, such as price distribution, ratings, acidity, and reviews.

## Getting Started

To run this application on your local machine, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Create a virtual environment and activate it.
4. Install the required packages by running `pip install -r requirements.txt`.
5. Run the Streamlit app by executing `streamlit run app.py` in your terminal.
6. Access the dashboard by navigating to `http://localhost:8501` in your web browser.

## Dataset

The dataset used in this project (`wines_SPA.csv`) contains information about Spanish wines, including price, rating, acidity, year, and number of reviews.

## Exploratory Data Analysis

The exploratory data analysis (EDA) notebook (`EDA.ipynb`) provides insights into the dataset.

During the data analysis, we observed the following insights:
- The cheapest wine in the dataset costs around 4.9, while the most expensive one is priced at 3119.
- Wines from the year 2004 have the highest number of reviews.

## Web Application Dashboard

The web application dashboard (`app.py`) allows users to interactively explore Spanish wine data. It includes:

- A header with project description.
- Histograms displaying price distribution, acidity, and other attributes.
- Scatter plots visualizing relationships between price, rating, and other variables.
- Checkbox for toggling highly rated wines.
- Recommendations of sampled wines based on user preferences.
- Bar chart showing the relationship between the year of the wine and the number of reviews.

## Accessing the Deployed Application

The application is deployed on Render and can be accessed https://wine-project-ru12.onrender.com .


