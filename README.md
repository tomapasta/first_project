# Gaming Investment Group

## Team Members:
A.K, 
R.P, 
D.G, 
C.M

## Project Overview
This project analyses global gaming industry trends (2000–2024) to identify the most promising investment opportunities across platforms, genres, and publishers using data analysis and visualisation.

- **Objective:** Identify profitable and stable investment opportunities in gaming (console).  
- **Approach:** Executed a multi-dimensional performance analysis using segmented time-series to correlate critical sentiment, player engagement, and platform growth trends for high-ROI investment mapping.
  
📊 Dataset

 [Gaming Trend 2000–2024](https://www.kaggle.com/datasets/haseebindata/gaming-industry-trends-1000-rows).

## 📈 Key Findings 

- **The Quality Multiplier**: A direct correlation exists between high Metacritic scores and total revenue. Higher critical acclaim consistently drives higher sales.
- **Platform Powerhouses**: * Nintendo Switch leads in revenue per game, PlayStation maintains the largest total player base.
- **Genre Dominance** : The industry is anchored by Action, Strategy, and Sports, which consistently attract the highest volume of players.
- **Strategic Growth** : Investing in platforms showing a multi-year growth trend is a confirmed indicator of high ROI.

## 🎯 Recommendations

- **Primary Strategy**: Focus on Multi-platform development with a specialised optimisation for Nintendo consoles to maximise revenue per unit.
- **Prioritise Quality**: Aim for a Metacritic score of 80%+ (referencing Sony's benchmark of 47+ titles) to ensure peak revenue performance.
- **Target High-Volume Genres**: Align development resources toward Action, Strategy, or Sports to capture the broadest market share.
- **Scale via PlayStation**: Utilise PlayStation's massive player base to generate high total volume, while leveraging Nintendo for high-margin returns.


## 🛠️  Tools & Libraries

![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Visualization-4C72B0?style=flat&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=flat&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter&logoColor=white)
![ERD](https://img.shields.io/badge/ERD-Database%20Schema-00758F?logo=databricks&logoColor=white)
![Trello](https://img.shields.io/badge/Trello-%23026AA7.svg?logo=Trello&logoColor=white)


## Daily Task Flow 

## Day 1 - Project Initiation & Data Selection
On Day 1 we focused on dataset selection and cleaning. 

### 1. Introduction of the Project 

We are a group of game investors in Europe, and we are looking for where to invest in the gaming industry. 
- Which platforms are most profitable and sustainable?
- Which genres and titles drive growth?
- How critical ratings align with commercial success.
- Where future investments (publishing, studios, or platform partnerships) will yield the highest returns.

### The fund’s objectives:
- Maximize long‑term return by backing platforms and genres with strong, growing revenues.​
- Control risk by avoiding segments where sales are highly volatile or dependent on rare “hit” games.​


### 2. Dataset Selection

To look for this, we took the database Gaming Trend 2000-2024 as our research lab to build an investment thesis. 

This dataset provides detailed information of a thousand console games, including:

**Dataset Features:**
- Game Title  
- Genre  
- Platform  
- Release Year  
- Developer  
- Revenue (Millions $)  
- Players (Millions)  
- Peak Concurrent Players  
- Metacritic Score  
- Esports Popularity  
- Trending Status  

This dataset is useful for market research, such as identifying the best-performing genres and the highest revenue segments.

### 3. Data Transformation
The original dataset was almost clean, but we cleaned it using several techniques, then saved each function in a different .py file to apply later. 

### C.M:
null values (to check) 
filling Null Values 
column standardization (drop columns, head names, etc.) 

### D.G:
outlier handling 
duplicate data

### R.P:
format the data (REGIX) 
datatype handling (verify type, convert to int, float, or string) 

### A.K:
date/time cleaning 
resetting the index 

### 4. Created a Kanban Board for Project Management Purposes on Trello.
Using Kanban Board, A.K managed the tasks on Trello, organising the tasks between AM/PM for the whole duration of 4 days project. 

<img width="1762" height="609" alt="Screenshot 2026-02-07 113142" src="https://github.com/user-attachments/assets/b395256a-e796-4cd0-ba3c-2621fb0bbb1a" />


### 5. Created a Github Repository for the Project

We created the repository and defined the collaboration status for all group members using branch and merge techniques, so all files are always updated. We have practiced working collaboratively on the repository.

## Day 2 – Data Examination and Hypothesis

On Day 2, we began understanding the dataset and created the questions for the following fields:

### 1 . PS vs Xbox vs Nintendo
Which platform has the highest average revenue per game, and which has the highest median revenue per game?
How has the average Critic Score for the top five most active platforms (by number of releases) changed over the last decade (2000-2024)? Which platform shows the steadiest or steepest growth/decline in user score over this period?

### 2. Content & Genre 
Which genres (e.g., action, sports, RPG, family) generate the highest average and total revenue by platform?

### 3. Ratings vs Financial Performance

- Overall, what is the correlation between Metacritic critic score and revenue?
- Is there a “threshold” score (for example, above 80) after which median revenue increases sharply? (tested with bins like 0–69, 70–79, 80–89, 90+.​)

### 4. Portfolio & Investment Decision Questions
If the fund can only invest in one console ecosystem, which platform looks most attractive based on:
- Which companies have scores above 80 from Metacritic
- Which companies delivered the best revenue 
- Revenue growth over time
- How many players are in the genre, and by console, etc 

## Day 3/4 – Conclusions & Assembling Report
On Day 3/4 we focused on insights and visualization

### 1. Data Transformation

We cleaned the dataset, removed unnecessary columns, and created new grouped variables for analysis. We used the following techniques: 

- For drawing conclusions we made a group for Platform and Genre and looked for each revenue, ascending by total revenue.
- We made a correlation between Metacritic Score and Revenue using a scatter graphic from `matplotlib.pyplot` and `seaborn`.
- We created a score bin for 0, 69, 79, 89, 100 to compare with revenue.   
- Used `matplotlib.pyplot` and `barplot` to look for correlations and comparisons. 
- Applied datetime conversion and index resetting, 
- Deleted duplicates, analyzing outliers by looking at normal values of the dataset using boxplot
- Web Scraping for unit sales on Nintendo titles 
- Handled null values, dropped unnecessary columns, and renamed columns
- Bar Graphs using `matplotlib` to analyse players by genres, platforms
- Used `groupby` to sort Metacritics threshold, `matplotlib` to visualise the growth of each company and to identify top revenue developers
- Identify top revenue developers over the 3 years by using line graphs. 

### 2. Analysis & Conclusions
After we got the data clean, we analyzed the data for every question we had.

One of the decisions we made, right in the beginning, was to drop PC and mobile on our strategy, because they are a volatile market, with many games depending on free-to-play models, microtransactions, etc.
For this, we focused on the main consoles (PlayStation, Nintendo, Xbox), looking for real gaming unit sales, but still, used all data for statistical purposes. 

Looking at PS vs Xbox vs Nintendo, we concluded that Switch had the highest revenue per game, followed by cross-platform. 
In content and genre, again, cross-platform had the most revenue, with higher numbers in strategy and adventure. 
We tried to see if there was a correlation between Metacritic scores and revenue, but we find that there´s no correlation. 
    *Metacritic is a platform that combines the average scores from all gaming outlets that give games a review score. 

We found that the games that scored the best in Metacritic (80+) had the best total revenues. 
Looking for best portfolios to invest in, Sony was the company with more games above 80+ scores, followed by Microsoft and Rockstar. 
In revenues, Sony still had the best total income, followed by Activision and Rockstar. 

Looking for the most played genres by number of players, we found that action, strategy and sports attract the highest total number of players across the gaming industry. 
Overall, genres with fast-paced or strategic gameplay tend to dominate player engagement. 

In the conclusions, the Ravenclaw Gaming Investment Group decided to invest in multiplatforms, with a preference toward Nintendo consoles. 
Nintendo Switch has the lowest player totals comparatively, but they still represent major segments in the market. 
Nintendo has the highest per-game revenue median, so probably high revenue per person/game. Mario Kart and Animal Crossing are still very profitable. 

And finally, for the decision to cross-platform, we found that the strong performance in this highlights an industry trend: players prefer games that don’t lock them to a single console.

### 3. Challenges in the Project
The team was very confident in the dataset chosen and the business plan to invest on a console. The team had some minor challenges in coding, so we decided to keep it on Python/Pandas.
There was some confusion at the start with pushing, pulling, and changing the environment from the files in the repository, but never have conflicts to resolve.
Every team member worked in their own Jupyter file, then we compiled all code from contributions to a main final file.
We had some challenges compiling all the code in the same file, because of conflicts in column names and some rows. This could be avoided if all members started to code after the cleaning process.


## Day 5 – Project Presentation
On Day 5 we presented our findings and pitched the business plan. 
We finish the final code, with legends about the code to fill best practises learnings. 

### 1. Relationship charts

We drew a Relationship chart in Miro from our database, for practise purposes. 
<img width="1053" height="718" alt="image" src="https://github.com/user-attachments/assets/7c6ca3b2-c04c-400c-982a-8f5358b53d95" />


Than we translate the chart to DrawDB to get code for SQL, for practise purposes. 
https://www.drawdb.app/editor?shareId=aefa044a1175f8ca638d2245f72bc3eb

Chart images saved in Figure folder. 

### 2. Final project presentation
The results from the analysis available upon request.

This project helped our team practice collaborative data analysis, investment reasoning, and Python-based visualization while exploring key trends in the global gaming industry.

