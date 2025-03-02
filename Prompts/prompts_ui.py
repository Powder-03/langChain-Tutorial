from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st 
from langchain_core.prompts import PromptTemplate

load_dotenv()
model= ChatGoogleGenerativeAI(model = 'gemini-1.5-pro' , temperature=0.1)

st.header('Reasearch Tool')
paper_input = st.selectbox("Select Research paper name", ["Select...", "Attention is all you need " , "BERT :Pre-training of deeo birectional transformer" , "GPT-3: Language models are Few-shot learners","Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select explanation style", ["Beginner-Friendly" , "Technical","Code-Oriented","Mathematical"])

length_input = st.selectbox("Select explanation length", ["Short (1-2 paragraphs)" , "Medium(3-5 paragraphs)" , "Long (detailed explanation)"])


#TEMPLATE
template = PromptTemplate(
    template = """Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.""", 

    input_variables = ['paper_input' , 'style_input ', 'length_input']
)     

#FILL THE PLACEHOLDERS                     

prompt = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})



if st.button('Summarise'):
    result = model.invoke(prompt)
    st.write(result.content)
    
#static prompts jab user ko full control ho prompt pr=e mtlb poora prompt whi likhe
#dyanmic prompt jab phle se set ho kaphi prompt ki ans kse dena h bs aapse thode input lelo
 