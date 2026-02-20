# badelivery
Aplicação de Delivery e Produção da Biano Gourmet

## CRIAÇÃO NO SERVIDOR

### 1. Atualizar SO e instalar pacote:
sudo apt update <BR>
sudo apt upgrade <BR>
sudo apt install python3 python3-pip python3-venv git nginx <BR>
### 2. Django Project
cd /var/www/html <BR>
mkdir baproject <BR>
cd baproject <BR>
sudo git clone https://github.com/marcobutzke/badelivery.git <BR>
### 3. Ambiente Virtual
sudo python3 -m venv venv <BR>
source venv/bin/activate <BR>
pip install -r requirements.txt <BR>
pip install psycopg2-binary <BR>
pip install gunicorn <BR>
cd badelivery <BR>
python3 manage.py migrate <BR>
python3 manage.py collectstatic <BR>
python3 manage.py runserver 0.0.0.0:8000 <BR>
deactivate

###4. Confgurações de pastas

cd /var <BR>
sudo chown -R $USER:www-data www/ <BR>

### 5. Gunicorn

source venv/bin/activate <BR>
which guvicorn  --> /var/www/html/baproject/venv/bin/gunicorn <BR>
deactivate <BR>

cd /
sudo nano /etc/systemd/system/gunicorn.service

[Unit] <BR>
Description=Gunicorn <BR>
After=network.target <BR>

[Service] <BR>
User=www-data <BR>
Group=www-data <BR>
WorkingDirectory=/var/www/html/baproject/badelivery <BR>
ExecStart=/var/www/html/baproject/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:8000 produção.wsgi:application

[Install] <BR>
WantedBy=multi.user.target <BR>

sudo systemctl enable gunicorn <BR>
sudo systemctl start gunicorn  <BR>
sudo systemctl status gunicorn <BR>

### 6. nginx

cd / <BR>
sudo nano /etc/nginx/sites-available/baproject <BR>

server {
    listen 80;
    server_name 31.97.244.5;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme
    }

    location /static/ {
        alias /var/www/html/baproject/badelivery/staticfiles/;
    }
}

sudo ln -s /etc/nginx/sites-available/x500x /etc/nginx/sites-enabled/ <BR>
sudo systemctl restart nginx <BR>
sudo systemctl status nginx <BR>

### 7. Dominio:



### 8. SSL:

sudo apt update <BR>
sudo apt install python3 python3-venv libaugeas0 <BR>

sudo python3 -m venv /opt/certbot/ <BR>
sudo /opt/certbot/bin/pip install --upgrade pip <BR>
sudo /opt/certbot/bin/pip install certbot certbot-nginx <BR>
sudo ln -s /opt/certbot/bin/certbot /usr/bin/certbot <BR>
sudo certbot --nginx <BR>
echo "0 0,12 * * * root /opt/certbot/bin/python -c 'import random; import time; time.sleep(random.random() * 3600)' && sudo certbot renew -q" | sudo tee -a /etc/crontab > /dev/null <BR>

## Atualizar Sevidor

### 1. Supabase:

rodar os scripts para atualizao banco de dados

### 2. Projeto:

settings.py <BR>
DEBUG=False <BR>
setar o banco do servidor <BR>

gerar requirements.txt -> pip freeze > requirements.txt <BR>
retirar a linha do psycopg <BR>

subir GitHub <BR>
git add . <BR>
git commit -m "mensagem" <BR>
git push

### 3. Hostinger Terminal

cd /var/www/html/baproject/badelivery <BR>
git pull <BR>
cd .. <BR>
source venv/bin/activate <BR>
pip install -r requiments.txt <BR>
cd badelivery <BR>
python3 manage.py migrate <BR>
python3 manage.py collectstatic <BR>
python3 manage.py runserver 0.0.0.0:8000 <BR>
deactivate <BR>

systemctl status gunicorn <BR>
systemctl stop gunicorn <BR>
systemctl enable gunicorn <BR>
systemctl start gunicorn <BR>
systemctl status gunicorn <BR>

systemctl restart nginx <BR>
systemctl status nginx <BR>

OBS: se precisar ainda reiniciar VPS ou systemctl daemon-load

