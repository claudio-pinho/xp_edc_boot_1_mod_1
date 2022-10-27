# instalar aws-cli
# configurar credenciais de acesso usando "aws configure" - buscar no AWS-IAM / user / security credentials

# instalar biblioteca boto3 - "pip install boto3"
import boto3
# instalar biblioteca pandas - "pip install pandas"
import pandas as pd

s3_client = boto3.client('s3')

s3_client.upload_file("C:\Essencial\EDC\Modulo_1\Pratica\ENEM\DADOS\ITENS_PROVA_2020.csv",
                      "datalake-claudio-edc",
                      "raw_data/itens_prova_2020.csv")

#s3_client.upload_file("C:\Essencial\EDC\Modulo_1\Pratica\ENEM\DADOS\MICRODADOS_ENEM_2020.csv",
#                      "datalake-claudio-edc",
#                      "raw_data/microdados_enem_2020.csv")

