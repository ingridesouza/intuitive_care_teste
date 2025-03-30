import os
import zipfile
import pandas as pd
import tabula
import logging
from typing import List, Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PDFProcessor:
    """Classe para processamento de PDFs de procedimentos"""
    
    def __init__(self):
        self.config = {
            'java_path': r"C:\Program Files\Java\jdk-24",
            'pdf_path': "doc/Anexo_I.pdf",
            'pages': "3-181"
        }
        
    def setup_environment(self):
        """Configura ambiente Java"""
        os.environ["JAVA_HOME"] = self.config['java_path']
        os.environ["PATH"] = f"{self.config['java_path']}\\bin;{os.environ['PATH']}"
        
    def extract_tables(self) -> List[pd.DataFrame]:
        """Extrai tabelas do PDF"""
        logger.info("Iniciando extração de tabelas...")
        return tabula.read_pdf(
            self.config['pdf_path'],
            pages=self.config['pages'],
            multiple_tables=True,
            lattice=True,
            pandas_options={'header': None}
        )
    
    def process_data(self, tables: List[pd.DataFrame]) -> pd.DataFrame:
        """Processa e limpa os dados"""
        logger.info("Processando dados...")
        df = pd.concat(tables, ignore_index=True)
        
        df.columns = [
            "PROCEDIMENTO", "RN (alteração)", "VIGÊNCIA", "OD", "AMB", 
            "HCO", "HSO", "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"
        ]
        
        df = df[~df['PROCEDIMENTO'].str.contains('PROCEDIMENTO', na=False)]
        df = df.drop_duplicates()
        
        replacements = {
            "OD": "Odontológico", "AMB": "Ambulatorial",
            "HCO": "Hospitalar com Ocupação", "HSO": "Hospitalar sem Ocupação",
            "REF": "Referência", "PAC": "Paciente", 
            "DUT": "Diretriz de Utilização"
        }
        
        df = df.replace(replacements)
        df = df.replace(r'\n', ' ', regex=True)
        df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        
        return df

def main():
    processor = PDFProcessor()
    
    try:
        processor.setup_environment()
        tables = processor.extract_tables()
        df_final = processor.process_data(tables)
        
        csv_filename = "rol_de_procedimentos.csv"
        df_final.to_csv(csv_filename, index=False, encoding="utf-8", quoting=csv.QUOTE_ALL)
        
        with zipfile.ZipFile("Teste_ingride.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(csv_filename)
            
        logger.info("Processo concluído com sucesso!")
        
    except Exception as e:
        logger.error(f"Erro durante a execução: {str(e)}")
        raise

if __name__ == "__main__":
    import csv
    main()