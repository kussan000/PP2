import re
import json

class ReceiptParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.receipt_dict = {
            "store": "",
            "BIN": "",
            "VAT": "",
            "VAT_series": "",
            "cash_register": "",
            "shift": "",
            "receipt_number": "",
            "cashier": "",
            "items": [],
            "total": 0.0,
            "payment_method": "Банковская карта",
            "fiscal_signature": "",
            "date_time": "",
            "address": "",
            "operator": ""
        }

    def parse(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            receipt_text = file.read()

        item_pattern = re.compile(r"(\d+)\.\s+(.+?)\n(\d+,\d+) x ([\d\s]+,\d+)\n([\d\s]+,[\d]{2})")
        total_pattern = re.compile(r"ИТОГО:\s*([\d\s]+,[\d]{2})")
        payment_pattern = re.compile(r"Банковская карта:\s*([\d\s]+,[\d]{2})")
        date_pattern = re.compile(r"Время:\s*([\d\.]+\s[\d:]+)")

        lines = receipt_text.split("\n")
        for line in lines:
            line = line.strip()

            if "Филиал" in line:
                self.receipt_dict["store"] = line
            elif "БИН" in line:
                self.receipt_dict["BIN"] = line.split()[-1]
            elif "НДС" in line:
                self.receipt_dict["VAT"] = line.split()[-1]
            elif "Касса" in line:
                self.receipt_dict["cash_register"] = line.split()[-1]
            elif "Смена" in line:
                self.receipt_dict["shift"] = line.split()[-1]
            elif "Порядковый номер чека" in line:
                self.receipt_dict["receipt_number"] = line.split()[-1]
            elif "Кассир" in line:
                self.receipt_dict["cashier"] = line.split()[-1]
            elif "Фискальный признак" in line:
                self.receipt_dict["fiscal_signature"] = line.split()[-1]
            elif "г." in line:
                self.receipt_dict["address"] = line
            elif "Оператор фискальных данных" in line:
                self.receipt_dict["operator"] = line

            date_match = date_pattern.search(line)
            if date_match:
                self.receipt_dict["date_time"] = date_match.group(1)

            total_match = total_pattern.search(line)
            if total_match:
                self.receipt_dict["total"] = float(total_match.group(1).replace(" ", "").replace(",", "."))

            payment_match = payment_pattern.search(line)
            if payment_match:
                self.receipt_dict["payment_method"] = float(payment_match.group(1).replace(" ", "").replace(",", "."))

        item_matches = item_pattern.findall(receipt_text)
        self.receipt_dict["items"] = [
            {
                "name": match[1].strip(),
                "quantity": float(match[2].replace(",", ".")),
                "unit_price": float(match[3].replace(" ", "").replace(",", ".")),
                "total_price": float(match[4].replace(" ", "").replace(",", "."))
            }
            for match in item_matches
        ]

    def to_json(self, output_file):
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(self.receipt_dict, file, ensure_ascii=False, indent=4)

    


if __name__ == "__main__":
    parser = ReceiptParser("C:/Users/mansu/Downloads/row.txt")
    parser.parse()
    parser.to_json("C:/Users/mansu/Downloads/receipt.json")

#C:/Users/mansu/Downloads/row.txt