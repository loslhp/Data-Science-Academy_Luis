#!/usr/bin/env python
# coding: utf-8

# #Calculadora em Python

# In[ ]:


print('*'*5 + 'Python Calculator' + '*'*5)
print('\n\n\nSelecione o número da operação desejada:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')
opcao = float(input('\n\nDigite sua opção (1/2/3/4):'))
#print(opcao)


# In[2]:


#print('voce selecionou a opcao', opcao)
primeiro = float(input('Digite o primeiro numero:'))
segundo = float(input('Digite o segundo numero:'))
#type(primeiro)
#type(segundo)


# In[3]:


if (opcao == 1):
        resultado = primeiro + segundo
        print(primeiro, '+', segundo, '=', resultado)
elif (opcao == 2):
        resultado = primeiro - segundo
        print(primeiro, '-', segundo, '=', resultado)
elif (opcao == 3):
        resultado = primeiro * segundo
        print(primeiro, '*', segundo, '=', resultado)
elif (opcao == 4):
        resultado = primeiro / segundo
        print(primeiro, '/', segundo, '=', resultado)
else:
        print('Selecionar opcao de 1 a 4')
  


# In[ ]:




