# Sentiment Analysis of Amazon Product Reviews

## Introduction

This project aims to perform sentiment analysis on Amazon product reviews to extract valuable insights regarding customer opinions and satisfaction levels. 

## Setup

To set up the project environment, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:
```bash 
git clone https://github.com/your-username/Amazon-Review-Sentiment-Analysis.git
```

2. **Navigate to the Project Directory**: Use the `cd` command to navigate into the project directory:

```bash
cd Amazon-Review-Sentiment-Analysis`
```

3. **Create a Virtual Environment**: Create a virtual environment to isolate project dependencies. Depending on your operating system, use one of the following commands:
- On macOS/Linux:
  ```
  python3 -m venv venv
  ```
- On Windows:
  ```
  python -m venv venv
  ```

4. **Activate the Virtual Environment**: Activate the virtual environment using the appropriate command:
- On macOS/Linux:
  ```
  source venv/bin/activate
  ```
- On Windows:
  ```
  venv\Scripts\activate
  ```

5. **Install Dependencies**: Install the required Python dependencies using pip:
```bash
pip install -r requirements.txt`
```


# Dataset

[The link to the dataset from 2018.](https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/#subsets)

Steps to download datset:
1. Navigate to the website and scroll down to the `Files` category.
2. Download the 'Amazon Fashion' reviews dataset (the one with 883,636 reviews).
3. Once downloaded, unzip the file and paste into the `data/raw` directory. 
