from docx import Document
import sys

doc = Document('/Users/jquiceva/Archivos_Juan/hackathon_dof_agent/creacion de dof agent.docx')
for para in doc.paragraphs:
    print(para.text)
