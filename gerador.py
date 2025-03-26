from faker import Faker
from faker.providers import DynamicProvider

fake = Faker('pt_BR')
departamentos = DynamicProvider(
    provider_name = "departamento_provider", elements = ["matematica", "computaçao", "civil", "eletrica", "fisica", "producao", "ciencias sociais", "quimica"]
)

cursos = DynamicProvider(
    provider_name = "curso_provider", elements = ["Eng. Eletrica","Eng. Mecanica", "Eng. Quimica", "Administração", "Eng. Automação", "Eng. de Materiais", "Eng. Robos", "Ciencia da Computação", "Ciencia de Dados", "Eng. de Produção"]
)

disciplinas = DynamicProvider(
    provider_name = "disciplina_provider", elements = ["Cálculo I", "Cálculo II", "Cálculo III", "Álgebra Linear", "Geometria Analítica",
        "Física I", "Física II", "Física III", "Química Geral", "Mecânica dos Sólidos",
        "Resistência dos Materiais", "Mecânica dos Fluidos", "Termodinâmica", "Eletromagnetismo",
        "Circuitos Elétricos", "Eletrônica", "Processos de Fabricação", "Engenharia de Materiais",
        "Sistemas Dinâmicos", "Controle e Automação", "Hidráulica", "Pneumática",
        "Gestão de Projetos", "Segurança do Trabalho", "Desenho Técnico", "Ciência dos Materiais",
        "Algoritmos e Estruturas de Dados", "Programação Orientada a Objetos", "Banco de Dados",
        "Sistemas Operacionais", "Redes de Computadores", "Compiladores", "Engenharia de Software",
        "Inteligência Artificial", "Aprendizado de Máquina", "Visão Computacional",
        "Criptografia e Segurança", "Computação Gráfica", "Arquitetura de Computadores",
        "Teoria da Computação", "Matemática Discreta", "Computação em Nuvem",
        "Desenvolvimento Web", "Computação Móvel", "Big Data", "Sistemas Distribuídos"]
)

fake.add_provider(departamentos)
fake.add_provider(cursos)
fake.add_provider(disciplinas)

#depart = {"id": None, "nome": None, "ra_coodernador": None}
#prof = {"ra": None, "nome": None, "id_depart": None}
#curs = {"id": None, "nome": None, "ra_coordenador": None}
#alun = {"ra": None, "nome": None, "id_curso": None}
#discip = {"id": None, "nome": None, "id_depart": None, "id_curso": None, "ra_coordenador": None}
turm = {"id": None, "id_diciplina": None, "semestre": None, "ano": None, "periodo": None, "ra_professor": None}
tc_c = {"id": None, "nome": None, "ra_professor": None}
tcc_alun = {"id_tcc": None, "ra_aluno": None}
matri_cu = {"id_curso": None, "id_diciplina": None}
hist = {"ra_aluno": None, "id_diciplina": None, "id_turma": None, "nota": None}

def gerarDepartamento(n):
    deptos = []
    nomes = []
    ids = []
    for i in range(n):
        aux = 1
        aux1 = 1 
        nome = fake.departamento_provider()
        while aux == 1:
            if nome in nomes:
                nome = fake.departamento_provider()
            else:
                aux = 0
        cod = fake.numerify(text='DE-%%%')

        while aux1 == 1:
            if cod in ids:
                cod = fake.numerify(text='DE-%%%')
            else:
                aux1 = 0
        depart = {"id": cod, "nome": nome, "ra_coodernador": None}
        nomes.append(nome)
        ids.append(cod)
        deptos.append(depart)
    return deptos

def gerarProfessor(n):
    profs = []
    ras = []
    nomes = []
    for i in range(n):
        aux = 1
        aux1 = 1
        ra = fake.numerify(text='12.%%%.%%%-%')
        while aux == 1:
            if ra in ras:
                ra = fake.numerify(text='12.%%%.%%%-%')
            else:
                aux = 0
        
        n1 = fake.first_name()
        n2 = fake.last_name()
        nome = n1 + " " + n2
        while aux1 == 1:
            if nome in nomes:
                nome = fake.name()
            else:
                aux1 = 0
        prof = {"ra": ra, "nome": nome, "id_depart": None}
        nomes.append(nome)
        ras.append(ra)
        profs.append(prof)
    return profs

def gerarCurso(n):
    cursos = []
    ids = []
    nomes = []
    for i in range(n):
        aux = 1
        aux1 =  1
        id = fake.numerify(text='CU-%%%')
        while aux == 1:
            if id in ids:
                id = fake.numerify(text='CU-%%%')
            else:
                aux = 0
        nome = fake.curso_provider()
        while aux1 == 1:
            if nome in nomes:
                nome = fake.curso_provider()
            else:
                aux1 = 0
        nomes.append(nome)
        ids.append(id)
        curs = {"id": id, "nome": nome, "ra_coordenador": None}
        cursos.append(curs)
    return cursos
        
def gerarAlunos(n):
    alunos = []
    ras = []
    nomes = []
    for i in range(n):
        aux = 1
        aux1 = 1
        ra = fake.numerify(text='24.%%%.%%%-%')
        while aux == 1:
            if ra in ras:
                ra = fake.numerify(text='24.%%%.%%%-%')
            else:
                aux = 0
        
        n1 = fake.first_name()
        n2 = fake.last_name()
        nome = n1 + " " + n2
        while aux1 == 1:
            if nome in nomes:
                nome = fake.name()
            else:
                aux1 = 0
        aluno = {"ra": ra, "nome": nome, "id_curso": None}
        nomes.append(nome)
        ras.append(ra)
        alunos.append(aluno)
    return alunos

def gerarDisciplina(n):
    discips = []
    nomes = []
    ids = []
    for i in range(n):
        aux = 1
        aux1 =  1
        id = fake.numerify(text='DI-%%%')
        while aux == 1:
            if id in ids:
                id = fake.numerify(text='DI-%%%')
            else:
                aux = 0
        nome = fake.disciplina_provider()
        while aux1 == 1:
            if nome in nomes:
                nome = fake.disciplina_provider()
            else:
                aux1 = 0
        nomes.append(nome)
        ids.append(id)
        discip = {"id": id, "nome": nome, "id_depart": None, "id_curso": None, "ra_coordenador": None}
        discips.append(discip)
    return discips

def gerarTurma(n):
    turmas = []
    


dep = gerarDepartamento(4)
#print(dep)
prof = gerarProfessor(6)
#print(prof)
curs = gerarCurso(5)
#print(curs)
alun = gerarAlunos(10)
#print(alun)
discip = gerarDisciplina(6)
print(discip)

