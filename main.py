import os
import streamlit as st
import pickle
import time
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()  # Take env variables from .env

st.title("News Research Tool")
st.sidebar.title("News Article URLs")

urls = []
file_path = "faiss_store_openai.pkl"

main_placefolder = st.empty()
llm = OpenAI(temperature=0.9, max_tokens=500)

for i in range(3):
    url = st.sidebar.text_input(f"URL {i + 1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
embeddings = OpenAIEmbeddings()
if process_url_clicked:
    # load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placefolder.text("Data Loading...Started...✅✅✅")
    data = loader.load()

    if data:
        # split data
        text_splitter = RecursiveCharacterTextSplitter(
            separators=['\n\n', '\n', '.', ','],
            chunk_size=1000
        )
        main_placefolder.text("Text Splitter...Started...✅✅✅")
        docs = text_splitter.split_documents(data)

        if docs:
            # create embeddings and save it to FAISS index
            vectorstore_openai = FAISS.from_documents(docs, embeddings)
            main_placefolder.text("Embedding Vector Started Building...✅✅✅")
            time.sleep(2)

            # Save the FAISS index to a pickle file
            vectorstore_openai.save_local(file_path)
        else:
            main_placefolder.text("Text Splitter produced empty documents. Check data.")
    else:
        main_placefolder.text("Data loading failed. Check URLs or network connection.")


# query = main_placefolder.text_input("Question: ")
# if query:
#     if os.path.exists(file_path):
#         vectorIndex = FAISS.load_local(file_path, embeddings)
#         chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorIndex.as_retriever())
#         results = chain({"question": query}, return_only_outputs=True)
#         st.header("Answer")
#         st.subheader(results["answer"])

query = main_placefolder.text_input("Question: ")
if query:
    if os.path.exists(file_path):
        vectorIndex = FAISS.load_local(file_path, embeddings,allow_dangerous_deserialization=True)
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorIndex.as_retriever())
        result = chain({"question": query}, return_only_outputs=True)
        # result will be a dictionary of this format --> {"answer": "", "sources": [] }
        st.header("Answer")
        st.write(result["answer"])

        # Display sources, if available
        sources = result.get("sources", "")
        if sources:
            st.subheader("Sources:")
            sources_list = sources.split("\n")  # Split the sources by newline
            for source in sources_list:
                st.write(source)