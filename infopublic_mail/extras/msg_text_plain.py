def mensagem(nome, cpf, senha, senha_sistema):
    msg = f"""
    Olá {nome},

    Segue abaixo seus dados de login para ter acesso aos nossos sistemas.

    Login: Infopublic\{cpf}
    Senha: {senha}
    Senha do sistema: {senha_sistema}

    Instruções:
        - Se você já tiver o ícone de acesso, basta clicar e inserir seu login
        e senha.
        - Após acesso bem sucedido, basta escolher o sistema que deseja acessar,
        só que desta vez você irá inserir a senha do sistema.

    Em caso de dúvidas basta retornar este email.

    suporte@infopublic.com.br
    """

    return msg