resource "aws_dynamodb_table" "non_critical_process" {
  name           = "non_critical_process"
  billing_mode   = "PROVISIONED" 
  read_capacity  = 1
  write_capacity = 1
  hash_key       = "source_system"
  range_key      = "file_name_time"

  attribute {
    name = "source_system"
    type = "S"
  }

  attribute {
    name = "file_name_time"
    type = "S"
  }

}
