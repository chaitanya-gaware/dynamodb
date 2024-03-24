module "lambda_function" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = "test_dynamo"
  description   = "lambda to test dynamodb"
  handler       = "index.lambda_handler"
  runtime       = "python3.8"

  source_path = "${var.lambda_path}"

  tags = {
    Name = "lambda_for_dynamodb"
  }
}