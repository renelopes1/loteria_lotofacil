import requests
import pandas as pd
import collections
import sys

url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=Lotof%C3%A1cil'
#url = sys.argv[1]
r = requests.get(url, verify=False)

#Removendo os caracteres do arquivo da Caixa transformar utilizar o read_html
r.text
r_text = r.text.replace('\\r\\n', '')
r_text = r.text.replace('"\r\n}', '')
r_text = r.text.replace('"\r\n}\'', '')
r_text = r.text.replace('{\r\n  "html": "', '')
##r_text[:15] - Mostrar ultimos caracteres
df = pd.read_html(r_text)

type(df)
type(df[0])

df=df[0].copy()

new_columns = df.columns
new_columns = list(i.replace('\\r\\n','') for i in new_columns)
new_columns

df.columns = new_columns
#Removendo os valores nulo
df = df[df['Bola1']==df['Bola1']]

df = pd.DataFrame({
    'Bola1': df['Bola1'].astype(int),
    'Bola2': df['Bola2'].astype(int),
    'Bola3': df['Bola3'].astype(int),
    'Bola4': df['Bola4'].astype(int),
    'Bola5': df['Bola5'].astype(int),
    'Bola6': df['Bola6'].astype(int),
    'Bola7': df['Bola7'].astype(int),
    'Bola8': df['Bola8'].astype(int),
    'Bola9': df['Bola9'].astype(int),
    'Bola10': df['Bola10'].astype(int),
    'Bola11': df['Bola11'].astype(int),
    'Bola12': df['Bola12'].astype(int),
    'Bola13': df['Bola13'].astype(int),
    'Bola14': df['Bola14'].astype(int),
    'Bola15': df['Bola15'].astype(int),
})

nr_pop = list(range(1,26))
nr_pares = [2,4,6,8,10,12,14,16,18,20,22,24]
nr_impares = [1,3,5,7,9,11,13,15,17,19,21,23,25]
nr_primos = [2,3,5,7,11,13,17,19,23]

comb = []
v_01 = 0
v_02 = 0
v_03 = 0
v_04 = 0
v_05 = 0
v_06 = 0
v_07 = 0
v_08 = 0
v_09 = 0
v_10 = 0
v_11 = 0
v_12 = 0
v_13 = 0
v_14 = 0
v_15 = 0
v_16 = 0
v_17 = 0
v_18 = 0
v_19 = 0
v_20 = 0
v_21 = 0
v_22 = 0
v_23 = 0
v_24 = 0
v_25 = 0

lst_campos = ['Bola1','Bola2','Bola3','Bola4','Bola5',
              'Bola6','Bola7','Bola8','Bola9','Bola10',
              'Bola11','Bola12','Bola13','Bola14','Bola15']



for index, row in df.iterrows():
    v_pares = 0
    v_impares = 0
    v_primos = 0
    for campo in lst_campos:
        if row[campo] in nr_pares:
            v_pares += 1
        if row[campo] in nr_impares:
            v_impares += 1
        if row[campo] in nr_primos:
            v_primos += 1
        if row[campo] == 1:
            v_01 += 1
        if row[campo] == 2:
            v_02 += 1
        if row[campo] == 3:
            v_03 += 1
        if row[campo] == 4:
            v_04 += 1
        if row[campo] == 5:
            v_05 += 1
        if row[campo] == 6:
            v_06 += 1
        if row[campo] == 7:
            v_07 += 1
        if row[campo] == 8:
            v_08 += 1
        if row[campo] == 9:
            v_09 += 1
        if row[campo] == 10:
            v_10 += 1
        if row[campo] == 11:
            v_11 += 1
        if row[campo] == 12:
            v_12 += 1
        if row[campo] == 13:
            v_13 += 1
        if row[campo] == 14:
            v_14 += 1
        if row[campo] == 15:
            v_15 += 1
        if row[campo] == 16:
            v_16 += 1
        if row[campo] == 17:
            v_17 += 1
        if row[campo] == 18:
            v_18 += 1
        if row[campo] == 19:
            v_19 += 1 
        if row[campo] == 20:
            v_20 += 1
        if row[campo] == 21:
            v_21 += 1
        if row[campo] == 22:
            v_22 += 1
        if row[campo] == 23:
            v_23 += 1
        if row[campo] == 24:
            v_24 += 1
        if row[campo] == 25:
            v_25 += 1
    
    comb.append(str(v_pares)+'p-'+str(v_impares)+'i-'+str(v_primos)+'np')

freq_nr = [
    [1,v_01],
    [2,v_02],
    [3,v_03],
    [4,v_04],
    [5,v_05],
    [6,v_06],
    [7,v_07],
    [8,v_08],
    [9,v_09],
    [10,v_10],
    [11,v_11],
    [12,v_12],
    [13,v_13],
    [14,v_14],
    [15,v_15],
    [16,v_16],
    [17,v_17],
    [18,v_18],
    [19,v_19],
    [20,v_20],
    [21,v_21],
    [22,v_22],
    [23,v_23],
    [24,v_24],
    [25,v_25]
]

#ordenar 
freq_nr
freq_nr.sort(key=lambda tup:tup[1])

freq_nr[0]
freq_nr[-1]

counter = collections.Counter(comb)
resultado = pd.DataFrame(counter.items(),columns=['Combinacao','Frequencia'])
resultado['p_freq'] = resultado['Frequencia']/resultado['Frequencia'].sum()
resultado = resultado.sort_values(by='p_freq')


print('''
O número mais frequente é o: {}
O número menos frequente é o: {}
A Combinação de Pares, Ímpares e Prirmos mais frequente é: {} com a frequencia de: {}%
'''.format(freq_nr[-1][0],freq_nr[0][0],resultado['Combinacao'].values[-1],int((resultado['p_freq'].values[-1]*100)*100)/100)
)