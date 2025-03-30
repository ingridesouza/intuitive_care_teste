from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv("backend/Relatorio_cadop.csv", sep=";", encoding="utf-8")

df.columns = df.columns.str.strip().str.lower()

@app.get("/buscar")
def buscar_operadoras(termo: str = Query(..., min_length=2)):
    resultados = df[
        df["razao_social"].str.contains(termo, case=False, na=False) |
        df["nome_fantasia"].str.contains(termo, case=False, na=False)
    ].head(10)

    # Remove valores NaN para evitar erro no JSON
    resultados = resultados.fillna("")

    return resultados.to_dict(orient="records")
