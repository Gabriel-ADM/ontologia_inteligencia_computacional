% report.pl

generate_report(Implante, Tomossintese, Limitacao, Relatorio) :-
    BaseText = "Exame realizado em mamógrafo digital, marca Siemens, nas incidências de rotina Craniocaudal (CC) e Mediolateral Oblíqua (MLO) com extensão axilar usando foco de 0,3 mm",
    append_tomossintese(BaseText, Tomossintese, BaseText1),
    append_implante(BaseText1, Implante, BaseText2),
    append_limitacao(BaseText2, Limitacao, Relatorio).

append_tomossintese(BaseText, 'com_tomossintese', Relatorio) :-
    atom_concat(BaseText, ", complementado com tomossíntese para melhor visualização de achados anormais", Relatorio).
append_tomossintese(BaseText, _, BaseText).

append_implante(BaseText, 'com_implante', Relatorio) :-
    atom_concat(BaseText, ", adaptado para pacientes com implantes mamários", Relatorio).
append_implante(BaseText, _, BaseText).

append_limitacao(BaseText, 'com_limitacao', Relatorio) :-
    atom_concat(BaseText, ". Apesar de alguns desafios técnicos, como a posição do implante, os filmes serão impressos e entregues posteriormente ao exame.", Relatorio).
append_limitacao(BaseText, _, Relatorio) :-
    atom_concat(BaseText, ". Os filmes serão impressos e entregues posteriormente ao exame.", Relatorio).
