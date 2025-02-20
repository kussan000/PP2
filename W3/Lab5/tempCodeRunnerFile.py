    value = line.split(":")[-1].strip().replace(" ", "").replace(",", ".")
        if value:  # Проверяем, что строка не пустая
            receipt["payment"]["VAT_12%"] = float(value)
        else:
            rec