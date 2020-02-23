
# Running sample DjangoDocker application

Please follow delow steps

## DEV Environment Requirement
1. Python3
2. Pip3
3. Docker

## Application dev setup

```$xslt
git clone
cd DjangoDocker
pip3 -r requirement.txt
```

## Run application in dev
`python manage.py runserver`

OR 

`gunicorn DjangoDocker.wsgi:application  -b '[::]:8000'`


## Building docker
`sudo docker build -t my-django-web-services .`

## Running docker in Local DEV
`sudo docker run -p 8000:8000 --env ALLOWED_HOST=<YOUR_HOST_IP/HOSTNAME> -it my-django-web-services`

## Push docker to Docker Repository
```$xslt
sudo docker push <YOUR_REPO>/my-django-web-services:<TAG_NAME>
```
e.g
``` 
sudo docker push mahendra001/my-django-web-services:1.0 
```

## Running Docker in DEV Above
If exising docker container is running 
```$xslt
sudo docker stop ci_server
sudo docker rm ci_server
```
Start Latest Docker 
```$xslt
sudo docker pull my-django-web-services
sudo docker run -p 8000:8000 -d --name ci_server --env ALLOWED_HOST=<YOUR_HOST_IP/HOSTNAME> my-django-web-services
```


