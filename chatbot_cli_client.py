import argparse
from colorama import Fore, Back, Style
from rag_chatbot import RagChatbot, LlmModelTypes
from prompt_library import DefaultPrompts, NasaSpokespersonPrompts
from langchain_core.messages import AIMessage, HumanMessage

# TODO:
#  add color to the input/output text so it is easier to read
#  add command line options and use domain
#  add a total model run summary at the end of the conversation - cost, tokens, etc.

parser = argparse.ArgumentParser(description='Chatbot CLI Client')
parser.add_argument('domain_name', type=str, help='The domain name for the chatbot')
args = parser.parse_args()

domain_name = args.domain_name
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

    # This part keeps track of the conversation history
    if type(response) == AIMessage:
        chat_history.extend([HumanMessage(content=human_input), response])
    else:  # This is needed because some LLM's will return a string instead of a AIMessage
        chat_history.extend([HumanMessage(content=human_input), AIMessage(content=response)])
    print(Fore.BLUE + response + Style.RESET_ALL)
    print()

