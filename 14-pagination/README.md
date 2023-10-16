Mapeamento objeto-relacional de um subset de dados (https://www.kaggle.com/datasets/peopledatalabssf/free-7-million-company-dataset)

É preciso editar o arquivo csv para inserir um nome no primeiro campo, a fim de facilitar os trabalhos :-)

Extração de 1000 registros:
```
head -1000 companies_sorted.csv > companies_1000.csv
```

Importando os dados (https://stackoverflow.com/questions/14947916/import-csv-to-sqlite):

```
$ sqlite3 yourfile.sqlite
sqlite>  .mode csv
sqlite>  .import test.csv yourtable
sqlite>  .exit
```

Acessando parte dos registros (paginação):
https://stackoverflow.com/questions/20642497/sqlalchemy-query-to-return-only-n-results

