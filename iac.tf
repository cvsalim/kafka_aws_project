#MSK
resource "aws_msk_cluster" "kafka_cluster" {
  cluster_name           = "kafka-finance-cluster"
  kafka_version         = "2.8.1"
  number_of_broker_nodes = 3
  broker_node_group_info {
    instance_type = "kafka.t3.small"
  }
}


#RDS Postgres
resource "aws_db_instance" "postgres" {
  engine            = "postgres"
  instance_class    = "db.t3.micro"
  allocated_storage = 20
  username         = "admin"
  password         = "password"
}


