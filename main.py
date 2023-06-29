from fastapi import FastAPI
from pymongo import MongoClient
from bson import json_util

# Подключение к MongoDB
client = MongoClient('mongodb://root:password@localhost:27017')

# Выбор базы данных
db = client['mydatabase']

# Коллекция "kishi_juz_taipalar"
kishi_juz_taipalar_collection = db['kishi_juz_taipalar']

# Коллекция "kishi_juz_rular"
kishi_juz_rular_collection = db['kishi_juz_rular']

# Коллекция "orta_juz_taipalar"
orta_juz_taipalar_collection = db['orta_juz_taipalar']

# Коллекция "orta_juz_rular"
orta_juz_rular_collection = db['orta_juz_rular']

# Коллекция "uly_juz_taipalar"
uly_juz_taipalar_collection = db['uly_juz_taipalar']

# Коллекция "uly_juz_rular"
uly_juz_rular_collection = db['uly_juz_rular']

# Создание экземпляра FastAPI
app = FastAPI()


# Маршрут для получения всех записей из коллекции "kishi_juz_taipalar"
@app.get('/kishi_juz/taipalar')
def get_kishi_juz_taipalar():
    taipalar = kishi_juz_taipalar_collection.find()
    return {'taipalar': bson_to_json(taipalar)}


# Маршрут для получения всех записей из коллекции "kishi_juz_rular"
@app.get('/kishi_juz/rular')
def get_kishi_juz_rular():
    rular = kishi_juz_rular_collection.find().sort('name')
    return {'rular': bson_to_json(rular)}


# Маршрут для создания новой записи в коллекции "kishi_juz_taipalar"
@app.post('/kishi_juz/taipalar')
def create_kishi_juz_taipa(taipa: str):
    taipa_data = {'taipa': taipa}
    taipa_id = kishi_juz_taipalar_collection.insert_one(taipa_data).inserted_id
    return {'taipa_id': str(taipa_id)}


# Маршрут для создания новой записи в коллекции "kishi_juz_rular"
@app.post('/kishi_juz/rular')
def create_kishi_juz_rular(taipa_id: str, name: str, description: str, picture: str):
    rular_data = {
        'taipa_id': taipa_id,
        'name': name,
        'description': description,
        'picture': picture
    }
    rular_id = kishi_juz_rular_collection.insert_one(rular_data).inserted_id
    return {'rular_id': str(rular_id)}


# Маршрут для получения всех записей из коллекции "orta_juz_taipalar"
@app.get('/orta_juz/taipalar')
def get_orta_juz_taipalar():
    taipalar = orta_juz_taipalar_collection.find()
    return {'taipalar': bson_to_json(taipalar)}


# Маршрут для получения всех записей из коллекции "orta_juz_rular"
@app.get('/orta_juz/rular')
def get_orta_juz_rular():
    rular = orta_juz_rular_collection.find().sort('name')
    return {'rular': bson_to_json(rular)}


# Маршрут для создания новой записи в коллекции "orta_juz_taipalar"
@app.post('/orta_juz/taipalar')
def create_orta_juz_taipa(taipa: str):
    taipa_data = {'taipa': taipa}
    taipa_id = orta_juz_taipalar_collection.insert_one(taipa_data).inserted_id
    return {'taipa_id': str(taipa_id)}


# Маршрут для создания новой записи в коллекции "orta_juz_rular"
@app.post('/orta_juz/rular')
def create_orta_juz_rular(taipa_id: str, name: str, description: str, picture: str):
    rular_data = {
        'taipa_id': taipa_id,
        'name': name,
        'description': description,
        'picture': picture
    }
    rular_id = orta_juz_rular_collection.insert_one(rular_data).inserted_id
    return {'rular_id': str(rular_id)}


# Маршрут для получения всех записей из коллекции "uly_juz_taipalar"
@app.get('/uly_juz/taipalar')
def get_uly_juz_taipalar():
    taipalar = uly_juz_taipalar_collection.find()
    return {'taipalar': bson_to_json(taipalar)}


# Маршрут для получения всех записей из коллекции "uly_juz_rular"
@app.get('/uly_juz/rular')
def get_uly_juz_rular():
    rular = uly_juz_rular_collection.find().sort('name')
    return {'rular': bson_to_json(rular)}


# Маршрут для создания новой записи в коллекции "uly_juz_taipalar"
@app.post('/uly_juz/taipalar')
def create_uly_juz_taipa(taipa: str):
    taipa_data = {'taipa': taipa}
    taipa_id = uly_juz_taipalar_collection.insert_one(taipa_data).inserted_id
    return {'taipa_id': str(taipa_id)}


# Маршрут для создания новой записи в коллекции "uly_juz_rular"
@app.post('/uly_juz/rular')
def create_uly_juz_rular(taipa_id: str, name: str, description: str, picture: str):
    rular_data = {
        'taipa_id': taipa_id,
        'name': name,
        'description': description,
        'picture': picture
    }
    rular_id = uly_juz_rular_collection.insert_one(rular_data).inserted_id
    return {'rular_id': str(rular_id)}


# Закрытие соединения с MongoDB при остановке сервера
@app.on_event('shutdown')
def shutdown_event():
    client.close()


# Функция для преобразования ObjectId в строковое представление
def bson_to_json(data):
    return json_util.dumps(data)


# Запуск сервера с использованием Uvicorn
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000)
