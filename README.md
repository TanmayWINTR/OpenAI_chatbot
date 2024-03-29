
# OpenAI_chatbot

This project provides a template for creating a chatbot using OpenAI's GPT model and Gradio. It's designed to be a user-friendly interface for real estate investment and negotiation advice, but can be customized for various other applications. Users can interact with a GPT-powered chatbot, receiving insights and responses to a wide range of queries.

## Getting Started

These instructions will guide you through setting up and running your own instance of the chatbot on your local machine.

### Prerequisites

Ensure that you have Python installed on your system. This application requires Python 3.6 or later.

### Installation

1. **Install OpenAI Package**

   Install the OpenAI Python package, necessary for interacting with the OpenAI API:

   ```bash
   pip install openai==0.28.1
   ```

2. **Install Gradio**

   Install Gradio, which is used to create the web interface for the chatbot:

   ```bash
   pip install gradio
   ```
### Additional Setup: OpenAI Account and API Key Creation
Before using the chatbot, an OpenAI account and an API key are required.

Creating an OpenAI Account
1. Visit the OpenAI website and sign up.
2. Verify your account via the link sent to your email.

Generating an API Key
1. Log into your OpenAI account.
2. Navigate to the 'API' section and generate a new API key.
3. Securely store the generated API key.

### Configuration

- **API Key**: An OpenAI API key is required. Replace `'your-api-key'` in the code with your actual OpenAI API key.
- **Customizing the Chatbot Role**: Customize the chatbot's role and expertise by modifying the `messages` variable. This allows you to tailor the chatbot for different use cases.

  Example:
  ```python
  messages = [{"role": "system", "content": "You are a financial expert specializing in real estate investment and negotiation. You answer the financial questions in less than 20 words."}]
  ```

### Running the Application

1. **Start the Application**

   Run the Python script containing the chatbot code.

2. **Access the Interface**

   A URL will be displayed in the terminal. Click on this URL to open the Gradio interface in your web browser.

3. **Interact with the Chatbot**

   Begin interacting with the chatbot by typing in your queries.

## Interface Screenshots

Here is a screenshot of the Chatbot interface:

![Chatbot Interface](chatbot.png)

## Customization and Usage

Feel free to customize and use this template for building your own chatbots. Whether you're looking to create an educational tool, a customer service assistant, or a personal project, this code serves as a versatile starting point.

## Support

For any queries or issues, feel free to open an issue in this repository.

