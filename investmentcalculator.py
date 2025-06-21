#taxa_de_=Q´[ÇD
# ´W    [ÇD
#   W´ÇD
# ´cljuros_ao_ano = 13.75 #tempo_em_meses = 6 #rendimento_total = valor_inicial * taxa_de_juros_ao_ano * tempo_em_meses # => 111,4583333

c = float(input('valor do capital: '))
i = float(input('taxa tempo: '))
t = floar(input('tempo: '))

# M = C*(1+i)**t

def rendimento_total (valor_inicial, taxa_de_juros_ao_ano, tempo_em_meses)
    taxa_de_juros_ao_ano_decimal = taxa_de_juros_ao_ano/100
    taxa_de_juros_ao_mes = taxa_de_juros_ao_ano_decimal/12
    taxa = taxa_de_juros_ao_mes+1
    fator_de_juros = taxa**tempo_em_meses
    montante = fator_de_juros*valor_inicial
    montante_arredondada = round (montante, 2)

    print(f'R$ {montante_arredondada:.2f}')

rendimento_total(c, i, t)
