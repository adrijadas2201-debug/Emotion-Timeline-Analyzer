# Emotion Timeline Analysis using NLP

## Overview

This project analyzes the emotions of user-entered text messages and visualizes how emotions change over time. It uses a pre-trained transformer model to classify emotions such as joy, sadness, anger, fear, and more.

The project combines Natural Language Processing (NLP) with data visualization to understand emotional trends in conversations.

---

## Features

* Accepts multiple user input messages
* Detects emotions using a pre-trained NLP model
* Stores results in a structured table using pandas
* Generates timestamps for each message
* Displays results in terminal
* Plots emotion score vs time graph

---

## Tech Stack

* Python
* Transformers (Hugging Face)
* Pandas
* Matplotlib

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/emotion-timeline-analysis.git
cd emotion-timeline-analysis
```

### 2. Install dependencies

```bash
pip install transformers pandas matplotlib
```

---

## Usage

Run the program:

```bash
python main.py
```

Enter the number of messages and input them one by one.

The program will:

* Display emotion analysis in terminal
* Show a graph of emotion score over time

---

## Technical Approach

### 1. Input Collection

User inputs multiple messages which are stored in a list.

### 2. Emotion Detection

A pre-trained transformer model is used:

```python
pipeline('text-classification', model="j-hartmann/emotion-english-distilroberta-base")
```

It returns:

* Emotion label
* Confidence score

### 3. Data Processing

Results are stored in a pandas DataFrame with:

* Message
* Emotion label
* Score
* Timestamp

### 4. Time Generation

Each message is assigned a timestamp:

```python
datetime.now() + timedelta(seconds=i*2)
```

### 5. Visualization

* Graph plotted using matplotlib
* X-axis shows time
* Y-axis shows emotion score

---

## Output

### Terminal Output

Displays a table containing:

* Message
* Emotion
* Score
* Time

### Graph Output

A line graph showing emotion score over time.

---

## Notes

* First run may take time due to model download
* Internet connection is required initially
* Warning messages from the model can be ignored

---


## Use Cases

* Mental health tracking
* Chat emotion analysis
* Sentiment tracking
* AI journaling systems

---


## Future Improvements

* Build a web application using Flask
* Add real-time chat emotion tracking
* Store data in a database
* Export results to CSV
* Improve graph visualization with colors

---



