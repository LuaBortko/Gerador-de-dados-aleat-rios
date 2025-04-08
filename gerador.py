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
        "Desenvolvimento Web", "Computação Móvel", "Big Data", "Sistemas Distribuídos",
        "Métodos Numéricos", "Equações Diferenciais Ordinárias", "Equações Diferenciais Parciais",
    "Cálculo Numérico", "Física Moderna", "Física Quântica para Engenharia",
    "Estatística e Probabilidade", "Análise Real", "Análise Complexa",
    "Instrumentação e Medidas", "Dinâmica de Sistemas Mecânicos", "Elementos de Máquinas",
    "Transferência de Calor", "Sistemas Térmicos", "Projeto Mecânico",
    "Máquinas Hidráulicas", "Eficiência Energética", "Engenharia Econômica",
    "Engenharia de Produção", "Engenharia de Controle", "Robótica Industrial",
    "Manutenção Industrial", "Engenharia de Requisitos", "Testes de Software",
    "Desenvolvimento de Aplicativos", "Interface Humano-Computador (IHC)",
    "Sistemas Embarcados", "Computação Quântica", "Computação Paralela", "Engenharia de Dados",
    "DevOps", "Análise de Dados", "Deep Learning", "Processamento de Linguagem Natural (PLN)",
    "Blockchain e Aplicações", "Internet das Coisas (IoT)", "Segurança Cibernética",
    "Empreendedorismo e Inovação", "Ética Profissional e Engenharia", "Comunicação Científica",
    "Design Thinking", "Sustentabilidade e Meio Ambiente", "Liderança e Trabalho em Equipe",
    "Propriedade Intelectual", "Metodologia Científica", "Projetos Interdisciplinares"]
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
##curs = {"id": None, "nome": None, "ra_coordenador": None}
##alun = {"ra": None, "nome": None, "id_curso": None}
##discip = {"id": None, "nome": None, "id_depart": None, "id_curso": None, "ra_coordenador": None}
##turm = {"id": None, "id_disciplina": None, "semestre": None, "ano": None, "periodo": None, "ra_professor": None}
##matri_cur = {"id_curso": None, "id_disciplina": None}
#hist = {"ra_aluno": None, "id_disciplina": None, "id_turma": None, "nota": None}
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
        elif "Ciencia" in nome:
            p = "C"
        else:
            p = "ADM"
        id = fake.numerify(text= p +'-%')
        while aux == 1:
            if id in ids:
                id = fake.numerify(text= p +'-%')
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
        id = fake.numerify(text='MT-%%%')
        while aux == 1:
            if id in ids:
                id = fake.numerify(text='MT-%%%')
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
        turm = {"id": id, "id_disciplina": None, "semestre": semestre, "ano": ano, "periodo": periodo, "ra_professor": None}
        turmas.append(turm)
    return turmas

def gerarMatrizCurricular(curso,disciplina, semestre):
    matri_cur = {"id_curso": curso, "id_disciplina": disciplina, "semestre": semestre}
    return matri_cur

def gerarHistorico(aluno,disc,turma,nota):
    hist = {"ra_aluno": aluno, "id_disciplina": disc, "id_turma": turma, "nota": nota}
    return hist

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

def gerarTCC_aluno(tcc,aluno):
    tcc_alun = {"id_tcc": tcc, "ra_aluno": aluno}
    return tcc_alun

#Main
n = int(input("Digite o numero de dados 1-8: "))
#gera o numero de departamentos e professores
l_aux = []
if n > 8:
    depart = gerarDepartamento(8)
else:
    depart = gerarDepartamento(n)
professores = gerarProfessor(n^2 + 2*n)
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
cursos = gerarCurso(randint(4,10))
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
alunos = gerarAlunos(n^2 + 4*n)
#Relação aluno e curso
for i in range(len(alunos)):
    if i < len(cursos):
        alunos[i]["id_curso"] = cursos[i]["id"]
    else:
        r = randint(0,len(cursos)-1)
        alunos[i]["id_curso"] = cursos[r]["id"]
#Criar as disciplinas
disciplinas = gerarDisciplina(3*len(cursos))
#Relações das disciplinas - curso
for i in range(len(disciplinas)):
    #relação com o departamento
    if i < len(depart):
        disciplinas[i]["id_depart"] = depart[i]["id"]
    else:
        r = randint(0,len(depart)-1)
        disciplinas[i]["id_depart"] = depart[r]["id"]
    #relação com o professor
    for j in range(len(professores)):
        if professores[j]["id_depart"] == disciplinas[i]["id_depart"]:
            l_aux.append(professores[j]["ra"])
    r2 =  randint(0,len(l_aux)-1)
    disciplinas[i]["ra_coordenador"] = l_aux[r2]
    l_aux.clear()
