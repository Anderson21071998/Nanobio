#  Caderno de dados

Os primeiros dias foram voltados a adquirir uma certa familiaridade com os programas que iriamos utilizar com  maior frequência, tanto o Autodock Vina quanto o Discovery studio.
        Certo para um primeiro ponto vamos discutir um pouco sobre as ferramentas, colocar alguns pontos importantes para que auxiliem tanto caso eu queira vir aqui reler a fim de relembrar algumas coisas. Tanto o DS quanto o AutodockTools (Vina), são software para modelagem molecular, usaremos o primeiro para fazer um tratamento da molécula ou proteína (não se restringindo a isso), e o segundo para fazer os cálculos da posição do ligante com a proteína, podemos fazer o tratamento das moléculas e proteínas no Vina, mas acredito que seja mais fácil de visualizar no DS.
       Alguns conceito importantes:
Sítio Catalítico. 
O sítio catalítico é uma região da proteína que forma um pequeno compartimento onde a catálise de uma certa reação química é mais favorável, no caso de protease, esta reação é hidrólise da ligação peptídica

Estrutura Secundária da Proteína.
A estrutura secundária da proteína corresponde a região localizada de estrutura ordenada estabilizada por ligações de hidrogênio entre os grupos -NH e C=O da cadeia principal as cadeias laterais. os dois tipos principais de estruturas secundárias são hélices alfa e alpha beta

Segue anotações das minhas pesquisas.

Primeira parte, foi a escolha dos ligantes, para ser mais exato, a escolha de dois ligantes, a princípio não deveria ser escolhido qualquer tipo de fármaco que estivesse disponibilizado, pois existem alguns problemas que devem ser levados em conta, o primeiro é as limitações que o Vina nem com software, ele não fornece dados precisos de ligações proteínas + proteínas, sendo assim não era possível a escolha do Interferon beta, outro problema era encontrar a estrutura modelada do ligante e da proteína a qual ele fazia referência, analisando esses problemas durante um dia cheguei a conclusão que o Lopinavir e o Ritonavir, eram boas escolhas, analisados independentemente.
Agora eu me orientei para encontrar a proteína que nos artigos demonstram que o ligante possa vir a fazer um efeito significativo

Dificuldades:
    Senti muita dificuldades em rodar o Vina, nos tutoriais foi tecnicamente acessível, mas executar os programas sozinho é outra coisa
    Semana do dia 09/10/20:

Fiz testes iniciais com as moléculas do Lopinavir e do ritonavir para checagem das energias de ligação, os resultados obtidos seguem abaixo
Resultados Obtidos com o Lopinavir na Mpro do coronavírus, no sítio catalítico da HIS 41 e CYS 145 
   Os resultados foram obtidos usando as seguintes especificações, a caixa de encaixe tinha a dimensão 30 X 30 X 30, e a localização dela foi na posição (-22, 5, 13.084).

1 teste
mode |   affinity | dist from best mode
     | (kcal/mol) | rmsd l.b.| rmsd u.b.
-----+------------+----------+----------
   1         -8.4      0.000      0.000
   2         -8.2      2.075      6.018
   3         -8.1      1.268      3.327
   4         -8.1      1.169      3.465
   5         -7.9      2.688      7.185
   6         -7.7      2.035      4.385
   7         -7.7      2.858      7.970
   8         -7.7      2.122      3.097
   9         -7.6      2.086      8.293


2 teste

mode |   affinity | dist from best mode
     | (kcal/mol) | rmsd l.b.| rmsd u.b.
-----+------------+----------+----------
   1         -8.4      0.000      0.000
   2         -8.2      2.179      6.293
   3         -8.1      1.070      3.329
   4         -8.1      2.646      7.026
   5         -7.8      2.313      8.102
   6         -7.7      2.664      7.056
   7         -7.7      2.860      4.984
   8         -7.7      1.969      4.703
   9         -7.7      1.844      3.904


Teste com o Ritonavir na Mpro

1 Teste:
mode |   affinity | dist from best mode
     | (kcal/mol) | rmsd l.b.| rmsd u.b.
