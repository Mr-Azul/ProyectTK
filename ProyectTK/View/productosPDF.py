from reportlab.pdfgen.canvas import Canvas
from datetime import datetime, timedelta
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape


class Archivo:
    """
    Información de: Documento
    """
    def __init__(self, nombre_modelo,  dia_reporte):
        self.nombre_modelo = nombre_modelo
        self.dia_reporte = dia_reporte
class ReportPdf:
    list=[]
    def __init__(self, list,file_name):
        
        
        list=list
        archivo = Archivo('Productos', datetime.now().strftime('%d/%m/%Y'))

        
        document_title = 'Dulce Cherry'
        title = 'Dulce Cherry'
        nombre_colaborador = archivo.nombre_modelo
        fecha_actual = archivo.dia_reporte
        canvas = Canvas(file_name)
        canvas.setPageSize(landscape(letter))
        canvas.setTitle(document_title)
        canvas.setFont("Helvetica-Bold", 20)
        canvas.drawCentredString(230+100, 805-250, title)
        canvas.setFont("Helvetica", 16)
        canvas.drawCentredString(230+100, 785-250, nombre_colaborador)
        canvas.setFont("Helvetica", 14)
        canvas.drawCentredString(230+100, 765-250, fecha_actual)

        title_background = colors.fidblue
        data_actividades = [
            ['Id', 'Codigo', 'Nombre', 'Proveedor', 'Precio', 'Stock'],
        ]
        for i in list:
            data_actividades.append([i[0], i[1], i[2], i[3], i[4], i[5]])
            table_actividades = Table(data_actividades, colWidths=85, rowHeights=15, repeatRows=0)
            tblStyle = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), title_background),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
            rowNumb = len(data_actividades)
            for row in range(1, rowNumb):
               
                table_background = colors.aliceblue
                tblStyle.add('BACKGROUND', (0, row), (-1, row), table_background)
            table_actividades.setStyle(tblStyle)
            width = 150
            height = -600
            table_actividades.wrapOn(canvas, width, height)
            table_actividades.drawOn(canvas, 65, (0 - height) - 240)

        canvas.save()
