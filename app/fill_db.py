from datetime import datetime

from app.database import SessionLocal
from app.models import Pessoa


def fill_db():
    # Create a session
    session = SessionLocal()

    # Check if the Pessoa table is empty
    if not session.query(Pessoa).first():
        fixtures = [
            Pessoa(
                nome="Alberto Vieira",
                rg="25.507.105-2",
                cpf="168.637.122-53",
                data_nascimento=datetime.strptime("01-07-1997", "%d-%m-%Y"),
                data_admissao=datetime.strptime("28-09-2020", "%d-%m-%Y"),
            ),
            Pessoa(
                nome="Alexandre Teixeira",
                rg="79.474.888-8",
                cpf="877.733.889-89",
                data_nascimento=datetime.strptime("16-08-1982", "%d-%m-%Y"),
                data_admissao=datetime.strptime("15-05-2020", "%d-%m-%Y"),
            ),
            Pessoa(
                nome="Ana Carolina Souza",
                rg="52.565.667-8",
                cpf="766.370.920-96",
                data_nascimento=datetime.strptime("19-03-1982", "%d-%m-%Y"),
                data_admissao=datetime.strptime("19-08-2016", "%d-%m-%Y"),
            ),
            Pessoa(
                nome="Ana Paula Soares",
                rg="54.744.331-9",
                cpf="746.917.734-52",
                data_nascimento=datetime.strptime("01-09-1984", "%d-%m-%Y"),
                data_admissao=datetime.strptime("25-08-2019", "%d-%m-%Y"),
            ),
            Pessoa(
                nome="Antônio Siqueira",
                rg="81.669.888-5",
                cpf="695.991.412-45",
                data_nascimento=datetime.strptime("26-07-1990", "%d-%m-%Y"),
                data_admissao=datetime.strptime("18-05-2016", "%d-%m-%Y"),
            ),
            Pessoa(
                nome="Arthur Silva",
                rg="43.204.402-9",
                cpf="345.898.157-88",
                data_nascimento=datetime.strptime("30-12-1996", "%d-%m-%Y"),
                data_admissao=datetime.strptime("28-04-2016", "%d-%m-%Y"),
            ),
            Pessoa(
                nome="Bárbara Santos",
                rg="57.106.623-3",
                cpf="587.914.225-66",
                data_nascimento=datetime.strptime("04-09-2000", "%d-%m-%Y"),
                data_admissao=datetime.strptime("17-11-2018", "%d-%m-%Y"),
            ),
            Pessoa(
                nome="Beatriz Santana",
                rg="70.855.305-2",
                cpf="093.084.203-04",
                data_nascimento=datetime.strptime("17-05-1994", "%d-%m-%Y"),
                data_admissao=datetime.strptime("05-03-2018", "%d-%m-%Y"),
            ),
            Pessoa(
                nome="Caio Sampaio",
                rg="14.475.327-9",
                cpf="483.764.953-05",
                data_nascimento=datetime.strptime("18-11-1995", "%d-%m-%Y"),
                data_admissao=datetime.strptime("03-06-2020", "%d-%m-%Y"),
            ),
            Pessoa(
                nome="Carla Rodrigues",
                rg="62.692.082-5",
                cpf="566.412.961-13",
                data_nascimento=datetime.strptime("04-08-1996", "%d-%m-%Y"),
                data_admissao=datetime.strptime("31-03-2015", "%d-%m-%Y"),
            ),
            Pessoa(
                nome="Carlos Rocha",
                rg="23.782.125-5",
                cpf="053.166.034-60",
                data_nascimento=datetime.strptime("07-07-1983", "%d-%m-%Y"),
                data_admissao=datetime.strptime("08-03-2017", "%d-%m-%Y"),
            ),
            Pessoa(
                nome="Cauê Ribeiro",
                rg="33.548.790-1",
                cpf="491.145.149-15",
                data_nascimento=datetime.strptime("27-01-1981", "%d-%m-%Y"),
                data_admissao=datetime.strptime("31-12-2020", "%d-%m-%Y"),
            ),
            Pessoa(
                nome="Cláudia Reis",
                rg="54.435.082-9",
                cpf="511.020.782-80",
                data_nascimento=datetime.strptime("04-08-1986", "%d-%m-%Y"),
                data_admissao=datetime.strptime("25-09-2020", "%d-%m-%Y"),
            ),
            Pessoa(
                nome="Cláudio Ramos",
                rg="41.432.308-6",
                cpf="673.452.026-90",
                data_nascimento=datetime.strptime("12-08-1982", "%d-%m-%Y"),
                data_admissao=datetime.strptime("01-11-2019", "%d-%m-%Y"),
            ),
            Pessoa(
                nome="Daiane Pereira",
                rg="90.815.741-8",
                cpf="704.352.424-58",
                data_nascimento=datetime.strptime("22-11-2002", "%d-%m-%Y"),
                data_admissao=datetime.strptime("15-06-2017", "%d-%m-%Y"),
            ),
            Pessoa(
                nome="Diego Penha",
                rg="43.099.953-1",
                cpf="329.630.074-00",
                data_nascimento=datetime.strptime("23-02-1983", "%d-%m-%Y"),
                data_admissao=datetime.strptime("01-12-2017", "%d-%m-%Y"),
            ),
            Pessoa(
                nome="Eduardo Oliveira",
                rg="46.249.609-1",
                cpf="772.220.114-80",
                data_nascimento=datetime.strptime("12-02-2001", "%d-%m-%Y"),
                data_admissao=datetime.strptime("10-05-2020", "%d-%m-%Y"),
            ),
            Pessoa(
                nome="Eliana Nunes",
                rg="84.269.396-7",
                cpf="130.491.959-59",
                data_nascimento=datetime.strptime("03-07-1994", "%d-%m-%Y"),
                data_admissao=datetime.strptime("16-01-2018", "%d-%m-%Y"),
            ),
            Pessoa(
                nome="Enzo Nascimento",
                rg="68.986.227-4",
                cpf="356.759.355-25",
                data_nascimento=datetime.strptime("05-05-1989", "%d-%m-%Y"),
                data_admissao=datetime.strptime("23-08-2016", "%d-%m-%Y"),
            ),
            Pessoa(
                nome="Fabiana Moura",
                rg="69.437.526-9",
                cpf="149.992.262-00",
                data_nascimento=datetime.strptime("21-08-1995", "%d-%m-%Y"),
                data_admissao=datetime.strptime("26-03-2019", "%d-%m-%Y"),
            ),
        ]

        # Add data to the session and commit
        session.add_all(fixtures)
        session.commit()
