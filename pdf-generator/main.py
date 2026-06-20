from fastapi import FastAPI
from fastapi.responses import FileResponse
from fpdf import FPDF
import requests

app = FastAPI()

@app.get("/api/pdf")
def generate_pdf():
    # 1. Récupération des données API en interne
    response = requests.get("http://api:8000/api/cv")
    data = response.json()

    # 2. Configuration du PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # --- EN-TÊTE ---
    pdf.set_font("helvetica", "B", 22)
    pdf.cell(0, 10, data["basics"]["name"], new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.set_font("helvetica", "I", 12)
    pdf.cell(0, 8, data["basics"]["title"], new_x="LMARGIN", new_y="NEXT", align="C")

    