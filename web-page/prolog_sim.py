def generate_report(implante, tomossintese, limitacao):
    base_text = "Exame realizado em mamógrafo digital, marca Siemens, nas incidências de rotina Craniocaudal (CC) e Mediolateral Oblíqua (MLO) com extensão axilar usando foco de 0,3 mm"
    
    # Adicionar tomossíntese se aplicável
    if tomossintese == 'com_tomossintese':
        base_text += ", complementado com tomossíntese para melhor visualização de achados anormais"
    
    # Adaptar texto para pacientes com implante
    if implante == 'com_implante':
        base_text += ", adaptado para pacientes com implantes mamários"
    
    # Adicionar informações de limitação
    if limitacao == 'com_limitacao':
        base_text += ". Apesar de alguns desafios técnicos, como a posição do implante, o"
        base_text += "s filmes serão impressos e entregues posteriormente ao exame."
    else:
    # Texto final
        base_text += ". Os filmes serão impressos e entregues posteriormente ao exame."
    
    return base_text

# Testando a função com diferentes combinações
# print(generate_report('com_implante', 'com_tomossintese', 'com_limitacao'))
# print(generate_report('com_implante', 'com_tomossintese', 'sem_limitacao'))
# print(generate_report('com_implante', 'sem_tomossintese', 'com_limitacao'))
# print(generate_report('com_implante', 'sem_tomossintese', 'sem_limitacao'))
# print(generate_report('sem_implante', 'com_tomossintese', 'com_limitacao'))
# print(generate_report('sem_implante', 'com_tomossintese', 'sem_limitacao'))
# print(generate_report('sem_implante', 'sem_tomossintese', 'com_limitacao'))
# print(generate_report('sem_implante', 'sem_tomossintese', 'sem_limitacao'))
