OpenAI API Text-Summarization

Document Summarizer

This repository contains a Python script that utilizes OpenAI's GPT model to summarize the content of a text document. The script reads a document from a file, sends its content to the OpenAI API, and returns a concise summary of the text.

Features
Read Document: The script reads the content of a text document.
Summarize Document: Uses OpenAI's GPT-3.5 model to generate a summary of the content.
Flexible Input: You can specify the path to your document.
Customizable Settings: You can adjust the model, token limits, and temperature for summarization.
Requirements
To run this script, you will need:

Python 3.6+
OpenAI Python library
An OpenAI API key
Install Dependencies
Clone the repository:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Install the required dependencies:

pip install openai
Get Your OpenAI API Key
You need an OpenAI API key to use the model. You can obtain it by signing up on OpenAI's website. Once you have your API key, replace the placeholder your-api-key with your actual API key in the script.

Usage
Place your document: Save the text document you want to summarize in the same directory as the script, or specify the full path.

Run the script:

python document_summarizer.py
The script will read the document, summarize its content, and print the summary to the terminal.

Get Your OpenAI API Key
You need an OpenAI API key to use the model. You can obtain it by signing up on OpenAI's website. Once you have your API key, replace the placeholder your-api-key with your actual API key in the script.

Python Code
Below is the Python code for the document summarizer:

import openai

# Set your OpenAI API key
openai.api_key = "api_key"

def read_document(file_path):
    """
    Reads the content of a document.
    
    Parameters:
        file_path (str): Path to the document file.
        
    Returns:
        str: Content of the document.
    """
    try:
        with open(file_path, "r") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None

def summarize_document(content, model="gpt-3.5-turbo", max_tokens=300, temperature=0.5):
    """
    Summarizes the content of a document using OpenAI API.
    
    Parameters:
        content (str): Content to summarize.
        model (str): GPT model to use (default: gpt-3.5-turbo).
        max_tokens (int): Maximum tokens for the summary.
        temperature (float): Sampling temperature for response creativity.
        
    Returns:
        str: Summary of the content.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,  # Specify the chat model here
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": f"Summarize the following text: {content}"}],
            max_tokens=max_tokens,
            temperature=temperature
        )
        
        # Extract the summary from the response
        summary = response['choices'][0]['message']['content'].strip()
        return summary
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Specify the path to the document file
    document_path = "text_summarize.txt"  # Replace with your file path
    
    # Read the document
    document_content = read_document(document_path)
    
    if document_content:
        print("Summarizing the document...")
        # Summarize the document
        summary = summarize_document(document_content)
        print("\nSummary:")
        print(summary)
    else:
        print("Failed to read the document. Please check the file path.")
        
Example Input

Artificial Intelligence (AI) refers to the field of computer science dedicated to building systems capable of performing tasks that would typically require human intelligence. These tasks include reasoning, learning, problem-solving, perception, and language understanding.AI encompasses various subfields like machine learning (ML), where systems learn from data to improve performance over time, and deep learning, a subset of ML that uses neural networks to model complex patterns. AI is used in a wide range of applications, from virtual assistants and autonomous vehicles to medical diagnostics and robotics.The potential of AI is vast, revolutionizing industries such as healthcare, finance, and manufacturing. However, AI also raises concerns around ethics, job displacement, and privacy, prompting ongoing discussions about its responsible development and use.

Example Output

Summarizing the document...

Summary: Artificial Intelligence (AI) is a computer science field focused on creating systems that can perform tasks requiring human intelligence, such as reasoning and problem-solving. It includes subfields like machine learning and deep learning, which enable systems to learn and improve over time. AI is utilized in various applications like virtual assistants and medical diagnostics, with the potential to transform industries. However, ethical, job-related, and privacy concerns have sparked discussions about the responsible development and use of AI.
