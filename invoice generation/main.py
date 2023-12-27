import pandas as pd
import glob
from fpdf import FPDF 
from pathlib import Path 

filepaths = glob.glob('./invoices/*.xlsx')

for filepath in filepaths:
    filename = Path(filepath).stem
    invoice_num, date = filename.split('-')

    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Invoice nr.{invoice_num}', ln=1)
    pdf.cell(w=50, h=8, txt=f'Date {date}', ln=1)
    
    df = pd.read_excel(filepath, sheet_name='Sheet 1')

    pdf.set_font(family='Times', size=12, style='B')
    pdf.cell(w=35, h=8, txt='Product ID', border=1)
    pdf.cell(w=60, h=8, txt='Product Name', border=1)
    pdf.cell(w=30, h=8, txt='Amount', border=1)
    pdf.cell(w=30, h=8, txt='Price per Unit', border=1)
    pdf.cell(w=30, h=8, txt='Total Price', border=1, ln=1)

    pdf.set_font(family='Times', size=10)
    pdf.set_text_color(80, 80, 80)

    sum = 0
    for index, row in df.iterrows():
        pdf.cell(w=35, h=8, txt=f"{row['product_id']}", border=1)
        pdf.cell(w=60, h=8, txt=f"{row['product_name']}", border=1)
        pdf.cell(w=30, h=8, txt=f"{row['amount_purchased']}", border=1)
        pdf.cell(w=30, h=8, txt=f"{row['price_per_unit']}", border=1)
        pdf.cell(w=30, h=8, txt=f"{row['total_price']}", border=1, ln=1)

        sum = sum + row['total_price']

    pdf.cell(w=35, h=8, txt="", border=1)
    pdf.cell(w=60, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=f"{sum}", border=1, ln=1)


    pdf.cell(w=0, h=8, txt=f'The total due amount is {sum} Euros.')

    pdf.output(f'pdfs/{filename}.pdf')
