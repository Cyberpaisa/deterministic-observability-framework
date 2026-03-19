import pandas as pd
import os
import logging
from typing import Dict, Any
from docx import Document

logger = logging.getLogger("enigma.data_analyst")

class EnigmaDataAnalyst:
    """
    Experto en análisis de datos, cruce de bases de datos y procesamiento de Excel/CSV/Word.
    """
    def __init__(self):
        self.output_dir = "output/data_analysis"
        os.makedirs(self.output_dir, exist_ok=True)

    def analyze_file(self, file_path: str) -> str:
        """Analiza un archivo y devuelve un resumen técnico."""
        ext = os.path.splitext(file_path)[1].lower()
        
        try:
            if ext == '.csv':
                df = pd.read_csv(file_path)
                return self._format_dataframe_summary(df, file_path)
            elif ext in ['.xlsx', '.xls']:
                df = pd.read_excel(file_path)
                return self._format_dataframe_summary(df, file_path)
            elif ext == '.xlsb':
                df = pd.read_excel(file_path, engine='pyxlsb')
                return self._format_dataframe_summary(df, file_path)
            elif ext == '.docx':
                return self._analyze_word(file_path)
            else:
                return f"⚠️ Formato {ext} no soportado para análisis directo."

        except Exception as e:
            logger.error(f"Error analizando archivo: {e}")
            return f"❌ Error al procesar el archivo: {str(e)}"

    def _format_dataframe_summary(self, df: pd.DataFrame, file_path: str) -> str:
        rows, cols = df.shape
        summary = f"📊 *Análisis de Datos: {os.path.basename(file_path)}*\n"
        summary += f"- Filas: {rows}\n- Columnas: {cols}\n"
        summary += f"- Columnas detectadas: {', '.join(df.columns[:10])}{'...' if cols > 10 else ''}\n"
        summary += f"\n*Resumen Estadístico (Numérico):*\n`{df.describe().to_string()}`\n"
        summary += f"\n*Primeras 5 líneas:*\n`{df.head().to_string()}`"
        return summary

    def _analyze_word(self, file_path: str) -> str:
        doc = Document(file_path)
        text = [p.text for p in doc.paragraphs if p.text.strip()]
        paragraphs_count = len(text)
        word_count = sum(len(p.split()) for p in text)
        
        summary = f"📄 *Análisis de Documento (Word): {os.path.basename(file_path)}*\n"
        summary += f"- Párrafos con texto: {paragraphs_count}\n"
        summary += f"- Palabras estimadas: {word_count}\n"
        summary += f"\n*Extracto del inicio:*\n{ ' '.join(text[:3])[:500]}..."
        return summary

if __name__ == "__main__":
    analyst = EnigmaDataAnalyst()
