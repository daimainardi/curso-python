#cid = str(input('Em qual cidade você mora? ')).strip()
#print(cid [:5].upper() == 'SANTO')
#true
cidade = str(input('Em qual cidade você mora? ')).strip()
if cidade.upper().startswith('SANTO'):
    print('A cidade começa com Santo')
else:
    print('A cidade não começa com Santo')

