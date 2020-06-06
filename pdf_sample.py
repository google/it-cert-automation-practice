#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate

from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet




#def generate_report(attachment, title, paragraph):
def generate_report(attachment,title, paragraph ):
    report = SimpleDocTemplate(attachment)
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles["h1"])
    report_body = Paragraph(paragraph, styles["BodyText"])
    report.build([report_title, report_body])
#generate_report('D:\\test.pdf', 'This is a test Title!','Apples <br/> 500 lbs <br/> kiwi <br/> 10 lbs<br/>')


