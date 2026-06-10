CREATE DATABASE IF NOT EXISTS banco_rh;
USE banco_rh;

CREATE TABLE IF NOT EXISTS administradores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL,
    senha VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS departamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    gerente VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS cargos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    salario_base DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS funcionarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    email VARCHAR(100),
    telefone VARCHAR(20),
    cargo_id INT,
    salario DECIMAL(10, 2),
    departamento_id INT,
    data_admissao DATE,
    FOREIGN KEY (cargo_id) REFERENCES cargos(id),
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);

CREATE TABLE IF NOT EXISTS logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50),
    acao TEXT,
    data_hora DATETIME
);

-- Inserir dados iniciais
INSERT INTO administradores (usuario, senha) VALUES ('admin', 'admin123');

INSERT INTO departamentos (nome, gerente) VALUES ('TI', 'Carlos Silva');
INSERT INTO departamentos (nome, gerente) VALUES ('RH', 'Ana Souza');
INSERT INTO departamentos (nome, gerente) VALUES ('Financeiro', 'Roberto Santos');

INSERT INTO cargos (nome, salario_base) VALUES ('Desenvolvedor Python', 5000.00);
INSERT INTO cargos (nome, salario_base) VALUES ('Analista de Sistemas', 4500.00);
INSERT INTO cargos (nome, salario_base) VALUES ('Gerente de Projetos', 8000.00);
