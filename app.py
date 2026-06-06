from flask import Flask, render_template, jsonify, request, session
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
from src.prompts import *
import os
import certifi

os.environ["SSL_CERT_FILE"] = certifi.where()

app = Flask(__name__)
app.secret_key = "your-secret-key"  # needed for session

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

embeddings = download_hugging_face_embeddings()

index_name = "medical-chatbot"
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

chatModel = ChatOpenAI(model="gpt-4o")

# Updated prompt with chat history placeholder
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="chat_history"),  # 👈 memory goes here
    ("human", "{input}"),
])

question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)


@app.route("/")
def index():
    session["chat_history"] = []  # reset on page load
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]

    # Load history from session
    chat_history = []
    for message in session.get("chat_history", []):
        if message["role"] == "human":
            chat_history.append(HumanMessage(content=message["content"]))
        else:
            chat_history.append(AIMessage(content=message["content"]))

    # Invoke RAG chain with history
    response = rag_chain.invoke({
        "input": msg,
        "chat_history": chat_history
    })

    answer = response["answer"]

    # Save updated history to session
    session["chat_history"] = session.get("chat_history", [])
    session["chat_history"].append({"role": "human", "content": msg})
    session["chat_history"].append({"role": "ai", "content": answer})
    session.modified = True

    print("Response:", answer)
    return str(answer)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7860, debug=True)