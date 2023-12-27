from fpdf import FPDF
from glob import glob
from pathlib import Path

pdf = FPDF()
filepaths = glob('./Notes/*.txt')
print(filepaths)

for filepath in filepaths:
    filename= Path(filepath).stem
    
    with open(filepath) as file:
        content = file.read()

    pdf.add_page()
    pdf.set_font(family='Times', size=18, style='B')
    pdf.cell(w=0, h=10, txt=f'{filename.title()}', ln=1)

    pdf.set_font(family='Times', size=12)
    pdf.multi_cell(w=0, h=6, txt=content)


pdf.output('output.pdf')