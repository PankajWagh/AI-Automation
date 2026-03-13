"""
CREATE DATABASE gpt_app;

USE gpt_app;

CREATE TABLE conversations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_message TEXT,
    ai_response TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

from flask import Flask, request, jsonify
import mysql.connector
from openai import OpenAI
import os

app = Flask(__name__)

# OpenAI client
client = OpenAI()

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gpt_app"
)

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    # Call OpenAI
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    ai_response = response.choices[0].message.content

    # Save to MySQL
    cursor = db.cursor()
    sql = "INSERT INTO conversations (user_message, ai_response) VALUES (%s, %s)"
    cursor.execute(sql, (user_message, ai_response))
    db.commit()

    return jsonify({"response": ai_response})


if __name__ == "__main__":
    app.run(port=5000, debug=True)