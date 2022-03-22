print('''To use this program run a blast2 with the fasta of your protein that is modeled in jmol as the query sequence
with your original protein as the subject. Copy paste the entire "in the middle" matching amino acid row and input it 
as the match string. Then find the number of the first matching amino acid of your query sequence and input that as the
number of the first match. You should then get the residue numbers of your matching amino acids to be put into resmol.''')
print()
pure_matches = input('Input match string:')

first_match = input('Input the number of the first match:')

matches = list(pure_matches)

alphabet = 'abcdefghijklmnopqrstuvwxyz'

A_caps = alphabet.upper()

ALC = list(A_caps)

fmatch = []

matchnum = 0

while matchnum < len(matches):
    if matches[matchnum] in ALC:
        fmatch.append(397 + matchnum)
        matchnum += 1
    else:
        matchnum += 1

print()

print('Your matching residue numbers are:')

print(fmatch)
