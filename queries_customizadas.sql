--01. Encontre os nomes de todos os estudantes.
--SELECT nome
--FROM aluno

--02. Encontre os nomes de todos os estudantes que cursaram algum curso
--1º ver cursos disponiveis e escolher um : ENG-4
--Select id
--From curso
--2º procurar os alunos que estão nesse curso
--SELECT nome
--FROM aluno WHERE id_curso = 'ENG-4'

--03.Liste os IDs dos professores que ensinam mais de uma disciplina.
--SELECT p.ra AS professor,count(t.id_disciplina) AS materias
--FROM professor p
--INNER JOIN turma t ON p.ra = t.ra_professor
--GROUP BY p.ra
--HAVING count(id_disciplina) > 1 

--04. Liste disciplinas que foram coordenadas pelos professores ra1 e 'ra2.
--select ra from professor ra1: 12.148.875-6 ra2: 12.117.777-5 --Descobrir os professores existentes
--SELECT d.id AS disciplina, p.nome AS professor, p.ra AS professor_ra
--FROM disciplina AS d
--INNER JOIN professor p
--  ON d.ra_coordenador = p.ra
--WHERE p.ra = '12.148.875-6' OR p.ra = '12.117.777-5'

--05.Liste todos as disciplinas que foram cursados por estudantes do curso "Ciencia de Dados".
--select nome from curso -- Descobrir os cursos existentes
--SELECT c.nome AS Curso, m.id_disciplina AS id_disciplina, d.nome AS disciplina 
--FROM curso c
--INNER JOIN matriz_curricular m
--  ON m.id_curso = c.id
--INNER JOIN disciplina d
--  ON d.id = m.id_disciplina
--WHERE c.nome = 'Ciencia de Dados'

--06.Recupere os nomes dos estudantes que cursaram disciplinas do departamento de "matematica".
--select nome from departamento -- Descobrir os departamentos existentes
--SELECT dep.nome AS Departamento, d.id AS Disciplina, a.nome AS aluno
--FROM disciplina d
--INNER JOIN departamento dep
--  ON d.id_departamento = dep.id
--INNER JOIN turma t
--  ON t.id_disciplina = d.id
--INNER JOIN historico h
--  ON h.id_turma = t.id
--INNER JOIN aluno a
--  ON a.ra = h.ra_aluno
--WHERE dep.nome = 'matematica'

--07.Encontre os professores que ensinam em 2020
--SELECT p.nome AS professor,d.id AS Diciplina, t.ano AS Ano
--FROM professor p
--INNER JOIN turma t
--  ON t.ra_professor = p.ra
--INNER JOIN disciplina d
--  ON d.id = t.id_disciplina
--WHERE t.ano = '2020' 

--08.Liste os professores e quantas turmas eles ministram.
--SELECT p.nome AS professor, count(t.id) AS qtde_turmas
--FROM professor p
--INNER JOIN turma t
--  ON t.ra_professor = p.ra
--GROUP BY p.nome
--HAVING count(t.id) > 0

--09. Encontre cursos com mais de 10 disciplinas
--SELECT c.nome AS Curso, count(m.id_disciplina) AS qtde_disciplinas
--FROM curso c
--INNER JOIN matriz_curricular m
--  ON m.id_curso = c.id
--group BY c.nome
--HAVING count(m.id_disciplina) > 10

--10.Mostre os TCCs e o professor coordenador de cada tcc
--SELECT nome, ra_professor AS Professor_Coordenador
--FROM tcc


--Mostre todo o histórico escolar de um aluno que teve reprovação em uma disciplina, retornando inclusive a reprovação em um semestre e a aprovação no semestre seguinte;
--SELECT distinct t.ano,t.semestre,h.id_turma,h.id_disciplina,h.nota from historico as h
--INNER JOIN turma t ON t.id_disciplina = h.id_disciplina
--WHERE h.ra_aluno = '24.112.641-4'
--ORDER BY id_disciplina;

--Mostre todos os TCCs orientados por um professor junto com os nomes dos alunos que fizeram o projeto
--SELECT distinct a.nome,t.id_tcc from tcc_aluno as t
--INNER JOIN aluno a ON t.ra_aluno = a.ra
--INNER JOIN tcc tt ON tt.ra_professor = '12.816.681-7'
--ORDER BY t.id_tcc;
