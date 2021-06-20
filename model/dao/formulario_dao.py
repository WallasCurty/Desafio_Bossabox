from application.model.entity.form import Cad


cad_list = [
    Cad(1,"Amzon Prime", "https://www.amazonprime.com/browse","Amazon Prime dispõe de filmes e series", ["Amazon", "serie"]),
    Cad(2,"Youtube", "https://www.disneyplus.com","Disney+ é um serviço de assinatura de streaming de vídeo on-line de propriedade e operado The Walt Disney Company", ["Disney", "animação"]),
    Cad(3,"Netflix", "https://www.netflix.com/browse","Netflix é uma provedora global de filmes e séries de televisão via streaming", ["filme", "serie"]),
    Cad(4,"Globo Play", "https://www.globoplay.com","Globoplay é uma plataforma digital de streaming de vídeos, desenvolvida e operada pelo Grupo Globo", ["Novelas", "serie"]),

]
class Cad_DAO():
    def __init__(self, cad_list = cad_list):
        self.cad_list = cad_list

    def listar_cad(self):
        return self.cad_list