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
