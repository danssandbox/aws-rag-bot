import argparse
from colorama import Fore, Back, Style
from rag_chatbot import RagChatbot, LlmModelTypes
from prompt_library import DefaultPrompts, NasaSpokespersonPrompts
from langchain_core.messages import AIMessage, HumanMessage
from dotenv import find_dotenv, load_dotenv
import os

# Load the environment variables as an option
load_dotenv(find_dotenv())
default_domain_name = os.getenv('OPENSEARCH_DOMAIN', default=None)

parser = argparse.ArgumentParser(description='Chatbot CLI Client')
parser.add_argument('-d', '--domain_name', type=str, help='The domain name for the chatbot', default=default_domain_name)
args = parser.parse_args()

domain_name = args.domain_name
if not domain_name:
    print("Please provide an OpenSearch domain name for the chatbot in command line argument or in the .env file.")
    exit(1)
else:
    print(f"Using OpenSearch domain name: {domain_name}")

#domain_name = "rise-gardens-kb-v2"
chatbot = RagChatbot(domain_name,
                     LlmModelTypes.BEDROCK_TITAN_EXPRESS,
                     prompt_model=NasaSpokespersonPrompts)
chat_history = []

while True:
    human_input = input(Fore.RED + "Hello, how can I help you? (x or exit to end this conversation)\n" + Style.RESET_ALL)
    if human_input.lower() in ["exit", "quit", "bye", "goodbye", "x", "q"]:
        print()
        print("I'm out of here!")
        break
    response = chatbot.ask_question(human_input, chat_history, verbose=True)

    # Keep track of the conversation history for future questions
    chat_history.extend([HumanMessage(content=human_input), response])

    print(Fore.BLUE + response.content + Style.RESET_ALL)
    print()

#Now print out the final summary of cost and tokens
conversational_summary = chatbot.get_model_run_summary()
print("========================= Summary of the conversation =========================")
print(f"Total Input tokens:  {conversational_summary['total_input_tokens']}")
print(f"      Output tokens: {conversational_summary['total_output_tokens']}")
print(f"      Cost:          ${conversational_summary['total_cost']:.4f}")
print(f"LLM Model used:  {conversational_summary['model_name']['name']}")
print(f"Vector DB index: {conversational_summary['vector_db_index']}")


