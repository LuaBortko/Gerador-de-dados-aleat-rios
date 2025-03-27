from faker import Faker
from faker.providers import DynamicProvider
from random import randint

fake = Faker('pt_BR')
departamentos = DynamicProvider(
    provider_name = "departamento_provider", elements = ["matematica", "computaçao", "civil", "eletrica", "fisica", "producao", "ciencias sociais", "quimica"]
)
#8
cursos = DynamicProvider(
    provider_name = "curso_provider", elements = ["Eng. Eletrica","Eng. Mecanica", "Eng. Quimica", "Administração", "Eng. Automação", "Eng. de Materiais", "Eng. Robos", "Ciencia da Computação", "Ciencia de Dados", "Eng. de Produção"]
)
#10
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

periodos = DynamicProvider(
    provider_name = "periodo_provider", elements = ["diurno" ,"vespertino", "noturno"]
)

semestres = DynamicProvider(
    provider_name = "semestre_provider", elements = ["1º","2º"]
)

tccs = DynamicProvider(
    provider_name = "tcc_provider", elements = ["Análise e Otimização de Processos Industriais com Inteligência Artificial",
        "Desenvolvimento de Materiais Sustentáveis para Construção Civil",
        "Aplicação da Internet das Coisas (IoT) em Sistemas de Automação Residencial",
        "Modelagem Computacional de Estruturas para Prevenção de Colapsos",
        "Estudo de Energias Renováveis: Viabilidade de Painéis Solares em Ambientes Urbanos",
        "Impacto da Impressão 3D na Engenharia de Produção",
        "Desenvolvimento de um Veículo Elétrico de Baixo Custo para Mobilidade Urbana",
        "Aplicação da Engenharia de Materiais na Indústria Aeroespacial",
        "Sistemas de Gestão de Manutenção Preditiva com Aprendizado de Máquina",
        "Desenvolvimento de um Sistema Inteligente para Monitoramento de Barragens",
        "Desenvolvimento de um Algoritmo de Machine Learning para Diagnóstico Médico",
        "Análise de Segurança Cibernética em Aplicações Web",
        "Desenvolvimento de um Assistente Virtual Baseado em Processamento de Linguagem Natural",
        "Blockchain: Aplicações Além das Criptomoedas",
        "Criação de um Sistema de Recomendação Usando Redes Neurais",
        "Automação de Testes de Software com Inteligência Artificial",
        "Desenvolvimento de um Jogo Educacional para Ensino de Programação",
        "Uso de Visão Computacional para Identificação de Placas de Trânsito",
        "Desenvolvimento de um Chatbot para Atendimento ao Cliente",
        "Computação Quântica: Algoritmos e Perspectivas Futuras"]
)

fake.add_provider(tccs)
fake.add_provider(departamentos)
fake.add_provider(cursos)
fake.add_provider(disciplinas)
fake.add_provider(periodos)
fake.add_provider(semestres)

##depart = {"id": None, "nome": None, "ra_coodernador": None}
##prof = {"ra": None, "nome": None, "id_depart": None}
#curs = {"id": None, "nome": None, "ra_coordenador": None}
#alun = {"ra": None, "nome": None, "id_curso": None}
#discip = {"id": None, "nome": None, "id_depart": None, "id_curso": None, "ra_coordenador": None}
#turm = {"id": None, "id_diciplina": None, "semestre": None, "ano": None, "periodo": None, "ra_professor": None}
#matri_cur = {"id_curso": None, "id_diciplina": None}
#hist = {"ra_aluno": None, "id_diciplina": None, "id_turma": None, "nota": None}
#tc_c = {"id": None, "nome": None, "ra_professor": None}
#tcc_alun = {"id_tcc": None, "ra_aluno": None}

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
        nome = fake.curso_provider()
        while aux1 == 1:
            if nome in nomes:
                nome = fake.curso_provider()
            else:
                aux1 = 0
        if "Eng" in nome:
            p = "ENG"
        elif nome == "Ciencia da Computação":
            p = "C"
        elif nome == "Ciencia de Dados":
            p = "C"
        else:
            p = "ADM"
        id = fake.numerify(text= p +'-%%%')
        while aux == 1:
            if id in ids:
                id = fake.numerify(text= p +'-%%%')
            else:
                aux = 0
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
    ids = []
    for i in range(n):
        aux = 1
        periodo = fake.periodo_provider()
        if periodo == "noturno":
            p = "NO"
        elif periodo == "vespertino":
            p = "VE"
        else:
            p = "DI"
        id = fake.numerify(text= p + '-%%%')
        while aux == 1:
            if id in ids:
                id = fake.numerify(text= p + '-%%%')
            else:
                aux = 0
        ano = randint(2015,2025)
        semestre = fake.semestre_provider()
        ids.append(id)
        turm = {"id": id, "id_diciplina": None, "semestre": semestre, "ano": ano, "periodo": periodo, "ra_professor": None}
        turmas.append(turm)
    return turmas

