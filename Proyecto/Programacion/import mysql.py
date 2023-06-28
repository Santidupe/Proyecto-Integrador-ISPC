import mysql.connector


class Bases:
    # Conexion a la base de datos
    def __init__(self):
        self.conexion = None
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="dupe",
                database="proyectointegrador",
                raise_on_warnings=True
            )
            print("Conexión correcta")
            self.cursor = self.conexion.cursor()
            self.verificar_tablas()
        except mysql.connector.Error as e:
            print("Ocurrió un error al conectar:", e)         
            
     #  Verifico si existen las tablas, en caso de no existir las creo
    def verificar_tablas(self):
        self.cursor.execute("SHOW TABLES LIKE 'Dispositivos_Iot'")
        table_exists = self.cursor.fetchone()
        if table_exists:
            print("La tabla Dispositivos_Iot ya existe.")
        else:
            self.crear_tabla_dispositivos_iot()
        
        self.cursor.execute("SHOW TABLES LIKE 'Est_dispositivos'")
        table_exists = self.cursor.fetchone()
        if table_exists:
            print("La tabla Est_dispositivos ya existe.")
        else:
            self.crear_tabla_est_dispositivos()

        self.agregar_relacion()
        
    # Creo tabla Dispositivos_iot
    def crear_tabla_dispositivos_iot(self):
        self.cursor.execute("""
            CREATE TABLE Dispositivos_Iot (
                Ind_dispositivos INT AUTO_INCREMENT,
                Mod_dispositivos VARCHAR(20),
                Nserie_dispositivos VARCHAR(25),
                Direcc_dispositivos VARCHAR(40),
                FInst_disp DATE,
                Coordenadas_disp VARCHAR(20),
                Est_disp INT,
                PRIMARY KEY (Ind_dispositivos),
                UNIQUE KEY (Nserie_dispositivos)
            )
        """)
        print("La tabla Dispositivos_Iot ha sido creada.")

    # Creo la tabla estados
    def crear_tabla_est_dispositivos(self):
        self.cursor.execute("""
            CREATE TABLE Est_dispositivos (
                Nr_estado INT,
                Desc_estado VARCHAR(20),
                PRIMARY KEY (Nr_estado)
            )
        """)
        print("La tabla Est_dispositivos ha sido creada.")
    
    # Agrego la relacion entre las tablas
    def agregar_relacion(self):
        self.cursor.execute("SHOW CREATE TABLE Dispositivos_Iot")
        table_definition = self.cursor.fetchone()[1]
        if "fk_Est_disp" not in table_definition:
            self.cursor.execute("""
                ALTER TABLE Dispositivos_Iot
                ADD CONSTRAINT fk_Est_disp
                FOREIGN KEY (Est_disp) REFERENCES Estados_disp(Nr_estado)
            """)
            print("La relación entre las tablas Dispositivos_Iot y Est_dispositivos ha sido creada.")
            
    # En caso de que las tablas esten vacías inserto un registro en blanco para que no de error la consulta 
    def verificar_registros(self):
        self.cursor.execute("SELECT COUNT(*) FROM Dispositivos_Iot")
        count = self.cursor.fetchone()[0]
        if count == 0:
            self.cursor.execute("INSERT INTO Dispositivos_Iot (Mod_dispositivos, Nserie_dispositivos, Direcc_dispositivos, FInst_disp, Coordenadas_disp, Est_disp) VALUES ('', '', '', '', '', 0)")
            self.conexion.commit()
        
        self.cursor.execute("SELECT COUNT(*) FROM Est_dispositivos")
        count = self.cursor.fetchone()[0]
        if count == 0:
            self.cursor.execute("INSERT INTO Est_dispositivos (Nr_estado, Desc_estado) VALUES (0, '')")
            self.conexion.commit()
    
    # Creo dispositivo nuevo
    def crear_dispositivo(self, mod_disp, nserie_disp, direcc_disp, finst_disp, coordenadas_disp, est_disp):
        consulta = "INSERT INTO Dispositivos_Iot (Mod_dispositivos, Nserie_dispositivos, Direcc_dispositivos, FInst_disp, Coordenadas_disp, Est_disp) VALUES (%s, %s, %s, %s, %s, %s)"
        datos = (mod_disp, nserie_disp, direcc_disp, finst_disp, coordenadas_disp, est_disp)
        self.cursor.execute(consulta, datos)
        self.conexion.commit()
        print("Dispositivo creado con éxito.")
    
    # Consulta de dispositivos en las bases de datos
    #def obtener_dispositivos(self):
    #    consulta = "SELECT * FROM Dispositivos_Iot"
    #    self.cursor.execute(consulta)
    #    dispositivos = self.cursor.fetchall()
    #    for dispositivo in dispositivos:
    #     print(dispositivo)
    def obtener_dispositivos(self):
        consulta = "SELECT * FROM Dispositivos_Iot"
        self.cursor.execute(consulta)
        dispositivos = self.cursor.fetchall()
        # Limpio la pantalla
        # limpiar_pantalla()
        # Imprimo el encabezado
        print("ID | Modelo | Número de Serie | Dirección | Fecha de Instalación | Coordenadas | Estado")
        # Imprimo los dispositivos
        contador = 0
        for dispositivo in dispositivos:
            print(f"{dispositivo[0]} | {dispositivo[1]} | {dispositivo[2]} | {dispositivo[3]} | {dispositivo[4]} | {dispositivo[5]} | {dispositivo[6]}")
            contador += 1
            # Verificar si se han mostrado 20 registros
            # Verificar si se han mostrado 20 registros o se ha llegado al final
            if contador % 20 == 0 or contador == len(dispositivos):
                input("Presiona cualquier tecla para continuar...")
                # Limpia la pantalla (opcional)
                # En la proxima modificacion pegar el codigo para limpiar la pantalla
            # if contador % 20 == 0:
            #    input("Presiona cualquier tecla para continuar...")
            
    # Actualizo el dispositivo (Lo modifico)
    def actualizar_dispositivo(self, ind_dispositivos, direcc_dispositivos, mod_dispositivos, nserie_dispositivos, finst_disp, coordenadas_disp, est_disp):
        consulta = "UPDATE Disp_Iot SET Mod_disp = %s, Nserie_disp = %s, Direcc_disp = %s, FInst_disp = %s, Coordenadas_disp = %s, Est_disp = %s WHERE Ind_disp = %s"
        datos = (mod_dispositivos, nserie_dispositivos, direcc_dispositivos, ind_dispositivos, finst_disp, coordenadas_disp, est_disp)
        self.cursor.execute(consulta, datos)
        self.conexion.commit()
        print("El dispositivo ha sido actualizado con éxito.")
    
    # Elimino el dispositivo
    def eliminar_dispositivo(self, ind_dispositivos):
        consulta = "DELETE FROM Dispositivos_Iot WHERE Ind_dispositivos = %s"
        datos = (ind_dispositivos,)
        self.cursor.execute(consulta, datos)
        self.conexion.commit()
        print("El dispositivo ha sido eliminado con éxito.")