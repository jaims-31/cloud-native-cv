from fastapi import FastAPI
from fastapi.responses import FileResponse
from fpdf import FPDF
import requests
import os

app = FastAPI()


@app.get("/api/pdf")
def generate_pdf():
    # 1. Récupération des données API en interne
    api_url = os.getenv("API_URL", "http://cv-api-service")
    response = requests.get(f"{api_url}/api/cv")
    data = response.json()

    # 2. Configuration du PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # --- EN-TÊTE ---
    pdf.set_font("helvetica", "B", 22)
    pdf.cell(
        0, 10, data["basics"]["name"],
        new_x="LMARGIN", new_y="NEXT", align="C"
    )
    pdf.set_font("helvetica", "I", 12)
    pdf.cell(
        0, 8, data["basics"]["title"],
        new_x="LMARGIN", new_y="NEXT", align="C"
    )

    # Contacts
    pdf.set_font("helvetica", "", 10)
    contact_info = (
        f"{data['basics']['location']}  |  "
        f"{data['basics']['phone']}  |  "
        f"{data['basics']['email']}"
    )
    pdf.cell(0, 8, contact_info, new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(5)

    # --- PROFIL ---
    pdf.set_font("helvetica", "B", 12)
    pdf.cell(0, 8, "PROFIL", new_x="LMARGIN", new_y="NEXT", border="B")
    pdf.set_font("helvetica", "", 10)
    pdf.multi_cell(0, 6, data["basics"]["summary"])
    pdf.ln(5)

    # --- COMPÉTENCES ---
    pdf.set_font("helvetica", "B", 12)
    pdf.cell(0, 8, "COMPÉTENCES", new_x="LMARGIN", new_y="NEXT", border="B")
    for category, skills in data["skills"].items():
        pdf.set_font("helvetica", "B", 10)
        pdf.cell(0, 6, category + " :", new_x="LMARGIN", new_y="NEXT") 
        pdf.multi_cell(0, 6, skills, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(2)
    pdf.ln(5)

    # --- PROJETS ---
    pdf.set_font("helvetica", "B", 12)
    pdf.cell(
        0, 8, "PROJET CLOUD & DEVOPS",
        new_x="LMARGIN", new_y="NEXT", border="B"
    )
    for proj in data["projects"]:
        pdf.set_font("helvetica", "B", 10)
        pdf.cell(0, 6, proj["title"], new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("helvetica", "", 10)
        pdf.multi_cell(0, 6, proj["description"])

    # 3. Sauvegarde et envoi
    pdf.output("cv_export.pdf")
    return FileResponse(
        "cv_export.pdf",
        media_type="application/pdf",
        filename="CV_Franck_Barry.pdf"
    )
