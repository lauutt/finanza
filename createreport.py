from fpdf import FPDF
import datetime

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('lucicoin.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(100, 10, 'Resume from Lucicoin', 1, 0, 'C')
        # Line break
        self.ln(40)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')	


def createpdf(stockslist):
	now = datetime.datetime.now()
	dt_string = now.strftime("%d%m%Y %H%M")
	pdf = PDF()
	pdf.alias_nb_pages()
	pdf.add_page()
	pdf.set_font('Times', '', 12)
	pdf.cell(0, 10, 'Resumen creado en: '+str(now), 0, 1)
	for i in stockslist:
	    pdf.cell(0, 10, i , 0, 1)
	pdf.output('hola.pdf', 'F')