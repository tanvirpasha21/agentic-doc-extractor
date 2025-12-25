from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title
pdf.cell(200, 10, txt="Sample Invoice", ln=True, align="C")

# Company info
pdf.ln(10)
pdf.cell(200, 10, txt="Company: OpenAI Test Corp", ln=True)
pdf.cell(200, 10, txt="Invoice Number: 12345", ln=True)
pdf.cell(200, 10, txt="Date: 2025-12-25", ln=True)

# Table header
pdf.ln(10)
pdf.cell(60, 10, txt="Item", border=1)
pdf.cell(40, 10, txt="Quantity", border=1)
pdf.cell(50, 10, txt="Unit Price", border=1)
pdf.cell(40, 10, txt="Total", border=1)
pdf.ln()

# Table row
pdf.cell(60, 10, txt="Widget A", border=1)
pdf.cell(40, 10, txt="2", border=1)
pdf.cell(50, 10, txt="£10", border=1)
pdf.cell(40, 10, txt="£20", border=1)
pdf.ln()

pdf.cell(60, 10, txt="Widget B", border=1)
pdf.cell(40, 10, txt="1", border=1)
pdf.cell(50, 10, txt="£15", border=1)
pdf.cell(40, 10, txt="£15", border=1)
pdf.ln()

# Total
pdf.ln(5)
pdf.cell(200, 10, txt="Total Amount: £35", ln=True, align="R")

# Save PDF
pdf.output("sample.pdf")

print("sample.pdf generated successfully!")
