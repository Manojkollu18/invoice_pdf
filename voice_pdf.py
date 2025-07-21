from fpdf import FPDF
from datetime import datetime

class InvoiceGenerator:
    def __init__(self, client_name, items, output_path="invoice.pdf"):
        self.client_name = client_name
        self.items = items  # List of dicts: {'description': str, 'quantity': int, 'price': float}
        self.output_path = output_path
        self.invoice_date = datetime.now().strftime("%d-%m-%Y")
        self.pdf = FPDF()
        
    def generate_invoice(self):
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)
        
        # Header
        self.pdf.set_font("Arial", "B", 16)
        self.pdf.cell(200, 10, txt="INVOICE", ln=1, align="C")

        # Client Info
        self.pdf.set_font("Arial", size=12)
        self.pdf.cell(100, 10, txt=f"Client: {self.client_name}", ln=1)
        self.pdf.cell(100, 10, txt=f"Date: {self.invoice_date}", ln=1)

        # Table Header
        self.pdf.set_font("Arial", "B", 12)
        self.pdf.cell(100, 10, "Description", 1)
        self.pdf.cell(30, 10, "Quantity", 1)
        self.pdf.cell(30, 10, "Price", 1)
        self.pdf.cell(30, 10, "Total", 1)
        self.pdf.ln()

        # Items
        self.pdf.set_font("Arial", size=12)
        grand_total = 0
        for item in self.items:
            desc = item['description']
            qty = item['quantity']
            price = item['price']
            total = qty * price
            grand_total += total
            self.pdf.cell(100, 10, desc, 1)
            self.pdf.cell(30, 10, str(qty), 1)
            self.pdf.cell(30, 10, f"{price:.2f}", 1)
            self.pdf.cell(30, 10, f"{total:.2f}", 1)
            self.pdf.ln()

        # Grand Total
        self.pdf.set_font("Arial", "B", 12)
        self.pdf.cell(160, 10, "Grand Total", 1)
        self.pdf.cell(30, 10, f"{grand_total:.2f}", 1)

        # Save File
        self.pdf.output(self.output_path)
        print(f"Invoice saved to {self.output_path}")

# === Sample Usage ===

if __name__ == "__main__":
    client_name = "John Doe"
    items = [
        {"description": "Web Design", "quantity": 1, "price": 500.0},
        {"description": "Hosting (1 year)", "quantity": 1, "price": 100.0},
        {"description": "Domain (.com)", "quantity": 1, "price": 15.0}
    ]

    invoice = InvoiceGenerator(client_name, items, output_path="invoice_john_doe.pdf")
    invoice.generate_invoice()