def gerarMatrizCurricular(n):
    matrizes_curriculares = []
    for i in range(n):
        matri_cur = {"id_curso": None, "id_diciplina": None}
        matrizes_curriculares.append(matri_cur)
    return matrizes_curriculares

def gerarHistorico(n):
    historicos = []
    for i in range(n):
        nota = randint(0,10)
        hist = {"ra_aluno": None, "id_diciplina": None, "id_turma": None, "nota": nota}
        historicos.append(hist)
    return historicos

def gerarTCC(n):
    tccs = []
    ids = []
    nomes = []
    for i in range(n):
        aux = 1
        aux1 = 1
        id = fake.numerify(text='TCC-%%%%')
        while aux == 1:
            if id in ids:
                id = fake.numerify(text='TCC-%%%%')
            else:
                aux = 0
        
        nome = fake.tcc_provider()
        while aux1 == 1:
            if nome in nomes:
                nome = fake.tcc_provider()
            else:
                aux1 = 0
        tc_c = {"id": id, "nome": nome, "ra_professor": None}
        nomes.append(nome)
        ids.append(id)
        tccs.append(tc_c)
    return tccs

def gerarTCC_aluno(n):
    tccs_a = []
    for i in range(n):
        tcc_alun = {"id_tcc": None, "ra_aluno": None}
        tccs_a.append(tcc_alun)
    return tccs_a

#Main
n = int(input("Digite o numero de dados 1-8: "))
#gera o numero de departamentos e professores
l_aux = []
if n > 8:
    depart = gerarDepartamento(8)
else:
    depart = gerarDepartamento(n)
professores = gerarProfessor(n^2 + 4*n)
#relação departamento - professor
for i in range(len(depart)):
    aux = 1
    r = randint(0,len(professores)-1)
    coord_dep = professores[r]["ra"]
    while aux == 1:
        if coord_dep in l_aux:
            r = randint(0,len(professores)-1)
            coord_dep = professores[r]["ra"]
        else:
            aux = 0
    depart[i]["ra_coodernador"] = coord_dep
    professores[r]["id_depart"] = depart[i]["id"]
    l_aux.append(coord_dep) # no momento guarda ra dos professores coordenadores de depart 
l_aux.clear()
#relação professor - departamento
for i in range(len(professores)):
    if professores[i]["id_depart"] == None:
        r = randint(0,len(depart)-1)
        professores[i]["id_depart"] = depart[r]["id"]
#Criação de cursos
cursos = gerarCurso(randint(2,10))
#Relaçao curso e professor
for i in range(len(cursos)):
    aux = 1
    r = randint(0,len(professores)-1)
    coord_cu = professores[r]["ra"]
    while aux == 1:
        if coord_cu in l_aux:
            r = randint(0,len(professores)-1)
            coord_cu = professores[r]["ra"]
        else:
            aux = 0
    cursos[i]["ra_coordenador"] = coord_cu
    l_aux.append(coord_cu)
l_aux.clear()
#criação do aluno
alunos = gerarAlunos(n^3 + 8*n)
#Relação aluno e curso
for i in range(len(alunos)):
    if i < len(cursos):
        alunos[i]["id_curso"] = cursos[i]["id"]
    else:
        r = randint(0,len(cursos)-1)
        alunos[i]["id_curso"] = cursos[r]["id"]
#

print("Departamentos:\n")
print(depart)
print("\nProfessores:\n")
print(professores)
print("\nCursos:\n")
print(cursos)
print("\n")
print("Alunos:")
print("\n")
print(alunos)
