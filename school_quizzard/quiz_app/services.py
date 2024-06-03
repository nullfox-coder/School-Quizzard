import openai
from . import config
import sqlite3

openai.api_key = config.API_KEY

def initialize_database():
    #connect to the SQlite database
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    
    #create a table if doesn't exist
    cursor.execute('''Create table if not exists questions
                   (id integer primary key, key text unique, value text)''')
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
    response = openai.Completion.create(
        engine = "gpt-3.5-turbo",
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
    while key_exists(cursor,key):
        key = f"{base_key}{index}"
        index +=1

        # Insert questions into our databases

        value = questions
        cursor.execute("Insert into questions(key,value) values (?,?)",(key,value))
        conn.commit()

        return questions

def key_exists(cursor,key):
    cursor.execute("Select count(*) from questions where key=?", (key,))
    count = cursor.fetchone()[0]
    return count>0

def print_all_questions():
    initialize_database()

    #connect to the SQLite database
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    # Retrive all rows from the databases

    cursor.execute("Select * from questions")
    rows = cursor.fetchall()

    return rows