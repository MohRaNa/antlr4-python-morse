from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from antlr4 import *
from MorseLexer import MorseLexer
from MorseParser import MorseParser

# Mapeo de letras y dígitos al código Morse
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

def text_to_morse(text):
    return ' '.join(morse_dict[char] for char in text.upper() if char in morse_dict)

# Función para recorrer el árbol y extraer los valores
def extract_morse_code(tree, parser):
    if tree.getChildCount() == 0:
        return tree.getText()
    result = []
    for i in range(tree.getChildCount()):
        child = tree.getChild(i)
        result.append(extract_morse_code(child, parser))
    return ' '.join(result)

# Configuración de CORS
origins = ["*"]
app = FastAPI(title='Morse Code API')
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Modelos de datos
class InputData(BaseModel):
    text: str

class OutputData(BaseModel):
    result: str

# Endpoint para traducir texto al código Morse
@app.post('/translate', response_model=OutputData)
def translate(data: InputData):
    input_text = text_to_morse(data.text)
    lexer = MorseLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    parser = MorseParser(stream)
    tree = parser.morse_code()
    
    result = extract_morse_code(tree, parser)
    return {'result': result}
