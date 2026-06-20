from fastapi import FastAPI
from fastapi.responses import FileResponse
from fpdf import FPDF
import requests

app = FastAPI()


@app.get("/api/pdf")
def generate_pdf():
    # Le générateur interroge le microservice API via le réseau interne Docker.
    response = requests.get("http://api:8000/api/cv")
    data = response.json()

    # Création du PDF
    pdf = FPDF()
    pdf.add_page()

    # Titre
    pdf.set_font("helvetica", size=20, style="B")
    pdf.cell(
        0,
        10,
        text=data["basics"]["name"],
        new_x="LMARGIN",
        new_y="NEXT",
        align="C",
    )

    # Sous-titre
    pdf.set_font("helvetica", size=14, style="I")
    pdf.cell(
        0,
        10,
        text=data["basics"]["title"],
        new_x="LMARGIN",
        new_y="NEXT",
        align='C',
    )

    pdf.ln(10)

    # Compétences
    pdf.set_font("helvetica", size=12, style="B")
    pdf.cell(0, 10, text="Mes Compétences :", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", size=12)
    for skill in data["skills"]:
        pdf.cell(0, 8, text=f"- {skill}", new_x="LMARGIN", new_y="NEXT")

    # Sauvegarde et envoi au navigateur
    pdf.output("cv_export.pdf")
    return FileResponse(
        "cv_export.pdf",
        media_type="application/pdf",
        filename="Mon_CV_Cloud_Native.pdf",
    )