-----+------------+----------+----------
   1         -7.3      0.000      0.000
   2         -6.6      3.173      5.814
   3         -6.5      3.087      7.369
   4         -6.5      3.716      9.288
   5         -6.5      2.361      5.351
   6         -6.5      2.991      4.963
   7         -6.4      3.166      5.409
   8         -6.4      2.705      5.898
   9         -6.4      4.109     10.200


2 Teste:
mode |   affinity | dist from best mode
     | (kcal/mol) | rmsd l.b.| rmsd u.b.
-----+------------+----------+----------
   1         -6.5      0.000      0.000
   2         -6.5      3.853      6.563
   3         -6.5      3.455      6.311
   4         -6.3      2.003      3.543
   5         -6.2      3.139      7.220
   6         -6.2      3.839      6.362
   7         -6.2      3.473      6.811
   8         -6.2      2.007      3.791
   9         -6.2      4.126      6.422


   Estudarei agora as moléculas do lopinavir e do ritonavir em outra parte da Mpro, a parte relacionada a união das cadeias, tanto a ARG 4, quanto a GLU 290 , segue os resultados obtidos
   Os resultados foram adquiridos usando especificações diferentes da outra, o tamanho da caixa foi 22 X 22 X 22, e a posição espacial dela foi (-3, -7, 27) que é uma região entre os dois aminoácidos.

Para o Lopinavir
1 teste

mode |   affinity | dist from best mode
     | (kcal/mol) | rmsd l.b.| rmsd u.b.
-----+------------+----------+----------
   1         -6.6      0.000      0.000
   2         -6.5      1.318      3.251
   3         -6.4      3.308      6.830
   4         -6.2      2.838      8.452
   5         -6.2      2.734      7.648
   6         -6.2      2.732      8.183
   7         -6.0      3.383      6.851
   8         -6.0      2.034      6.815
   9         -6.0      3.436      6.732


2 teste

mode |   affinity | dist from best mode
     | (kcal/mol) | rmsd l.b.| rmsd u.b.
-----+------------+----------+----------
   1         -6.9      0.000      0.000
   2         -6.6      4.071      7.517
   3         -6.5      2.079      5.916
   4         -6.5      2.416      8.135
   5         -6.4      3.219      9.952
   6         -6.4      2.244      5.557
   7         -6.4      2.373      5.955
   8         -6.4      3.836      5.862
   9         -6.3      4.152      7.545

Para o Ritonavir

1 teste

mode |   affinity | dist from best mode
     | (kcal/mol) | rmsd l.b.| rmsd u.b.
-----+------------+----------+----------
   1         -6.7      0.000      0.000
   2         -6.4      3.140      7.386
   3         -6.4      3.107      7.174
   4         -6.1      2.699      8.221
   5         -6.1      2.884      8.867
   6         -6.0      2.733      7.639
   7         -6.0      2.745      6.577
   8         -6.0      3.090      7.042
   9         -6.0      3.412     10.044

2 teste

mode |   affinity | dist from best mode
     | (kcal/mol) | rmsd l.b.| rmsd u.b.
-----+------------+----------+----------
   1         -6.4      0.000      0.000
   2         -6.4      3.181      7.259
   3         -6.3      3.665     10.346
   4         -6.3      2.706      8.488
   5         -6.3      1.632      2.168
   6         -6.2      2.872      7.681
   7         -6.2      4.179      8.868
   8         -6.2      3.464      6.645
   9         -6.1      2.089      7.459


 Fiz dois testes referentes a cada uma das moléculas, e os resultados foram aceitáveis, encontrei algumas dificuldades o processo de fazer os testes, mas que durante o processo foram resolvidas, grande parte dessas dificuldades giravam em torno da má organização que eu tive ao fazer os testes, não atualizei o nome do arquivo de saída devido a isso eles ficavam se sobrepondo e apagando o anterior. Na reunião do dia 09/10 foram feitas observações referentes a diferença de valor do ritonavir na Mpro agindo no sítio catalítico, acredito que isso tenha sido erro humano gerado por mim no tratamento tanto da proteína quanto do ligante, a falta de incluir o hidrogênios ionizáveis deve ter gerado essa exclusão do valor -7,3 gerado no primeiro teste.

