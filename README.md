# Kickstarter-Projects-Analysis

## Overview of Project
Kickstarter is a platform, which uses crowdfunding to fund creative projects. This project examines global Kickstarter campaigns from 2009 to 2017 and aims to uncover trends related to theater projects, specifically plays.

## Purpose
The purpose of this project is gain insights on how different campaigns, specific to plays, fared in relation to their launch dates and their funding goals.

## About Dataset
- Name: name of project - A project is a finite work with a clear goal that you’d like to bring to life. Think albums, books, or
- Category: Category of project
- State: Current condition the project is in
- Currency: Currency used to support
- Launched: date launched
- Deadline: deadline for crowdfunding
- Goal: fundraising goal- the funding goal is the amount of money that a creator needs to complete their project
- Pledged: amount pledged by ( crowd )

## Data Preprocessing with python
- Convert [‘deadline’, ‘launched’] columns to datetime datatype
- Drop duplicates values
- Drop [‘usd-pledged’, ‘goal’, ‘pledged’] columns
- Drop null values from [‘name’] column
- Remove (N,0”) values from dataset
- Create Columns [‘launched_year, ‘deadline_year’] from [‘launched’, ‘deadline’] columns


## Data Analysis With Python
- Total projects by state
- Total Projects by launched year
- Total Projects by main category
- Total Projects by deadline year
- Total Projects by country
- Total Backers by Country
- Total Backers by deadline_year
- Total Pledged by country
- Total Pledged by Deadline year
- Total Successful Projects Per launched_year
- Total Successful Projects Per main_category
- Total Successful Projects Per Country
- Total backers Of Successful Projects Per deadline_year
- Total backers Of Successful Projects Per country
- Total Pledged of Successful Projects Per main_category
- Total Pledged Of Successful Projects Per deadline_year

## Data Visualization with Power BI
- Create Measures OF
  o Total Projects # Card
  o Total Backers # Card
  o Countries # Card
  o Total Goals # Card
  o Total Pledged # Card
- Total Projects by status # Column Chart
- Total Pledged by country # Bar Chart
- Total Projects by Launched Year # Stacked Area Chart
- Total Projects by Main Category and Category and Name # Column chart and click drill down to view other categories and name
- Total Pledged & Total Goal by Deadline Years # Area chart
