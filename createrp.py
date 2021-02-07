from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.platypus.flowables import Image
import datetime

PAGE_HEIGHT = defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()
Title = "Stocks Report"
now = datetime.datetime.now()
Date = now.strftime("%d/%m/%Y %H:%M")
pageinfo = "Lucifer CORP Enterprises"
style = getSampleStyleSheet()
yourStyle = ParagraphStyle('yourtitle',
                           fontName="Helvetica-Bold",
                           fontSize=16,
                           parent=style['Heading2'],
                           alignment=1,
                           spaceAfter=14)


def myFirstPage(canvas, doc):
	canvas.saveState()
	canvas.setFont('Helvetica-Bold',20)
	canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
	canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-130, Date)
	im = Image("lucicoin.png", width=2*inch, height=2*inch)
	im.hAlign = 'LEFT'
	canvas.setFont('Helvetica',9)
	canvas.drawString(inch, 0.75 * inch, "First Page / %s" % pageinfo)
	canvas.restoreState()

def myLaterPages(canvas, doc):
	canvas.saveState()
	canvas.setFont('Times-Roman',9)
	canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, pageinfo))
	canvas.restoreState()


def createpdf(stockslist, total):
	doc = SimpleDocTemplate("phello.pdf")
	Story = [Spacer(1,2*inch)]
	style = styles["Normal"]
	for i in stockslist:
		p = Paragraph(i, style)
		Story.append(p)
		Story.append(Spacer(1,0.2*inch))
	p = Paragraph('TOTAL: ' + total + ' USD', yourStyle)
	Story.append(p)
	doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)
	



