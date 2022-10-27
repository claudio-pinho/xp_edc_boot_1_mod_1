resource "aws_s3_bucket" "datalake" {
#  bucket = "${var.base_bucket_name}-${var.ambiente}-${var.numero_conta}"
  bucket = "datalake-rais"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "datalake" {
  bucket = aws_s3_bucket.datalake.bucket
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
}

resource "aws_s3_bucket_acl" "datalake" {
  bucket = aws_s3_bucket.datalake.id
  acl    = "private"
}

#resource "aws_s3_object" "codigo_spark" {
#  bucket = aws_s3_bucket.datalake.id
#  key    = "emr-code/pyspark/import_enem_from_tf.py"
#  source = "../python/import_enem.py"
#  etag   = filemd5("../python/import_enem.py")
#}

resource "aws_s3_bucket_object" "object1" {
for_each = fileset("C:/Essencial/EDC/Modulo_1/Desafio/DADOS/", "*.txt")
bucket = aws_s3_bucket.datalake.id
key = each.value
source = "C:/Essencial/EDC/Modulo_1/Desafio/DADOS/${each.value}"
etag = filemd5("C:/Essencial/EDC/Modulo_1/Desafio/DADOS/${each.value}")
}

provider "aws" {
  region = "${var.aws_region}"
}