#Criação matriz
matrizes = []
for i in range(len(cursos)):
    curso = cursos[i]["id"]
    for j in range(randint(15, 20)):
        r = randint(0, len(disciplinas) - 1)
        disciplina = disciplinas[r]["id"]
        #vendo se ja tem essa disciplina nesse curso
        aux = 0
        while aux == 0:
            if disciplina in l_aux:
                r = randint(0, len(disciplinas) - 1)
                disciplina = disciplinas[r]["id"]
            else:
                aux = 1
        l_aux.append(disciplina)
        matrizes.append(gerarMatrizCurricular(curso,disciplina,randint(1,4)))
        disciplinas[r]["id_curso"] = curso
    l_aux.clear()
#Criação da turma
turmas = gerarTurma(len(disciplinas)*3)
#relações de turma
for i in range(len(turmas)):
    #relação turma e disciplina
    if i < len(disciplinas):
        turmas[i]["id_disciplina"] = disciplinas[i]["id"]
    else:
        r = randint(0,len(disciplinas)-1)
        turmas[i]["id_disciplina"] = disciplinas[r]["id"]
    #relação turma e professor
    if i < len(professores):
        turmas[i]["ra_professor"] = professores[i]["ra"]
    else:
        r = randint(0,len(professores)-1)
        turmas[i]["ra_professor"] = professores[r]["ra"]
#Criação históricos
historicos = []
# Relações histórico e tcc 
nAlunosTcc = 0
alunTcc = []
for i in range(len(alunos)):
    alunos[i]["id_curso"] = curso
    al_semestre = randint(1,4)
    for j in range(len(matrizes)):
        if matrizes[j]["id_curso"] == curso:
            semestre = matrizes[j]["semestre"]
            if al_semestre <= semestre:
                #print(turmas)
                for k in range(len(turmas)):
                    if turmas[k]["id_disciplina"] == matrizes[j]["id_disciplina"]:
                       l_aux.append(turmas[k]["id"]) 
                r = randint(0,len(l_aux)-1)
                historicos.append(gerarHistorico(alunos[i]["ra"],matrizes[j]["id_disciplina"],l_aux[r],randint(0,10)))
                l_aux.clear()
    if al_semestre == 4:
        nAlunosTcc =+ 1  
        alunTcc.append(alunos[i]["ra"])

#reprovação
for i in range(len(historicos)):
    historico = historicos[i]
    for j in range(len(turmas)):
        if historico["id_turma"] == turmas[j]["id"]:
            turma_atual = turmas[j] 
    aux = turma_atual["id"]
    id_aux = aux[3] + aux[4] + aux[5]  
    turma_atual["id"] = "DP-" + id_aux
    if turma_atual["semestre"] == "1º":
        turma_atual["semestre"] = "2º"
    else:
        turma_atual["semestre"] = "1º"
        turma_atual["ano"] += 1
    turmas.append(turma_atual)
    copia = gerarHistorico(historico["ra_aluno"],historico["id_disciplina"],turma_atual["id"],None)
    if historicos[i]["nota"] < 5:
        nota_nova = randint(5,10)
        copia["nota"] = nota_nova
        historicos.append(copia)
#TCC 
nTccs = int(nAlunosTcc/2)
tccs = gerarTCC(nTccs) 
for i in range(len(tccs)):
    r = randint(0,len(professores)-1)
    coordenador = professores[r]["ra"]
    aux = 0
    while aux == 0:
        if coordenador in l_aux:
            r = randint(0,len(professores)-1)
            coordenador = professores[r]["ra"]
        else:
            aux = 1
    
    tccs[i]["ra_professor"] = coordenador
l_aux.clear()
tccs_aluno = []
for i in range(len(tccs)):
    id_t = tccs[i]["id"]
    for j in range(randint(1,4)):
        r = randint(0,len(alunTcc)-1)
        aluno = alunTcc[r]
        tccs_aluno.append(gerarTCC_aluno(id_t,aluno))
        del alunTcc[r]
if len(alunTcc) != 0:
    for i in range(len(alunTcc)):
        r = randint(0,len(tccs)-1)
        tccs_aluno.append(gerarTCC_aluno(tccs[r]["id"],alunTcc[i]))


"""for j in range(len(cursos)):
    print("Curso: ",cursos[j]["id"])
    for i in range(len(matrizes)):
        if matrizes[i]["id_curso"] == cursos[j]["id"]:
            print(matrizes[i])

print(disciplinas)"""

print(tccs)
print("\n")
print(tccs_aluno)