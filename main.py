from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv('data.csv')

for i, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=0, h=12, txt=row['Day'], align="L",
             ln=1)

pdf.output('output.pdf')