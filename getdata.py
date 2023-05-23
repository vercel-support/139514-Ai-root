import sys
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain import OpenAI
import os
import pyttsx3
from playsound import playsound
from gtts import gTTS

os.environ["OPENAI_API_KEY"] = "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"

text_speech = pyttsx3.init()

embeddings = OpenAIEmbeddings(openai_api_key= "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") #INPUT API KEY HERE#""

loader = DirectoryLoader('ScrapData', glob="**/*.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=2500, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
texts = text_splitter.split_documents(documents)
#%%
docsearch = Chroma.from_documents(texts, embeddings)
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=docsearch.as_retriever()
)
def query(q):
    print("Query: ", q)
    answer = qa.run(q)
    print("Answer: ", answer)

def soundQuery(q):
    print("Query: ", q)
    answer = qa.run(q)
    tts = gTTS(answer)
    tts.save('answer.mp3')
    print("Answer: ", answer)
    playsound('answer.mp3')