# suporte_infopublic

Realizar as seguintes correções:

1. Retirar o 'None' que aparecem em 'Senha sistema' para usuários que não possuem a senha do sistema,
   isto poderá ocasionar dúvidas e induzir o usuário a achar que é a senha dele.
2. Adicionar um try-except na função de envio de emails, informando em mensagem flash caso ocorra erro
   no envio de emails.