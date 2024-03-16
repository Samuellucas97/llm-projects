from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI


from dotenv import load_dotenv
from os import environ, getcwd

load_dotenv(f'{getcwd()}/.env')

OPENAPI_API_KEY = environ.get("OPENAPI_API_KEY", "")
CREATIVITY=0


chat = ChatOpenAI(temperature=CREATIVITY,openai_api_key=OPENAPI_API_KEY)


def ask_to_wheather_expert(wheather_question, context=""):
    messages = [ 
        SystemMessage(
            content="Voce precisa atuar como um expert em previsão do tempo."
        ),
        HumanMessage(
            content=f'{wheather_question}. Considere as seguintes informações: {context}'
        ),
    ]
    return chat(messages)
    

def load_doc(file):
    from langchain.document_loaders import PyPDFLoader
    loader=PyPDFLoader(file)
    pages  = loader.load_and_split()
    # print("pages",pages)
    return loader.load()

pdf_paper='https://arxiv.org/pdf/2210.07342.pdf'
pages=load_doc(pdf_paper)
for page in pages:
    print(page)



wheather_question='Qual é a temperatura em Natal, no Rio Grande do Norte?'
ask_to_wheather_expert(wheather_question)