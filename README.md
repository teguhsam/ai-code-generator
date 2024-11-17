# AI Code Generator

This project provides an interface to convert Python code to optimized C++ code using OpenAI's GPT or Anthropic's Claude models. The project uses Gradio for the UI and includes functionality to execute both Python and C++ code.

## Table of Contents

- [AI Code Generator](#ai-code-generator)
  - [Table of Contents](#table-of-contents)
  - [Feature](#feature)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
    - [Clone the Repository](#clone-the-repository)
    - [Set up a Virtual Environment](#set-up-a-virtual-environment)
    - [Install Required Dependencies](#install-required-dependencies)
    - [Set Up Environment Variables](#set-up-environment-variables)
    - [Running the Application](#running-the-application)
    - [C++ Code Compilation](#c-code-compilation)
    - [Debugging/Errors](#debuggingerrors)
  - [Demo Video](#demo-video)
  - [File Structure](#file-structure)
  - [Dependencies](#dependencies)

## Feature

- Convert Python code to C++ using GPT or Claude models.
- Execute Python code in a local environment.
- Compile and run the generated C++ code using clang++.
- Provides a web-based interface to interact with the tool via Gradio.

## Prerequisites

1. Python 3.7+
2. Install the necessary Python libraries and dependencies.

## Setup

### Clone the Repository

Clone this repository to your local machine:

```
git clone https://github.com/teguhsam/ai-code-generator.git
cd ai-code-generator
```

### Set up a Virtual Environment

Create and activate a virtual environment for the project.

```
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Required Dependencies

```
pip install -r requirements.txt
```

### Set Up Environment Variables

This project requires OpenAI and Anthropic API keys. Create a .env file in the root directory of your project and add your API keys:

```
OPENAI_API_KEY=your-openai-api-key
ANTHROPIC_API_KEY=your-anthropic-api-key
```

### Running the Application

To run the application:

```
python main.py
```

This will start a Gradio interface in your browser where you can:

- Input Python code.
- Choose the model (GPT or Claude).
- Convert Python code to optimized C++.
- Run both the Python and C++ code.

### C++ Code Compilation

The project uses clang++ for compiling C++ code. Ensure clang is installed on your system:

```
brew install gcc
```

### Debugging/Errors

If you encounter any issues, ensure:

- You have valid API keys for OpenAI and Anthropic.
- The clang++ compiler is available in your system's path.
- All required Python packages are installed.
-

## Demo Video

https://github.com/user-attachments/assets/b092b775-52c6-4208-8f4d-c8bbc6161094



## File Structure

```
ai-code-generator/
│
├── main.py            # Main script to launch the Gradio UI and handle logic
├── models.py          # Model functions to interact with OpenAI and Anthropic APIs
├── optimized.cpp      # Generated C++ code (output file)
├── requirements.txt   # List of Python dependencies
├── .env               # (Optional) File for storing API keys
└── README.md          # Project documentation

```

## Dependencies

- openai: For interacting with the OpenAI API.
- anthropic: For interacting with the Anthropic API.
- gradio: For creating the web-based UI.
- python-dotenv: For loading environment variables from the .env file.
- subprocess: For running system commands to compile and execute C++ code.
- clang++: C++ compiler (must be installed separately).
