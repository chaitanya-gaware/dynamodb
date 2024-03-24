resource "aws_dynamodb_table" "critical_process" {
  name           = "critical_process"
  billing_mode   = "PROVISIONED"
  hash_key       = "source_system"
  range_key      = "file_name_time"
  read_capacity  = 1
  write_capacity = 1

  attribute {
    name = "source_system"
    type = "S"
  }

  attribute {
    name = "file_name_time"
    type = "S"
  }


}
