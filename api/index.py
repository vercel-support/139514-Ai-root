from flask import Flask, request, jsonify
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain import OpenAI
import os
import pyttsx3
from playsound import playsound
from gtts import gTTS

app = Flask(__name__)

os.environ["OPENAI_API_KEY"] = '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'

text_speech = pyttsx3.init()
embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

loader = DirectoryLoader('ScrapData', glob="**/*.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=2500, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
docsearch = Chroma.from_documents(texts, embeddings)

qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=docsearch.as_retriever()
)

@app.route('/api/query', methods=['POST'])
def query():
    data = request.get_json()
    q = data['query']
    answer = qa.run(q)
    return jsonify({'query': q, 'answer': answer})

@app.route('/api/soundQuery', methods=['POST'])
def sound_query():
    data = request.get_json()
    q = data['query']
    answer = qa.run(q)
    tts = gTTS(answer)
    tts.save('answer.mp3')
    playsound('answer.mp3')
    return jsonify({'query': q, 'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
