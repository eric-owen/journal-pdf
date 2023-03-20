from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv('data.csv')

page_num = 1

for i, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=0, h=12, txt=row['Day'], align="L",
             ln=0)
    pdf.cell(w=0, h=12, txt=str(page_num), align="R",
             ln=1)
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)
    pdf.line(10, 21, 200, 21)

    for i in range(row['Pages'] - 1):
        page_num += 1
        pdf.add_page()
        pdf.cell(w=0, h=12, txt=str(page_num), align="R",
                 ln=1)
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)
        page_num += 1


pdf.output('output.pdf')
