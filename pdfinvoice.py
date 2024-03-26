from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import json
import datetime


def create_invoice():
    # Read bill amounts from JSON file
    with open('bills.json', 'r') as file:
        bills = json.load(file)
    
    water_bill = bills['water_bill']  
    gas_bill = bills['gas_bill']  

    doc = SimpleDocTemplate("invoice.pdf", pagesize=letter)
    story = []
    width, height = letter

    # Define styles
    styles = getSampleStyleSheet()

    # Current Date
    today = datetime.date.today()
    invoice_date = today.strftime("%Y-%m-%d")

    # Calculate Due Date (1st of the following month)
    if today.month == 12:
        due_date = datetime.date(today.year + 1, 1, 1)
    else:
        due_date = datetime.date(today.year, today.month + 1, 1)
    due_date_str = due_date.strftime("%Y-%m-%d")

    # Add dates to the invoice
    story.append(Paragraph(f"Invoice Date: {invoice_date}", styles["Normal"]))
    story.append(Paragraph(f"Due Date: {due_date_str}", styles["Normal"]))
    story.append(Spacer(1, 12))    
    # Add logo
    logo_path = 'POHlogo.png'  # Make sure the file name matches
    logo = Image(logo_path, width=75, height=75)
    story.append(logo)
    story.append(Spacer(1, 12))  # Add some space below the logo

    # Data for table
    data = [
        ["Invoice To:", "", "Pay To:"],
        ["Johnny Chen", "", "POH LLC"],
        ["4912 SE 3rd Ave", "", "20 Wilderness Rd S"],
        ["Durant, OK 74701", "", "Calera, OK 74701"],
        ["", "", ""],  # Empty row for spacing
        ["Description", "Amount"],
        ["Rent", "$9,000.00"],
        ["License", "$3,800.00"],
        ["Bryan Co. Rural Water", f"${water_bill:.2f}"],
        ["OK Natural Gas", f"${gas_bill:.2f}"],
        ["360 Internet", "$104.90"],
    ]

    # Calculate total
    total = 9000 + 3800 + water_bill + gas_bill + 104.90
    data.append(["Total Due", f"${total:,.2f}"])

    # Create table
    table = Table(data, colWidths=[250, 100])

    # Add style to table
    style = TableStyle([
        ('BACKGROUND', (0, 5), (1,5), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Center for header rows
        ('ALIGN', (0, 5), (0, -1), 'LEFT'),     # Left align for description column
        ('ALIGN', (1, 5), (1, -1), 'RIGHT'),    # Right align for amount column
        
        # Background for billing info rows
        ('BACKGROUND', (0, 5), (0, 5), colors.whitesmoke),
        ('BACKGROUND', (1, 5), (1, 5), colors.whitesmoke),

        # Grid only for billing info rows
        ('BOX', (0, 5), (0, 5), 0.25, colors.black),
        ('BOX', (1, 5), (1, 5), 0.25, colors.black),
        ('BOX', (1, 11), (1, 11), 0.25, colors.gray),
    ])
    table.setStyle(style)

    # Add table to story
    story.append(table)

    # Build PDF
    doc.build(story)

create_invoice()

