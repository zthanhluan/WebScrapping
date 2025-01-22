from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2:latest")

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parseDescription}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

def parseUsingOllama (domChunks , parseDescription) :
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    finalResult = []
    for counter , chunk in enumerate (domChunks , start=1) :
        result = chain.invoke(
                                {"dom_content": chunk , "parseDescription": parseDescription}
                              )
        print(f"Parsed Batch {counter} of {len(domChunks)}")
        finalResult.append(result)
    return "\n".join(finalResult)