from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
import openai
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from models import Base, FileContent, Conversation
from utils import process_file

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/chatbot'
engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
session = Session()

openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        content = process_file(file_path)
        new_file = FileContent(filename=filename, content=content)
        session.add(new_file)
        session.commit()
        return redirect(url_for('index'))

@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.form['question']
    # Implementar lógica para buscar resposta
    response = openai.Completion.create(
        engine="davinci",
        prompt=question,
        max_tokens=150
    )
    answer = response.choices[0].text.strip()
    new_conversation = Conversation(question=question, answer=answer)
    session.add(new_conversation)
    session.commit()
    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug=True)
