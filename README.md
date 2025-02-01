# AI Tweet Generator

## Overview

This AI Tweet Generator is a Flask web application that generates viral tweets based on on chain data and social media activity. It utilizes the Langchain library with Google Generative AI to create engaging tweets that incorporate crypto slang, emojis, and relevant hashtags.

## Features

- Generates tweets based on mock on-chain data and social media mentions.
- Uses a language model to create engaging and viral content.
- Provides a simple web interface to trigger tweet generation.

## Technologies Used

- **Python**: The programming language used for the application.
- **Flask**: A lightweight web framework for building the web application.
- **Langchain**: A library for working with language models and prompts.
- **Google Generative AI**: The language model used for generating tweets.
- **dotenv**: A library for loading environment variables from a `.env` file.
- **HTML/CSS**: For creating the web interface.

## Application Interface 
![Screenshot (324)](https://github.com/user-attachments/assets/0d8655f6-08a7-459e-afb9-ee24eef1c16b)
![Screenshot (322)](https://github.com/user-attachments/assets/525a3406-c599-4cb5-ab66-c979441f4046)
![Screenshot (323)](https://github.com/user-attachments/assets/7fc39b04-5f03-4b27-b262-3219bc62eba5)

## Demo Screen Recording 


https://github.com/user-attachments/assets/329b6bc9-ba85-464a-a3c2-38c80c93d65d



## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gulshan-100/AI_Tweet_Generator_using_LLM.git
   cd AI_Tweet_Generator_using_LLM
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your Google API key:
   ```plaintext
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Click on the "Generate Tweets" button to generate and view the tweets.

## Files Description

- **app.py**: The main entry point of the application, defining the Flask routes and handling requests.
- **llm.py**: Initializes the language model used for generating tweets.
- **mock_data.py**: Contains mock data for social media mentions and on-chain data generation.
- **tweet_generator.py**: Implements the logic for generating tweets using the language model and the provided data.
- **templates/index.html**: The HTML template for the web interface.

## 

## Acknowledgments

- [Langchain](https://langchain.com/) for providing the tools to work with language models.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables.
