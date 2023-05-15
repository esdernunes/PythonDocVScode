'''import win32ui
import win32print
import win32con

drivers = win32print.EnumPrinterDrivers(None, None, 2)
hPrinter = win32print.OpenPrinter("POS58") #Adiciona o nome da impressora 
printer_info = win32print.GetPrinter(hPrinter, 2)
for driver in drivers:
    if driver["Name"] == printer_info["pDriverName"]:
        printer_driver = driver
raw_type = "XPS_PASS" if printer_driver["Version"] == 4 else "RAW"

try:
  hJob = win32print.StartDocPrinter(hPrinter, 1, ("test of raw data", None, raw_type))
  try:
    win32print.StartPagePrinter(hPrinter)
    #win32print.WritePrinter(hPrinter, raw_data) #imprimir uma variavel
    win32print.WritePrinter(hPrinter, b"\x1b\x40Hello, world!\n\x1d\x56\x41\x10") #imprimir um texto
    win32print.EndPagePrinter(hPrinter)
  finally:
    win32print.EndDocPrinter(hPrinter)
finally:
  win32print.ClosePrinter(hPrinter)'''




import win32ui
import win32print
import win32con

drivers = win32print.EnumPrinterDrivers(None, None, 2)
hPrinter = win32print.OpenPrinter("POS58") #Adiciona o nome da impressora 
printer_info = win32print.GetPrinter(hPrinter, 2)
for driver in drivers:
    if driver["Name"] == printer_info["pDriverName"]:
        printer_driver = driver
raw_type = "XPS_PASS" if printer_driver["Version"] == 4 else "RAW"

try:
    with open("texto.txt", "r",encoding='utf-8') as f:  # abrir o arquivo "texto.txt"
        content = f.readlines()  # ler o conteúdo do arquivo linha por linha
        #content.reverse()  # inverter a ordem das linhas

    hJob = win32print.StartDocPrinter(hPrinter, 1, ("test of raw data", None, raw_type))
    try:
        win32print.StartPagePrinter(hPrinter)
        for line in content:
            win32print.WritePrinter(hPrinter, line.replace("\n","\r\n").encode('utf-8'))  # enviar cada linha do arquivo para a impressora
        win32print.WritePrinter(hPrinter, "\r\n".encode('utf-8'))
        win32print.EndPagePrinter(hPrinter)
    finally:
        win32print.EndDocPrinter(hPrinter)
finally:
    win32print.ClosePrinter(hPrinter)
