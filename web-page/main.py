import io
from flask import Flask, render_template, request, send_file
from pdfrw import PdfReader, PdfWriter, PageMerge
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from prolog_sim import generate_report

app = Flask(__name__)

def draw_wrapped_text(canvas, text, x, y, max_width, font_size):
    canvas.setFont("Helvetica", font_size)
    lines = []
    words = text.split()
    current_line = ""
    
    for word in words:
        test_line = f"{current_line} {word}".strip()
        width = canvas.stringWidth(test_line, "Helvetica", font_size)
        if width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)
    
    y_offset = y
    for line in lines:
        canvas.drawString(x, y_offset, line)
        y_offset -= font_size + 2  # Adjust line height for wrapping

def create_overlay(data):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    
    font_size_smaller = 9
    font_size_bigger = 10
    first_header_item_height = 692
    larger_item_left = 50
    
    can.setFont("Helvetica", font_size_smaller)
    can.drawString(125, first_header_item_height, data['Nome do Paciente'])
    can.drawString(90, first_header_item_height-17, data['Prontuário'])
    can.drawString(170, first_header_item_height-17*2, data['Data de realização do exame'])
    can.drawString(130, first_header_item_height-17*3, data['Data de nascimento'])
    can.drawString(315, first_header_item_height, data['Sexo'])
    can.drawString(415, first_header_item_height-17, data['Hora de realização do exame'])
    can.drawString(315, first_header_item_height-17*2, data['Idade'])
    
    can.setFont("Helvetica", font_size_bigger)
    
    # Define max width for text wrapping
    max_width = 520
    
    draw_wrapped_text(can, data['Indicação do exame / História clínica'], larger_item_left, 530, max_width, font_size_bigger)
    draw_wrapped_text(can, data['Técnica do exame'], larger_item_left, 445, max_width, font_size_bigger)
    draw_wrapped_text(can, data['Descrição da composição da mama / padrão de densidade'], larger_item_left, 375, max_width, font_size_bigger)
    draw_wrapped_text(can, data['Descrição dos achados mamográfico'], larger_item_left, 290, max_width, font_size_bigger)
    draw_wrapped_text(can, data['Avaliação comparativa com exames anteriores'], larger_item_left, 220, max_width, font_size_bigger)
    
    can.drawString(larger_item_left+100, 141, data['Categoria BI-RADS'])
    can.drawString(larger_item_left, 110, data['Recomendação de conduta'])
    
    can.save()
    packet.seek(0)

    return packet


# Função para preencher o PDF
def fill_pdf(input_pdf, data):
    base_pdf = PdfReader(input_pdf)
    packet = create_overlay(data)
    
    overlay_pdf = PdfReader(packet)
    for i, page in enumerate(base_pdf.pages):
        overlay = PageMerge(page)
        overlay.add(overlay_pdf.pages[i]).render()
    
    output = io.BytesIO()
    writer = PdfWriter(output)
    writer.addpages(base_pdf.pages)
    writer.write()
    output.seek(0)
    
    return output

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = {
            'Nome do Paciente': request.form['Nome do Paciente'],
            'Prontuário': request.form['Prontuário'],
            'Data de realização do exame': request.form['Data de realização do exame'],
            'Data de nascimento': request.form['Data de nascimento'],
            'Sexo': request.form['Sexo'],
            'Hora de realização do exame': request.form['Hora de realização do exame'],
            'Idade': request.form['Idade'],
            'Indicação do exame / História clínica': request.form['Indicação do exame / História clínica'],
            'Técnica do exame': generate_report(f"{request.form['Implante']}_implante", f"{request.form['Tomossíntese']}_tomossintese", f"{request.form['Limitação']}_limitacao"),
            'Descrição da composição da mama / padrão de densidade': request.form['Descrição da composição da mama / padrão de densidade'],
            'Descrição dos achados mamográfico': request.form['Descrição dos achados mamográfico'],
            'Avaliação comparativa com exames anteriores': request.form['Avaliação comparativa com exames anteriores'],
            'Categoria BI-RADS': request.form['Categoria BI-RADS'],
            'Recomendação de conduta': request.form['Recomendação de conduta']
        }
        
        output_pdf = fill_pdf('Instruções\esqueleto_laudo.pdf', data)
        return send_file(output_pdf, as_attachment=True, download_name='Resultado Laudo.pdf')

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
