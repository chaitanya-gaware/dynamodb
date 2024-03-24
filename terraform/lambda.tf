# module "lambda_function" {
#   source = "terraform-aws-modules/lambda/aws"

#   function_name = "test_dynamo"
#   description   = "lambda to test dynamodb"
#   handler       = "index.lambda_handler"
#   runtime       = "python3.8"

#   source_path = "${var.lambda_path}"

#   tags = {
#     Name = "lambda_for_dynamodb"
#   }
# }
resource "aws_lambda_function" "example_lambda" {
  function_name = "example_lambda_function"
  handler       = "index.handler"
  runtime       = "nodejs14.x"
  filename      = "lambda_function.zip"  # Path to your Lambda function code ZIP file
  source_code_hash = filebase64sha256("lambda_function.zip")

  role = aws_iam_role.lambda_exec.arn  # IAM role ARN for Lambda execution

  # Additional configurations (optional)
  environment {
    variables = {
      ENV_VAR_NAME = "value"
    }
  }

  tags = {
    Name = "Example Lambda Function"
  }
}

# IAM Role for Lambda Execution
resource "aws_iam_role" "lambda_exec" {
  name = "lambda_exec_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect    = "Allow",
      Principal = {
        Service = "lambda.amazonaws.com"
      },
      Action    = "sts:AssumeRole"
    }]
  })

  tags = {
    Name = "Lambda Execution Role"
  }
}

# IAM Policy Attachment for Lambda Execution Role
resource "aws_iam_policy_attachment" "lambda_exec_attach" {
  name       = "lambda_exec_attach"
  roles      = [aws_iam_role.lambda_exec.name]
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}