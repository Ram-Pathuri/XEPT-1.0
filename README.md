
# XEPt-1.0

Xept 1.0 is a customized language model designed to read external links and provide answers to questions. It offers advanced capabilities tailored to user needs. With Xept 1.0, accessing information and obtaining accurate responses is streamlined and efficient. It represents a significant advancement in natural language processing technology.

## Screenshots

![App Screenshot](https://github.com/Ram-Pathuri/XEPT-1.0/blob/main/xept-1.0.png)


## Installation

1.Clone this repository to your local machine using:
```bash
 git clone https://github.com/Ram-Pathuri/XEPT-1.0.git
```

2.Install the required dependencies using pip:
  

```bash
 pip install -r requirements.txt
```
    
3.Set up your OpenAI API key by creating a .env file in the project root and adding your API

  
  ```bash
OPENAI_API_KEY=your_api_key_here
```
  4.Run the project

  
  ```bash
streamlit run main.py
```



## Project Structure

- main.py: The main Streamlit application script.
- requirements.txt: A list of required Python packages for the project.
- faiss_store_openai.pkl: A pickle file to store the FAISS index.
- env: Configuration file for storing your OpenAI API key.
## Note

The index out of range error occurs due to  the langchain version,so choose the appropriate version.
- happy coding -ram



