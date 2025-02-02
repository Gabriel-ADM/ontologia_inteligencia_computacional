# Geração de Laudos por Ontologia

Este projeto usa Flask para gerar laudos em PDF personalizados a partir de dados de um formulário.

## Como Executar

1. **Instale as Dependências**

   Instale as bibliotecas necessárias com:

   ```bash
   pip install Flask pdfrw reportlab
   ```

2. **Prepare o Arquivo PDF Base**

   Coloque o arquivo PDF base (`esqueleto_laudo.pdf`) no diretório de instruções.

3. **Execute o Servidor Flask**

   Salve o código em um arquivo Python, por exemplo, `app.py`, e inicie o servidor com:

   ```bash
   python app.py
   ```

4. **Acesse o Formulário**

   Abra um navegador e acesse [http://localhost:5000/](http://localhost:5000/) para visualizar o formulário.

5. **Preencha e Envie o Formulário**

   Complete o formulário e envie. O servidor gerará um PDF com as informações fornecidas e fornecerá um link para download.

---