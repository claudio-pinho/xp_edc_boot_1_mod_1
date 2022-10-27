# instalar aws-cli
# configurar credenciais de acesso usando "aws configure" - buscar no AWS-IAM / user / security credentials

# instalar biblioteca boto3 - "pip install boto3"
import boto3
# instalar biblioteca pandas - "pip install pandas"
import pandas as pd

s3_client = boto3.client('s3')

#s3_client.upload_file("C:\Essencial\EDC\Modulo_1\Desafio\DADOS\RAIS_VINC_PUB_CENTRO_OESTE.txt",
#                      "datalake-rais",
#                      "raw_data/rais_vinc_pub_centro_oeste.txt")

s3_client.upload_file("C:\Essencial\EDC\Modulo_1\Desafio\DADOS\RAIS_VINC_PUB_MG_ES_RJ.txt",
                      "datalake-rais",
                      "raw_data/rais_vinc_pub_mg_es_rj.txt")

s3_client.upload_file("C:\Essencial\EDC\Modulo_1\Desafio\DADOS\RAIS_VINC_PUB_NORDESTE.txt",
                      "datalake-rais",
                      "raw_data/rais_vinc_pub_nordeste.txt")

s3_client.upload_file("C:\Essencial\EDC\Modulo_1\Desafio\DADOS\RAIS_VINC_PUB_NORTE.txt",
                      "datalake-rais",
                      "raw_data/rais_vinc_pub_norte.txt")

s3_client.upload_file("C:\Essencial\EDC\Modulo_1\Desafio\DADOS\RAIS_VINC_PUB_SP.txt",
                      "datalake-rais",
                      "raw_data/rais_vinc_pub_sp.txt")

s3_client.upload_file("C:\Essencial\EDC\Modulo_1\Desafio\DADOS\RAIS_VINC_PUB_SUL.txt",
                      "datalake-rais",
                      "raw_data/rais_vinc_pub_sul.txt")
