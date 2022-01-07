from enum import Enum


class MessageEnum(Enum):
    RULES = (
        "**Regras:**\n"
        + "- Cada emblema de Maestria 7 novo vale um ponto\n"
        + "- Cada emblema de Maestria 6 novo vale 0,5 ponto\n"
        + "- Pra entrar no campeonato tem que postar a foto atual dos emblemas atuais e das maestrias 7\n"
        + "- Só são contabilizados emblemas obtidos depois da adesão ao campeonato\n"
    )

    COMMANDS_LIST = (
        "**COMANDOS DO BOT**\n"
        + "**?rules :** Regras do campeonato\n"
        + "**?p :** Pontos atuais\n"
        + "**?r :** Ranking atual de jogadores\n"
        + "**?m6 :** Cadastrar emblema de Maestria 6\n"
        + "**?m7 :** Cadastrar emblema de Maestria 7\n"
        + "**?c :** Se cadastrar no campeonato\n"
        + "**?rg :** Ranking Geral de todas temporadas"
    )

    REGISTERED_SUCCESSFULLY = "cadastrado no sistema," + "aguarde sua aprovação"

    EVERY_SEASON_RANKING = "**Ranking de todas temporadas:**\n"

    M6_EMBLEM = " parabéns pelo Emblema M6! - Pontos totais: "

    M7_EMBLEM = " parabéns pelo Emblema M7! - Pontos totais: "

    PLEASE_SEND_PICTURE = (
        "Por favor, envie a foto do emblema antes de realizar o cadastro"
    )

    IMAGE_REGISTERED = "Imagem cadastrada com sucesso!"
