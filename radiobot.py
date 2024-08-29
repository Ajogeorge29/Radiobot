
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Load the model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

# Initialize conversation history
conversation_history = []

# Function to generate a response from the Radiobot model
def generate_response(user_input):
    """
    Generate a response from the Radiobot model based on user input and conversation history.

    Args:
        user_input (str): The user's input to Radiobot.

    Returns:
        str: Radiobot's response.
    """
    # Add user input to the conversation history
    conversation_history.append(user_input)
    
    # Combine all conversation history into a single string for context
    input_text = " ".join(conversation_history)

    # Tokenize the input text with truncation to avoid input size limits
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512)
    
    # Ensure valid input for the model
    if inputs['input_ids'].size(1) == 0:
        return "I'm not sure how to respond to that."
    
    # Generate a response
    reply_ids = model.generate(**inputs)
    
    # Decode the response
    response = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
    
    # Add model response to conversation history
    conversation_history.append(response)
    
    return response

def main():
    """
    Main function to run Radiobot.
    """
    print("Welcome to Radiobot! Type 'quit' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit the chat if the user types 'quit'
        if user_input.lower() == 'quit':
            print("Exiting the chat. Goodbye!")
            break
        
        # Generate and print Radiobot's response
        response = generate_response(user_input)
        print("Radiobot:", response)

if __name__ == "__main__":
    main()
