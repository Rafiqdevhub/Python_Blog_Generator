# Blog Generation App

A Streamlit-based application that generates blog posts using the Llama 2 language model. The application allows users to generate customized blog content based on their specified topic, target audience, and desired word count.

## Features

- Generate blog posts using Llama 2 AI model
- Customize blog content for different audiences (Researchers, Data Scientists, Common People)
- Specify desired word count
- Real-time word count display
- User-friendly interface built with Streamlit

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Blog_Generation_App.git
cd Blog_Generation_App
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run main.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Enter your blog topic, desired word count, and select your target audience

4. Click "Generate" to create your blog post

## How It Works

The application uses:
- Streamlit for the web interface
- Llama 2 model (via CTransformers) for text generation
- LangChain for prompt templating and model interaction
- HuggingFace Hub for model downloading

## Project Structure

```
Blog_Generation_App/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── LICENSE             # MIT License file
└── README.md           # Project documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.