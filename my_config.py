import json

# Mevcut konfiqurasiya faylını yükleyin
with open('my_config.json', 'r') as file:
    config = json.load(file)

# 1. Müəllif haqqında məlumatı dəyişdirin
config['name'] = "Amil"
config['author'] = 'Mammadov'

# 2. Server üçün port məlumatını dəyişdirin
config['server'] = {
    'ports': 2024,
    'port2': 2025   
}

# 3. Brauzeri açmaq qabiliyyətini False-dən True-a dəyişdirin
config['openInBrowser'] = True

# 4. Şrift məlumatı əlavə edin
config['font'] = {
    'family': 'Arial',
    'size': 12,
    'style': 'normal'
}

# Yenilənmiş konfiqurasiya faylını yadda saxlayın
with open('my_config.json', 'w') as file:
    json.dump(config, file, indent=4)

print("Konfiqurasiya faylı uğurla yeniləndi.")
