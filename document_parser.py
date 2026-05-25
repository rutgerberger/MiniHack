import os
from pypdf import PdfReader

def extract_text_from_pdf(file_path):
    """Extracts text from a single PDF file."""
    text = ""
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    except Exception as e:
        print(f"Error reading PDF {file_path}: {e}")
    return text

def extract_text_from_txt(file_path):
    """Extracts text from a standard text or markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading TXT {file_path}: {e}")
        return ""

def load_course_materials(base_dir="CourseMaterial"):
    """
    Recursively scans the directory and parses supported file types.
    Returns a dictionary: { "filename": "extracted_text" }
    """
    documents = {}
    
    # Walk through the directory tree
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Handle PDFs (e.g., LectureSlides)
            if file.endswith('.pdf'):
                print(f"Parsing: {file}...")
                documents[file] = extract_text_from_pdf(file_path)
                
            # Handle Markdown and Text (e.g., READMEs, clean notes)
            elif file.endswith(('.md', '.txt', '.csv')):
                print(f"Parsing: {file}...")
                documents[file] = extract_text_from_txt(file_path)
                
            # [YOUR EXTENSION HERE] 
            
    return documents

def chunk_text(text, chunk_size=1000):
    """
    A basic utility to split large texts into smaller chunks for the agent.
    You can upgrade this!
    """
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]