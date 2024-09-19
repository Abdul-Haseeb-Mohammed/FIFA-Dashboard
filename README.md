# ⚽ FIFA 21 Player Data Analysis & Dashboard Project

Welcome to the **FIFA 21 Player Data Analysis** project! This project showcases how I cleaned the FIFA 21 dataset using **Python** and developed an **interactive dashboard** in **Tableau** for insightful visualizations.

## 📝 Project Overview

The FIFA 21 dataset contains data on nearly 19,000 football players, including attributes such as height, weight, wage, market value, potential, and more. This project aims to:
- **Clean and preprocess** the raw dataset using **Python** for meaningful analysis.
- **Visualize** the data in **Tableau**, providing interactive and informative visualizations.

## 💻 Technologies Used

- **Python**: For data cleaning and transformation.
- **Pandas & NumPy**: Python libraries used for data manipulation.
- **Tableau**: For interactive visualizations and dashboards.
- **Excel**: For exporting the cleaned data.

## 📊 Key Features of the Tableau Dashboard

The **Tableau** dashboard offers several insightful visualizations:

1. **Wages vs Value**: A scatter plot showing the relationship between player wages and their market value.
2. **Geographical Distribution of Players**: A world map visualizing the number of players per country.
3. **Current Ability vs Potential**: A bar chart comparing players' current overall rating (OVA) with their potential rating (POT).
4. **Player Rating Distribution**: A histogram displaying the distribution of overall player ratings.
5. **Preferred Foot Distribution**: A pie chart showing the percentage of left-footed vs right-footed players.
6. **Player Clusters**: A radial chart grouping players based on similar time spent at clubs.
7. **Potential Growth Players**: A scatter plot displaying players with the highest potential growth in ratings.

## 🔍 Data Cleaning Process

Key data cleaning and transformation steps performed using **Python**:

1. **Height Conversion**: Heights were originally recorded in both centimeters and feet/inches. We standardized all height values to centimeters.
   
2. **Weight Conversion**: Weight values were represented in kilograms and pounds. All values were converted to pounds for consistency.

3. **Wage, Value, and Release Clause Conversion**: These columns had monetary values represented in various formats (e.g., '€1.5M', '€200K'). We converted them into numeric formats for accurate analysis.

4. **Star Ratings**: Columns like 'Weak Foot' (W/F), 'Skill Moves' (SM), and 'International Reputation' (IR) used star-based ratings (e.g., ★★★★). These were converted into numeric values.

5. **Contract Data Handling**: The contract column contained multiple formats (e.g., '2024 ~ 2026', 'ON LOAN'). We extracted contract start and end dates for better structure.

6. **Cleaning Extra Characters**: Removed any unnecessary newline characters, spaces, and symbols from relevant columns.

## 🌍 Insights from the Dashboard

Here are some of the interesting insights derived from the dashboard:

- **Player Distribution**: Most players come from Europe, with countries like Spain, Germany, and England leading in the number of players.
- **Wage vs Value**: Some players have a high market value but earn relatively lower wages, indicating a potential undervaluation in contracts.
- **High Potential Players**: The scatter plot shows which players have the greatest growth potential, useful for teams looking to invest in future stars.

## 📈 Tableau Public Dashboard

Explore the interactive **Tableau** dashboard by visiting the link below:

[🔗 Tableau Public Dashboard](https://public.tableau.com/shared/FK5DWQMPB?:display_count=n&:origin=viz_share_link)
