import pandas as pd
from fpdf import FPDF
from datetime import datetime
from .database import get_connection
from pathlib import Path

REPORTS_PATH = Path("reports")
REPORTS_PATH.mkdir(exist_ok=True)

def export_to_excel():
    with get_connection() as conn:
        df = pd.read_sql_query("""
        SELECT o.id, c.name AS client, o.description, o.status, o.cost, o.date_created
        FROM orders o
        LEFT JOIN clients c ON o.client_id = c.id
        ORDER BY o.date_created DESC
        """, conn)

    file_name = REPORTS_PATH / f"report_{datetime.now():%Y%m%d_%H%M%S}.xlsx"
    df.to_excel(file_name, index=False)
    print(f"✅ Отчёт сохранён: {file_name}")

def export_to_pdf():
    with get_connection() as conn:
        rows = conn.execute("""
        SELECT o.id, c.name, o.description, o.status, o.cost
        FROM orders o
        LEFT JOIN clients c ON o.client_id = c.id
        ORDER BY o.date_created DESC
        LIMIT 50
        """).fetchall()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Отчёт по заказам", ln=True, align="C")

    for row in rows:
        pdf.cell(200, 8, txt=f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}₽", ln=True)

    file_name = REPORTS_PATH / f"report_{datetime.now():%Y%m%d_%H%M%S}.pdf"
    pdf.output(file_name)
    print(f"✅ PDF сохранён: {file_name}")
