"""
Miguel Gonzalez Hernandez 21/4/2020
"""
asignatura=['Calculo','Circuitos','ELMG','ECOM','TV']
NotaCalculo=5
NotaCicuitos=6
NotaELMG=5
NotaEcom=3
NotaTv=7

notas=[NotaCalculo,NotaCicuitos,NotaELMG,NotaEcom,NotaTv]
print(asignatura )



for i in (range(len(notas)-1,-1,-1)):

   if(notas[i]>=5):

      del notas[i]
      del asignatura[i]



for i in asignatura:
    print(i)





