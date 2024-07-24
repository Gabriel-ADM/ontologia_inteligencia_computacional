# Geração de Laudos por Ontologia

Este projeto cria um servidor web usando Flask para gerar laudos PDFs personalizados com base em dados preenchidos em um formulário.

## Como Executar

1. **Instale as Dependências**

   Certifique-se de ter as bibliotecas necessárias instaladas. Execute o seguinte comando para instalar as dependências:

   ```bash
   pip install Flask pdfrw reportlab
Prepare o Arquivo PDF Base

Coloque o arquivo PDF base (esqueleto_laudo.pdf) no diretório Instruções.

Execute o Servidor Flask

Salve o código em um arquivo Python, por exemplo, app.py, e execute o servidor Flask com:

bash
Copiar código
python app.py
Acesse o Formulário

Abra um navegador web e vá para http://localhost:5000/ para acessar o formulário de entrada.

Preencha e Envie o Formulário

Preencha o formulário com as informações necessárias e envie. O servidor gerará um PDF com base nas informações fornecidas e fornecerá um link para download do PDF gerado.