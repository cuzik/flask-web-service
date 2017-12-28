-- Comandos de Criação de um Banco de Dados com os principais comados do mysql

-- Criação do Banco de Dados:
drop database store;
create database store DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;

-- Abrir um BD
use store

-- Criar tabelas dentro do BD aberto

-- Criar a tabela dos Usuários
create table product(
  prd_cod int unsigned not null auto_increment,
  prd_name varchar(100),
  prd_description varchar(100),
  prd_price float(10),
  prd_stock int,
  primary key (prd_cod)
) auto_increment=1;
