import psycopg2
import os
DATABASE_URL = os.environ['postgres://szlikxxxsncvyh:76df9a0905ef0ef2170da0ac7d9d5889c62f2e83d124f7b37febe03dda5cc376@ec2-54-228-209-117.eu-west-1.compute.amazonaws.com:5432/d2j7i18j7mu6q4']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')