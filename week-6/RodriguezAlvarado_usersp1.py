"""
    Title: RodriguezAlvarado_usersp1.py
    Author: Zadkiel Rodriguez Alvarado
    Date: 02/12/2024
    Description: Python with MongoDB Part 1
    Sources:
        https://learn-us-east-1-prod-fleet01-xythos.content.blackboardcdn.com/blackboard.learn.xythos.prod/5a31d48b683a8/23683848?X-Blackboard-S3-Bucket=blackboard.learn.xythos.prod&X-Blackboard-Expiration=1707771600000&X-Blackboard-Signature=yz11PxbARg%2FhJv%2BoVnBOuUjFMecBUm9jfKvA28Koxss%3D&X-Blackboard-Client-Id=100225&X-Blackboard-S3-Region=us-east-1&response-cache-control=private%2C%20max-age%3D21600&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27WEB%2520335%2520Python%2520Guide.pdf&response-content-type=application%2Fpdf&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQDLYUrqSS4SIlBJljQlS0eCL6LF%2BdtjdnfIyEGK13KJqwIhANL0sC2iE0WzxEXt2MbIifig9M4eqp76vkKowmo0ucsXKrMFCGIQABoMNTU2OTAzODYxMzYxIgxiR%2BtSJ5mlzU2o6ecqkAXBo2RyakkFHgvlBRPit4%2BxjOMlNG6YDtzH%2FOD%2BrWr%2FtLqjp%2F%2FnpqNj%2FYikIQwlGvh8fixVMoim%2BU2mfzq0f8MzJwNE9MjvVBujTSMWDLQSZSyUDCz4NJpTo9l%2B7Md6y25S0k%2F3R00XAyMLG2q1GvgTmTdJ62hhnPXN5vU2qsitkb4%2B5RIWfYGCQbLsCWkMb%2FHQJH2HjfD%2B7xfTDHvDUDpanT1BC8jMijV17nmelZ6K5K%2F2E4097KbCc5jkIkCVrLWdXK%2BUrhZY%2BCEQVQClj1UQMN43sb2bmzqzaYorafLqBkFVrVcVXlxEV99ND5Z%2FXLONfB6Lp6iy%2Bbme60KmRtJI4lkL1Ivsftdil0FJ6EI8oZfOfGEa0Kfq%2BWsQgki3KPO5wH1lFqt%2BNosIctw0XUqsXrVnuQmnT6wFiTF6PVxLRH20vUZ%2FaEw%2Fcr5rybRp%2F7eElVKm%2Fxd22CTko4GXuod1LbRsB7Ra7tVwpKjKCHjUe7LyCOjsBMbL9SSckCSrlN5ypuIEoXKTfbTAHXUdJeiqs0QKgGcLel8%2BsbuiAyhQG%2FiAWIMeYLXhk991%2BjeupA3%2FOTLLK4Afz4xYQFk7oQqPHWa1KxOTSA44JkB48wsvjzmcnRVYFJuB5i7IrsbXVq1RPdo2gy1hLbrFNxy0NdtxFPHKi8UtvSlFyPfGJvlVGPxXv9c8eijGqtmxdXtwcJanqxus%2BIiv9u87WdnK4sWH02BRi09XEFdeJ1Y3jFDB3Wr3B3sHbCMoMMLLDaz%2BH6YDxrfx6UNn1MErQBspn5AMuQXswxqFbOIkqmk26L5omg4%2FXZqQKeQKq3nDKFQvw%2B1KWi223qc2Gb3Ia8Yrh17EKk6Vgno13dxB1g%2BtOV4RZzCTkqmuBjqwAaREwbUEYTLV04OQVyvuxiOfHfxo3Nffctfp7Fkumn3EJokJf4EQGQcyZZ7oK9AKTOA%2BmSq5nu4BFLsxzKuwyZsVPoKO8OUJfV0k552ThX%2B4TBM1L8D0iRJzuF4gphHUexbVz1Jqv11jr%2BDdcEWdSKFey0sd0Oklf8n4NZRMZ2Ud%2BE7vag6kFR3pv9QQV29mv0j%2FRJ7OWRibiq42r4J4ZDZJl5uWZa944yqOE8Z5t8WI&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240212T150000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=ASIAYDKQORRYUS3SY6XR%2F20240212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=3dd3088c3886975edb664a81182ab986dbbc7bb50f945656c0d0f90b506267aa
        https://stackoverflow.com/questions/42463866/how-to-use-pip-with-visual-studio-code  
"""
# Import the MongoClient
from pymongo import MongoClient

# Build the connection string
client = MongoClient("mongodb+srv://web335_user:s3cret@web335db.rjmblap.mongodb.net/web335DB")

# Configure a variable to access the web335DB
db = client["web335DB"]

# Display all documents in the user's collection
for user in db.users.find({}):
    print(user)

# Display a document where the employeeId is 1011
print(db.users.find_one({"employeeId": "1011"}))

# Display a document where the lastName is Mozart
print(db.users.find_one({"lastName": "Mozart"}))