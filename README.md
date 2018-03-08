# Postmortem

Base de documentação para o processo de postmortem de incidentes

## Execução de migrations de banco de dados

```
# criar as migrations de acordo com mudanças detectadas nos models
make makemigrations app

# verificar os SQLs de determinada migration
make sqlmigrate app name=<migration name>

# sincronizar o estado do banco de dados com as migrations criadas
python manage.py migrate
```

## Execução do servidor

```
make runserver
```

## Para desenvolvimento local, exportar as ENVs de credenciais para o DBaaS

```
export DBAAS_MYSQL_ENDPOINT='host do banco de dados'
export DBAAS_MYSQL_PASSWORD='xxxxxxx'
export DBAAS_MYSQL_USER='usuario do banco de dados'
```

## Dashboard da app no Tsuru

[Dashboard da app](http://tsuru-dashboard.cloud.globoi.com/apps/postmortem)

## Estáticos sob S3

[Container](http://vault.gcloud.globoi.com/storage/objects/postmortem/?p=f5233c83d9314ac397cd734f37371b7e)


### Tasklist

- [ ] Autenticação de usuários com LDAP
- [ ] Filtros na home principal pelo campo "produto"
- [ ] Busca para conteúdo de todos os campos
- [ ] HTTPS
- [ ] Status do incidente