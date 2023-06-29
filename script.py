import json
from pymongo import MongoClient

# Подключение к MongoDB
client = MongoClient('mongodb://root:password@localhost:27017')

# Выбор базы данных
db = client['mydatabase']

# Коллекция "kishi_juz"
kishi_juz_collection = db['kishi_juz']

# Коллекция "orta_juz"
orta_juz_collection = db['orta_juz']

# Коллекция "uly_juz"
uly_juz_collection = db['uly_juz']

# Чтение JSON-файла
with open('data.json', 'r') as file:
    data = json.load(file)

# Обработка данных и сохранение в MongoDB
for category, category_data in data['updated_data'].items():
    # Создание коллекции для каждого juz
    juz_collection = None
    if category == 'kishi_juz':
        juz_collection = kishi_juz_collection
    elif category == 'orta_juz':
        juz_collection = orta_juz_collection
    elif category == 'uly_juz':
        juz_collection = uly_juz_collection

    if juz_collection is not None:
        # Создание коллекции "taipalar" и "rular" внутри каждого juz
        taipalar_collection = db[f"{category}_taipalar"]
        rular_collection = db[f"{category}_rular"]

        for taipa_data in category_data['taipalar']:
            # Вставка записи в коллекцию "taipalar"
            taipa_id = taipalar_collection.insert_one({'taipa': taipa_data['taipa']}).inserted_id

            # Вставка связанных записей в коллекцию "rular"
            for rular_data in taipa_data['rular']:
                rular_data['taipa_id'] = taipa_id
                rular_collection.insert_one(rular_data)

# Закрытие соединения с MongoDB
client.close()
