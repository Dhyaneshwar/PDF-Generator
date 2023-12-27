from fpdf import FPDF
import pandas as pd

pdf = FPDF()

# setting the margin to 0 because when we perform line break for footer, we try to go to the end of the page.
# By doing it we are over the margin. Since by default when the line is on margin, the page break will be triggered.
# In order to avoid it, we are setting it to false and the margin value as 0.
pdf.set_auto_page_break(auto=False, margin=0)

ds = pd.read_csv('topics.csv')

# Function to display the Header
def display_header(value):
    pdf.set_font('Arial', 'B', 14)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(w=0, h=5, txt=value, ln=1, align='L')

# Function to draw lines on the page
def draw_lines(start_point):
    for i in range(start_point, 286, 5):
        pdf.line(10,i,202,i)

# Function to print the Topic at the footer is declared here.
def add_pdf_footer(lineBreak, value):
    pdf.ln(lineBreak)
    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=5, txt=value, ln=1, align='R')

for index, row in ds.iterrows():
    topic = row['Topic']

    pdf.add_page()
    display_header(topic)    
    add_pdf_footer(272, topic)
    draw_lines(15)
    
    for i in range(row['Pages']-1):
        pdf.add_page()
        add_pdf_footer(276, topic)
        draw_lines(5)

pdf.output('output.pdf')