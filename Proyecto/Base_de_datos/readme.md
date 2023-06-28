### Verifico si la base de datos existe

SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'proyectointegradorv';

### Si la base de datos no existe, creo la base proyectointegrador

CREATE DATABASE IF NOT EXISTS proyectointegrador;


### Abro la base de datos ProyectoIntegrador

USE proyectointegrador;

### Verifico si existe la tabla, en caso contrario la creo con el nombre Dispositivos_Iot

CREATE TABLE if not exists Dispositivos_Iot (
  Nserie_dispositivos VARCHAR(25),
  
  Direcc_dispositivos VARCHAR(40),
  
  Ind_dispositivos INT AUTO_INCREMENT,
  
  Mod_dispositivos VARCHAR(20),
  
  FInst_disp DATE,
  
  Coordenadas_disp VARCHAR(20),
  
  Est_disp INT,
  
  PRIMARY KEY (Ind_dispositivos),
  
  UNIQUE KEY (Nserie_dispositivos)
);


### Verifico si existe y en caso contrario creo tabla Est_dispositivos

CREATE TABLE if not exists Est_dispositivos (
  Nr_estado INT,
  
  Desc_estado VARCHAR(20),
  
  PRIMARY KEY (Nr_estado)
);


### Agrego relación entre las tablas Dispositivos_Iot y Est_dispositivos

ALTER TABLE Dispositivos_Iot

  ADD CONSTRAINT fk_Est_disp
  
  FOREIGN KEY (Est_disp) REFERENCES Est_dispositivos(Nr_estado);

### Inserto valores a tabla est_dispositivos, columna Nr_estados

insert into proyectointegrador.est_dispositivos(Nr_estado)
  values (2012);
