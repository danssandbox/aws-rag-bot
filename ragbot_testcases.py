import unittest
from rag_chatbot import RagChatbot, LlmModelTypes

domain_name = "rise-gardens-kb-v2"
question = "what is the Answer to the Ultimate Question of Life, the Universe, and Everything"

class TestRagbot(unittest.TestCase):
    def test_bedrock_titan(self):
        chatbot = RagChatbot(domain_name, LlmModelTypes.BEDROCK_TITAN_EXPRESS)
        llm = chatbot.get_llm_model()
        meaning_of_life = llm.invoke(question)
        print(meaning_of_life)
        self.assertIn("42", meaning_of_life)


    def test_bedrock_llama2(self):
        chatbot = RagChatbot(domain_name, LlmModelTypes.BEDROCK_LLAMA2)
        llm = chatbot.get_llm_model()
        meaning_of_life = llm.invoke(question)
        print(meaning_of_life)
        self.assertIn("42", meaning_of_life)

    def test_bedrock_jurassic(self):
        chatbot = RagChatbot(domain_name, LlmModelTypes.BEDROCK_JURRASIC2_ULTRA)
        llm = chatbot.get_llm_model()
        meaning_of_life = llm.invoke(question)
        print(meaning_of_life)
        self.assertIn("42", meaning_of_life)


    def test_openai_gpt4(self):
        chatbot = RagChatbot(domain_name, LlmModelTypes.OPENAI_GPT4)
        llm = chatbot.get_llm_model()
        meaning_of_life = llm.invoke(question)
        print(meaning_of_life.content)
        self.assertIn("42", meaning_of_life.content)

    def test_openai_gpt3(self):
        chatbot = RagChatbot(domain_name, LlmModelTypes.OPENAI_GPT35)
        llm = chatbot.get_llm_model()
        meaning_of_life = llm.invoke(question)
        print(meaning_of_life.content)
        self.assertIn("42", meaning_of_life.content)

    def test_google_gemini_pro(self):
        chatbot = RagChatbot(domain_name, LlmModelTypes.GOOGLE_GEMINI_PRO)
        llm = chatbot.get_llm_model()
        meaning_of_life = llm.invoke(question)
        print(meaning_of_life.content)
        self.assertIn("42", meaning_of_life.content)

