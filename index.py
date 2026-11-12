from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app =  FastAPI()

app.add_middleware( ##Importante para gestionar las conexiones con Google Appscript
    CORSMiddleware,
    allow_origins=[
        "https://script.google.com",
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_origin_regex=r"^https://(?:.*-)?script\.googleusercontent\.com$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Seleccionar el repository según el entorno:
#
#DB FALSA (pruebas locales):
#transaction_repository = repository.FakeTransactionRepository()

# POSTGRESQL (producción):
#connection = get_connection()
#transaction_repository = repository.PostgresTransactionRepository(connection)
#item_repository = item_repository_module.PostgresItemRepository(connection)

@app.get("/")
async def root():
    return "Hello World!, I'm CLAIMOS API :)"


######## Login session endpoints ########

# El endpoint recibe las credenciales mediante el cuerpo (body) de la petición HTTP
# y no mediante parámetros de la URL.
#
# LoginRequest es un modelo de Pydantic que define y valida la estructura del
# body recibido. En este caso, commerce_id debe ser un entero y password debe
# ser una cadena de texto.
#
# Por lo tanto, el cliente realiza una petición:
#
# POST /session/login/
#
# con un body JSON como:
#
# {
#     "commerce_id": 1,
#     "password": "Santiago!123"
# }
#
# Esto es preferible para un login porque las credenciales no forman parte de
# la URL. Los datos enviados como parámetros de path o query pueden quedar
# registrados en URLs, logs, historial del navegador u otras herramientas.
#
# FastAPI utiliza LoginRequest para validar automáticamente el body antes de
# ejecutar la función login(). Si los datos no cumplen con el modelo, la
# petición es rechazada y la función no continúa con la autenticación.
#
# Esta misma distinción debe revisarse al diseñar otros endpoints:
#
# - Path parameters: identifican un recurso dentro de la URL.
# - Query parameters: sirven principalmente para filtros, opciones o parámetros
#   de consulta.
# - Request body: contiene datos enviados al servidor para crear, modificar o
#   procesar información, especialmente cuando contienen estructuras más
#   complejas o datos que no deberían formar parte de la URL.
#
"""
import auth.sessionModels
from auth import sessionToken

@app.post("/session/login/")
async def login(data : auth.sessionModels.LoginRequest):
    from services.googleSheets import auth
    session = auth(data.nit, data.password)
    #print(sessionToken.activeSessions)
    return sendData("endpoint: /session/login/", session)


@app.post("/session/validate/")
async def validate(data : auth.sessionModels.vRequest):
    session = sessionToken.validate(data.commerce_id, data.token_value)
    return session

@app.post("/session/logout/")
async def logout(data: auth.sessionModels.vRequest):
    session = sessionToken.logout(data.commerce_id, data.token_value)
    return session
"""