
# Radiobot - A Conversational AI for Radiology Enthusiasts

This repository contains a Python script (`radiobot.py`) that demonstrates the use of Hugging Face's Transformers library to create a conversational AI named **Radiobot** using the BlenderBot model (`facebook/blenderbot-400M-distill`). Radiobot is designed to maintain conversation context and handle multiple turns of dialogue, making it a helpful companion for radiology-related conversations or general chatting.

## Features

- Uses the `facebook/blenderbot-400M-distill` model for natural language understanding and generation.
- Maintains conversation history to provide contextual responses.
- Handles dynamic user inputs, allowing for an engaging chatbot experience.

## Requirements

To run Radiobot, you'll need the following Python libraries:

- `transformers`
- `torch`

You can install these dependencies using pip:

```bash
pip install transformers torch
```

## How to Use

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Ajogeorge29/radiobot.git
   cd radiobot
   ```

2. **Run the Script**:

   You can run the script directly from the command line:

   ```bash
   python radiobot.py
   ```

3. **Interact with Radiobot**:

   The script will start a simple conversation. You can continue to interact with Radiobot by entering your text input.

## Example Usage

```python
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Load the model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

# Start the conversation
user_input = "Hello, how are you?"
response = generate_response(user_input)
print("Radiobot:", response)
```

## Customization

- **Change the Model**: You can replace the BlenderBot model with any other conversational model available on Hugging Face's Model Hub by changing the `model_name` variable.
- **Modify Conversation History Handling**: Adjust how conversation history is maintained to suit more complex applications or use cases.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/transformers/) - An amazing library for state-of-the-art NLP models.
- [PyTorch](https://pytorch.org/) - The deep learning framework used for model implementation.
