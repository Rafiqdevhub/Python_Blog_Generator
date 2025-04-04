import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from huggingface_hub import hf_hub_download

def download_model():
    model_path = hf_hub_download(
        repo_id="TheBloke/Llama-2-7B-Chat-GGML",
        filename="llama-2-7b-chat.ggmlv3.q8_0.bin",
        revision="main"
    )
    return model_path

def getLLamaresponse(input_text, no_words, blog_style):
    try:
        # Download and get model path
        model_path = download_model()
        
        # LLama2 model initialization
        llm = CTransformers(
            model=model_path,
            model_type='llama',
            config={
                'max_new_tokens': 256,
                'temperature': 0.01
            }
        )
        
        # Prompt Template
        template = """
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
        """
        
        prompt = PromptTemplate(
            input_variables=["blog_style", "input_text", 'no_words'],
            template=template
        )
        
        # Generate the response from the LLama 2 model
        response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
        return response
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit UI Configuration
st.set_page_config(
    page_title="Generate Blogs",
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.header("Generate Blogs 🤖")

# User Input Section
input_text = st.text_input("Enter the Blog Topic")

# Creating two columns for additional fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox(
        'Writing the blog for',
        ('Researchers', 'Data Scientist', 'Common People'),
        index=0
    )

submit = st.button("Generate")

# Generate and display the blog
if submit:
    if not input_text:
        st.warning("Please enter a blog topic!")
    elif not no_words:
        st.warning("Please specify the number of words!")
    else:
        with st.spinner("Generating your blog... Please wait."):
            response = getLLamaresponse(input_text, no_words, blog_style)
            st.write(response)
            
            # Display word count
            word_count = len(response.split())
            st.info(f"Generated blog word count: {word_count}")