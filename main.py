import pandas as pd
from twilio.rest import Client # tem que fazer cadastro na Twilio

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 50000).any(): # para vendas acima de 50000
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 50000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 50000, 'Vendas'].values[0]

        """ Se algum valor na coluna vendas na tabela_vendas for maior de 55000,
        executar comando. tudo dentro do parenteses com .any() para dizer que é
        pra ser qualquer um dos valores dentro desta tabela. Sempre que se faz um .loc
        a resposta dele é uma tabela, para retornar o nome correto sempre no final
        tem que se colocar o .values[0]."""
        print(f'No mês {mes} o vendedor {vendedor} vendeu R$ {vendas}!')
        message = client.messages.create(
            to="seunumero",
            from_="numerofornecidopeloTwilio",
            body=f'No mês {mes} o vendedor {vendedor} vendeu R$ {vendas}!')
        print(message.sid)
