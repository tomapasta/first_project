# Ravenclaw Gaming Investment Group

# Team Members:
Ako 
Rui
Davy
Charul

# Day 1 - Project Initiation & Data Selection

## 1. Introduction to your project 

We are a group of game investors in Europe, and we are looking for where to invest in the gaming industry. 
- Which platforms are most profitable and sustainable?
- Which genres and titles drive growth?
- How critical ratings align with commercial success.
- Where future investments (publishing, studios, or platform partnerships) will yield the highest returns.

# The fund’s objectives:
- Maximize long‑term return by backing platforms and genres with strong, growing revenues.​
- Control risk by avoiding segments where sales are highly volatile or dependent on rare “hit” games.​


## 2. Dataset Selection

# To look for this, we took the database Gaming Trend 2000-2024 as our research lab to build an investment thesis. 

https://www.kaggle.com/datasets/haseebindata/gaming-industry-trends-1000-rows

This dataset provides detailed information of a thosand console games, including:

Game Title	
Genre	
Platform
Release Year
Developer	
Revenue (Millions $)	
Players (Millions)	
Peak 
Concurrent Players
Metacritic Score
Esports Popularity
Trending Status

This dataset is good to do some market research, look for best genres and most revenue.

## 3. Data Transformation
The original dataset was almost clean, but we've clenead with some techniques, then we save each function on a diferent .py file to apply later. 

Charul:
null values (to check) 
filling Null Values 
column standardization (drop columns, head names, etc.) 

Davy:
outlier handling 
duplicate data

Rui:
format the data (REGIX) 
datatype handling (verify type, convert to int, float, or string) 

Ako:
date/time cleaning 
resetting the index 

# 4. Createad a Kanban board for project management purposes on Trello.
We organized the tasks between before and after lunch for all week. 
https://trello.com/b/p5use74G/ravenclaw


# 5. Created a Github repository for the project:
https://github.com/tomapasta/first_project

We created the repository and defined the colaboration status for all group members. We use branch and merge techniques, so all files are always updated. We have practiced working collaboratively on the repository.


# Day 2 – Data Examination and hyphothesis

On day 2, we began understanding the dataset and created the questions for the following fields:

## 1 . PS vs Xbox vs Nintendo
Which platform has the highest average revenue per game, and which has the highest median revenue per game?
How has the average Critic Score for the top five most active platforms (by number of releases) changed over the last decade (2000-2024)? Which platform shows the steadiest or steepest growth/decline in user score over this period?

## 2. Content and genre 
Which genres (e.g., action, sports, RPG, family) generate the highest average and total revenue by platform?

## 3. Ratings vs financial performance

- Overall, what is the correlation between Metacritic critic score and revenue?
- Is there a “threshold” score (for example, above 80) after which median revenue increases sharply? (tested with bins like 0–69, 70–79, 80–89, 90+.​)

## 4. Portfolio and investment decision questions
If the fund can only invest in one console ecosystem, which platform looks most attractive based on:
- Which companies have scores above 80 from Metacritic
- Which companies delivered the best revenue 
- Revenue growth over time
- How many players are in the genre, and by console, etc 

-  

# Day 3 – Conclusions | Assembling report

## 1. Steps for analysis

- For drawing conclusions we made group by for Platform and Genre and look for each revenue, ascending by total revenue
- We made a corrilation between Metacritic Score and Revenue using a scatter graphic fom matplotlib.pyplot and seaborn
- WE created a score bin for 0, 69, 79, 89, 100 to compare with revenue.   




missing from:
Ako
Davy
Charul



genre_revenue[['Total_Revenue', 'Average_Revenue']] = genre_revenue[['Total_Revenue', 'Average_Revenue']


# Dataset 
...

## Main dataset issues

- ...
- ...
- ...

## Solutions for the dataset issues
...

# Conclussions
...

# Next steps
...
