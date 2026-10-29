
# Documentação do Projeto de Engenharia de Sistemas A de 2026.1 

>Esta documentação está sujeita a alterações. Algumas pull requests (4 prs) que eu fiz ainda nao receberam aprovação, por isso as funcionalidades que elas implementam não estão descritas nesta documentação!


## 1. Visão Geral do Projeto

Este projeto consiste em um **Sistema de Gestão Curricular e Migração de Curso Universitário**, desenvolvido como parte da disciplina de **Engenharia de Sistemas A (2026.1)**.

A finalidade do sistema é gerenciar dados acadêmicos de estudantes, analisar seu histórico escolar, verificar o cumprimento dos componentes curriculares (disciplinas obrigatórias, optativas e horas complementares), validar pré-requisitos, mapear equivalências entre disciplinas antigas e novas e simular a migração de alunos entre diferentes matrizes curriculares.

---

## 2. Tecnologias Utilizadas

* **Linguagem de Programação:** Python 3 (Python 3.10 a 3.14)
* **Framework de Testes:** `pytest`
* **Leitura de Arquivos de Configuração:** `iniconfig`
* **Ambiente Virtual:** Python `venv`
* **Ferramenta de Gerenciamento de Pacotes:** `pip` / `flit` / `packaging`

---

## 3. Estrutura de Diretórios do Projeto

```text
Engenharia-de-Sistemas-A-2026.1/
│
├── __init__.py                       # Inicialização do pacote principal
├── disciplina.py                     # Representação de disciplinas individuais
├── componente_disciplina.py          # Tipos e estruturas de componentes curriculares
├── curriculo.py                      # Gestão de currículos e matrizes acadêmicas
├── validador_disciplinas.py          # Regras de validação de disciplinas e pré-requisitos
├── equivalencia.py                   # Mapeamento de equivalências entre disciplinas
├── verificar_desempenho.py           # Análise de notas, histórico e progresso do aluno
├── horas_complementares.py           # Contabilização de atividades complementares
├── simula_migracao.py                # Motor de simulação de migração entre currículos
├── Visualiza_Fluxograma.py           # Módulo de visualização do fluxo de disciplinas
│
├── testes/                           # Suite de testes automatizados
│   ├── __init__.py
│   ├── test_classificador.py         # Testes de classificação de disciplinas
│   ├── test_curriculo.py             # Testes de regras do currículo
│   ├── test_equivalencia.py          # Testes de equivalências de disciplinas
│   ├── test_horas_complementares.py  # Testes de validação de horas complementares
│   ├── test_simula_migracao.py       # Testes do fluxo de simulação de migração
│   └── test_validador_disciplinas.py # Testes dos validadores de requisitos
│
└── venv/                             # Ambiente virtual isolado usando em ambiente de desenvolvimento

```

---

## 4. Funcionalidades Implementadas

O projeto organiza suas funcionalidades em módulos orientados a objetos e funções especializadas:

### 4.1. Gestão de Disciplinas (`disciplina.py`)

* Cadastro de disciplinas contendo código, nome, carga horária, tipo (obrigatória/optativa) e pré-requisitos.
* Consulta e validação das propriedades essenciais das disciplinas.

### 4.2. Estruturação de Componentes Curriculares (`componente_disciplina.py`)

* Agrupamento de disciplinas em categorias específicas dentro da grade do curso.
* Definição da carga horária exigida por bloco temático ou período acadêmico.

### 4.3. Gestão de Currículo e Matriz Acadêmica (`curriculo.py`)

* Cadastro e manutenção de versões de matrizes curriculares (e.g., currículo antigo vs. currículo novo).
* Organização gráfica/conceitual dos períodos do curso.
* Cálculo do total de horas exigidas para a integralização do curso.

### 4.4. Validação e Verificação de Requisitos (`validador_disciplinas.py`)

* Checagem de cumprimento de pré-requisitos antes da matrícula/aproveitamento de disciplinas.
* Verificação do estado das disciplinas no histórico do aluno (Aprovado, Reprovado, Cursando, Dispensa).

### 4.5. Mapeamento de Equivalências (`equivalencia.py`)

* Configuração de regras de equivalência direta ($1 \to 1$) ou combinada ($M \to N$) entre disciplinas de currículos distintos.
* Conversão automática de créditos e disciplinas cursadas no currículo de origem para o currículo de destino.

### 4.6. Análise de Desempenho e Histórico Acadêmico (`verificar_desempenho.py`)

* Cálculo do Coeficiente de Rendimento (CR) ou Média Geral do estudante.
* Verificação da taxa de integralização do curso (porcentagem de disciplinas concluídas).

### 4.7. Controle de Horas Complementares (`horas_complementares.py`, `test_horas_complementares.py`)

* Registro e categorização de atividades complementares (pesquisa, extensão, eventos, monitoria).
* Validação do limite máximo aproveitável por categoria e cálculo do cumprimento da carga horária mínima exigida.

### 4.8. Simulação de Migração Curricular (`simula_migracao.py`, `test_simula_migracao.py`)

* Simulação completa da transição do aluno de um currículo antigo para um novo.
* Identificação automática de disciplinas aproveitadas por equivalência.
* Geração do saldo de pendências para o aluno no novo currículo.

### 4.9. Visualização de Fluxograma (`Visualiza_Fluxograma.py`)

* Interface/recurso visual para exibição da distribuição temporal e sequencial das disciplinas ao longo dos semestres.

---

## 5. Suíte de Testes Automatizados (`testes/`)

O projeto utiliza o **Pytest** para garantir a integridade das regras de negócio. A cobertura de testes contempla:

* **`test_classificador.py`:** Testes das regras de classificação de componentes e categorias de disciplinas.
* **`test_curriculo.py`:** Validação da montagem da grade e integridade do currículo.
* **`test_equivalencia.py`:** Validação dos casos de equivalência simples e composta.
* **`test_horas_complementares.py`:** Testes dos limites e contabilização de atividades acadêmicas.
* **`test_simula_migracao.py`:** Testes de ponta a ponta do processo de simulação de troca de matriz curricular.
* **`test_validador_disciplinas.py`:** Validação do cumprimento de pré-requisitos e status acadêmicos.