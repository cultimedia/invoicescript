## Monthly Invoice Script Playbook

**1. Activate the Virtual Environment**
Ensure you're working within the correct virtual environment to manage dependencies effectively.

```bash
source ~/invoice/bin/activate
```

**2. Navigate to Your Project Directory**
Change to the directory containing your script to ensure all file paths in the script resolve correctly.

```bash
cd /Users/keithwilkins/invoicescript
```

**3. Ensure All Dependencies Are Installed**
Install any necessary Python packages from your `requirements.txt` to avoid surprises.

```bash
pip install -r requirements.txt
```

**4. Run the Script**
Execute your script to process and send the invoices.

```bash
python3 run_invoice_process.py
```

**5. Check Sent Emails**
Verify the emails in your sent folder to ensure no tenant is emailed multiple times. This step is crucial to maintaining good relations and ensuring communication clarity.

**6. Deactivate the Virtual Environment**
Once your tasks are complete, deactivate the virtual environment to revert to your system’s default settings.

```bash
deactivate
```

**7. Periodic Review**
Schedule a monthly reminder to review this playbook and update it if there are changes in the process or environment paths.

**8. Backup Your Work**
Regularly backup your script and related files to prevent data loss and ensure continuity of operations.

