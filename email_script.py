import smtplib
from email.message import EmailMessage
from credentials import EMAIL_ADDRESS, EMAIL_PASSWORD
import os

def send_email(invoice_pdf_path, recipient_email, cc_emails):
    msg = EmailMessage()
    msg['Subject'] = 'Your Monthly Invoice'
    msg['From'] = 'keith@legacycult.com'  # Replace with your email
    msg['To'] = recipient_email
    msg['Cc'] = ', '.join(cc_emails)
    msg.set_content('Attached is your monthly invoice.')

    with open(invoice_pdf_path, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

# Correct the path before sending it to the function
invoice_pdf_path = os.path.expanduser('~/invoicescript/invoice.pdf')
send_email(invoice_pdf_path, "skychen888999@gmail.com", ["cal@calwilkins.com", "keith@poh.llc"])

