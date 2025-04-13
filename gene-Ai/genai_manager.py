import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Used to securely store your API key
from google.colab import userdata

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')

genai.configure(api_key="AIzaSyCCgQVLdh_CT31bkQjafP0L7Tx4Xkr1jaUXY")

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

    model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("What is the meaning of life?")
to_markdown(response.text)
