from flask import Flask, render_template
from Model.connection import Connection
from Controller.teacherManagementController import teacher_blueprint
from Controller.mainController import main_bp
from Controller.subjectManagementController import subject_bp
from Controller.competenceManagementController import competence_bp
from Controller.learningOutcomeManagementController import learning_outcome_bp
from Controller.integrationController import integration_bp
from Controller.authController import auth_blueprint



# Inicializacion de la aplicacion Flask
app = Flask(__name__)  
# Clave secreta
app.secret_key = 'mysecretkey'  # Necesario para usar 'flash'

# Inicialización de la conexión MySQL ANTES de definir las rutas
db = Connection.init_database(app)  # Obtiene el objeto db

# Configuración e inicialización de JWT
jwt = Connection.config_JWT(app)  # Obtiene el objeto `jwt`

#Registro de los controladores
app.register_blueprint(main_bp) #Controlador de la pagina principal

#Controlador de la gestion de asignaturas
app.register_blueprint(subject_bp, url_prefix='/subject')
#Controlador de la gestion de competencias
app.register_blueprint(competence_bp,url_prefix='/competence')
#Controlador de la gestion de RA
app.register_blueprint(learning_outcome_bp,url_prefix='/learning_outcome')
#Controlador de la gestion de docentes
app.register_blueprint(teacher_blueprint, url_prefix='/teacher')
#Controlador de la integracion asignatura-competencia-docente
app.register_blueprint(integration_bp, url_prefix='/asign')
#Controlador de autentificacion
app.register_blueprint(auth_blueprint, url_prefix='/auth')

#Comprobar que el archivo que se esta ejecutando es el principal
if __name__ == '__main__':
    app.run(debug=True, port=3000)  # debug = true, actualiza cada vez que hacemos cambios en el servidor
