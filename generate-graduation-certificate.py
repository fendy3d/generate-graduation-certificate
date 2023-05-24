# Python program to create
# a pdf file
# Reference: https://pyfpdf.readthedocs.io/en/latest/ReferenceManual/index.html


from fpdf import FPDF
import pandas as pd

#variables
pdf = FPDF(orientation = 'L', unit = 'mm', format=(206,298))
x_name = 45 # 45 is the best
y_name = 115 # 115 is the best
x_date = 198 # 198 is the best
y_date = 155 # 155 is the best
x_teacher1 = 247
y_teacher1 = 155
x_teacher2 = 247
y_teacher2 = 182
show_border = 0

#Reading csv
df = pd.read_csv("data.csv")
studentList = df["name of student"]
dateList = df["date"]
teacher1List = df["teacher1"]
teacher2List = df["teacher2"]



for i in range(len(studentList)):
	student = studentList[i]
	date = dateList[i]
	teacher1 = teacher1List[i]
	teacher2 = teacher2List[i]

	pdf.add_page()
	pdf.set_text_color(0.0, 0.0, 0.0)
	pdf.set_font("Helvetica", size = 35, style='B')

	# Set student
	pdf.set_xy(x_name, y_name)
	pdf.cell(200, 10, txt = student,ln = 1, align = 'L', border = show_border)

	# Set Date
	pdf.set_font("Helvetica", size = 12)
	pdf.set_xy(x_date, y_date)
	pdf.cell(36, 5, txt = date, ln = 1, align = 'C', border = show_border)

	# Set teacher 1
	pdf.set_font("Helvetica", size = 12)
	pdf.set_xy(x_teacher1, y_teacher1)
	pdf.cell(36, 5, txt = teacher1, ln = 1, align = 'C', border = show_border)

	# Set teacher 2
	pdf.set_font("Helvetica", size = 12)
	pdf.set_xy(x_teacher2, y_teacher2)
	pdf.cell(36, 5, txt = teacher2, ln = 1, align = 'C', border = show_border)

	
# save the pdf with name .pdf
pdf.output("output.pdf")
