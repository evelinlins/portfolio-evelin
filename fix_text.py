with open('index.modular.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix academic formation section
old = 'Base Acad\u00eamica & Did\u00e1tica</div>'
new = '2020 \u2014 2025</div>'
content = content.replace(old, new)

old = 'Licenciatura em Pedagogia & CST em Marketing Digital</h3>'
new = 'Licenciatura em Pedagogia (UNINOVE) & CST em Marketing Digital (Ampli)</h3>'
content = content.replace(old, new)

old = 'UNINOVE & Ampli (2023 - 2025)</div>'
new = 'UNINOVE (2020 \u2013 2022) \u00b7 Ampli (2023 \u2013 2025)</div>'
content = content.replace(old, new)

old_desc = 'Forma\u00e7\u00e3o superior unindo comunica\u00e7\u00e3o estrat\u00e9gica de mercado e licenciatura em Pedagogia. Minha forma\u00e7\u00e3o como professora \u00e9 um dos meus maiores diferenciais em dados e neg\u00f3cios: desenvolve did\u00e1tica refinada, escuta ativa, empatia e facilidade singular para traduzir n\u00fameros e m\u00e9tricas densas em explica\u00e7\u00f5es simples para tomadores de decis\u00e3o.'
new_desc = 'Iniciei a gradua\u00e7\u00e3o em Pedagogia pela UNINOVE em 2020 \u2014 per\u00edodo em que descobri o marketing digital \u2014 e conclu\u00ed a licenciatura em 2022. Em 2023 iniciei o CST em Marketing Digital pela Ampli, conclu\u00eddo em 2025. Minha forma\u00e7\u00e3o como professora \u00e9 um diferencial raro no universo corporativo: desenvolve did\u00e1tica refinada, escuta ativa e a facilidade singular de traduzir m\u00e9tricas densas em linguagem acess\u00edvel para qualquer equipe ou lideran\u00e7a.'
content = content.replace(old_desc, new_desc)

print('academic replaced?', 'UNINOVE (2020' in content)

# Fix Sobre Mim - Sobre Mim about text already done, just verify
print('Sobre Mim generation ok?', 'Python, SQL, Power BI, Tableau, Excel Avan' in content)

with open('index.modular.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('DONE')
