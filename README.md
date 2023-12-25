# Movie Recommendation System

This repository contains the code and dataset for building a Movie Recommendation System using the TMDB 5000 movie dataset

## Overview

This project focuses on analyzing the TMDB 5000 movie dataset to build a recommendation system. The system uses features like movie genres, directors, and cast to suggest similar movies based on user preferences.

## Dataset

- **TMDB 5000 Credits Dataset**: Contains details about movie credits, including cast and crew information.
- **TMDB 5000 Movies Dataset**: Contains general information about movies such as title, genres, runtime, and average ratings.

## Setup

To run the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/Blaze-coder3/Bharat-Intern.git
   ```

2. Install the necessary libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```
Certainly! Below is a simple section you can include in your documentation to guide users on creating a static folder for CSS files and a template folder for HTML files:

---

## Project Structure

Before running the Movie Recommendation System, make sure your project structure includes the necessary folders for organizing static files and templates.

### 1. Static Folder

The `static` folder is used to store static assets such as CSS files, images, or JavaScript files. In this project, we will use it to store the CSS file for styling our HTML templates.

Create a folder named `static` in your project directory.

```plaintext
/your_project_directory
|-- static
   |-- styles.css
   |-- (other static files)
|-- app.py
|-- (other project files)
```

### 2. Template Folder

The `templates` folder is used to store HTML templates that Flask will render. These templates define the structure of your web pages.

Create a folder named `templates` in your project directory.

```plaintext
/your_project_directory
|-- static
   |-- styles.css
   |-- (other static files)
|-- templates
   |-- index.html
   |-- (other HTML templates)
|-- app.py
|-- (other project files)
```


## Exploratory Data Analysis

The initial step involves understanding the dataset by exploring its structure, columns, and basic statistics.

## Data Preprocessing

- Merging credits and movies datasets based on the movie ID.
- Extracting features like directors, genres, and cast from the dataset.
- Handling missing values and duplicates.

## Visualization

Visualizations are essential for understanding patterns and insights from the data. This project includes:
- Bar charts for top directors by movie count.
- Histograms for movie runtimes and average ratings.

## Saving Data

The processed and merged dataset is saved as `merged_data.csv` for future use or analysis.

## Usage

You can run the Jupyter Notebook [here](https://colab.research.google.com/github/Blaze-coder3/Bharat-Intern/blob/Movie-Recommendation/Movie_Recommendation.ipynb) or clone the repository and execute the code locally.

## Contributors

A Syed Khwaja
