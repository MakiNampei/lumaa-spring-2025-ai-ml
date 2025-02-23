# Movie Recommendation System

### Video drive link
https://drive.google.com/file/d/1urAn6HP4jziNVodiMHf62_cnlzRIBpt_/view?usp=sharing

## Project Overview
This is a **content-based recommendation system** that suggests movies based on a user's **short text description**. The system uses **TF-IDF vectorization** and **cosine similarity** to determine the most relevant movie recommendations.

## Dataset
- **Source**: The dataset (`movies.csv`) is manually created for testing purposes.
- **Location**: Stored in the `data/` directory.
- **Columns:**
  - `title`: Movie title
  - `description`: A short summary of the movie
- **Example:**
  ```csv
  title,description
  "Guardians of the Galaxy","A group of intergalactic criminals must pull together to stop a fanatical warrior."
  "Star Wars","Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, and a Wookiee to save the galaxy."
  "Thor: Ragnarok","Thor must escape the alien planet Sakaar in time to save Asgard from Hela."

## How to Run the System

### Install Dependencies
Make sure you have Python installed. Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

### Running the System
```bash
python src/recommend.py "I love thrilling action movies set in space, with a comedic twist."
```

## Expected Output

### For a user input like:
```bash
"I love thrilling action movies set in space, with a comedic twist."
```
### result should be
```bash
1. Guardians of the Galaxy - A group of intergalactic criminals must pull together to stop a fanatical warrior.
2. Star Wars - Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, and a Wookiee to save the galaxy.
3. Thor: Ragnarok - Thor must escape the alien planet Sakaar in time to save Asgard from Hela.
```
