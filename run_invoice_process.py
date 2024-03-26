import os
from water_bill_script import get_water_bill
from gas_bill_script import get_gas_bill
from pdfinvoice import create_invoice
from email_script import send_email

def run_invoice_process():
    # Step 1: Scrape water and gas bills
    get_water_bill()
    get_gas_bill()

    # Step 2: Generate the invoice PDF
    create_invoice()

    # Step 3: Define the path to the invoice PDF
    invoice_pdf_path = os.path.expanduser('~/invoicescript/invoice.pdf')

    # Step 4: Email the invoice
    send_email(invoice_pdf_path, "cal@calwilkins.com", ["keith@poh.llc"])

# Run the entire invoice process
run_invoice_process()

