# Python program to create
# a pdf file
# Reference: https://pyfpdf.readthedocs.io/en/latest/ReferenceManual/index.html


from fpdf import FPDF
import pandas as pd

#variables
pdf = FPDF(orientation = 'L', unit = 'mm', format=(206,298))
x_name = 45 # 45 is the best
y_name = 115 # 115 is the best
x_date = 197 # 200 195 197
y_date = 160 # 155 is the best
x_teacher1 = 247
y_teacher1 = 155
x_teacher2 = 247
y_teacher2 = 182
show_border = 0

#Reading csv
df = pd.read_csv("data.csv")
studentList = df["name of student"]
dateList = df["date"]



for i in range(len(studentList)):
	student = studentList[i]
	date = dateList[i]

	pdf.add_page()
	pdf.set_text_color(255.0, 0.0, 0.0)
	pdf.set_font("Helvetica", size = 35, style='B')

	pdf.set_xy(x_name, y_name)
	pdf.cell(200, 10, txt = student,ln = 1, align = 'L', border = show_border)

	# Set Date
	pdf.set_font("Helvetica", size = 12)
	pdf.set_xy(x_date, y_date)
	pdf.cell(36, 5, txt = date, ln = 1, align = 'C', border = show_border)


# save the pdf with name .pdf
pdf.output("output.pdf")
