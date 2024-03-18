import opentai
from . import config
import sqlite3

openai.api_key = config.API_KEY

def initialize_database(self):
    #connect to the SQlite database
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    
    #create a table if doesn't exist
    cursor.execute('''Create table if not exists questions
                   (id integer primary key, key text unique, vale text)''')
    conn.commit()
    conn.close()

def generate_question(text):
    initialize_database()

    #connect to the SQLite database
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    
    #defining prompt
    prompt = f"Create a practice test with multiple choice questions on the following text:\n{text}\n\n"\
             f"Each question should be on a different line. Each question should have 4 possible answers."\
             f"Under the possible answer we should have the correctanswer"
    
    #generating question using the CHATGPT API
    response = openai.completion.create(
        engine = "text_davinci-003",
        prompt = prompt,
        max_token = 3500,
        stop = None,
        temperature = 0.7
    )

    # extract the generated questions from the API Responses

    questions = response.choices[0].text

    # generate a unique key for our questions

    base_key = ''.join(text.split()[:2])
    key = base_key
    index = 1
    # while

def key_exists():
    cursor.execute("S   ")

def print_all_questions():
    pass