curl --location --request POST 'localhost:9000/user_management/signup' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=PNdu30nbwJyRBUvPRTdZb69HdBwDNimMU3HAyjvR2wtuHJFqHaLbNXX3M3eBrYyW' \
--data-raw '{
    "username": "hello",
    "first_name": "Test",
    "last_name": "R",
    "phone_number": "56600",
    "email": "test@gmail.com",
    "password": "456789834"
}'


curl --location --request POST 'localhost:9000/user_management/signup' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=PNdu30nbwJyRBUvPRTdZb69HdBwDNimMU3HAyjvR2wtuHJFqHaLbNXX3M3eBrYyW' \
--data-raw '{
    "username": "hello",
    "first_name": "Test",
    "last_name": "R",
    "password": "456789834"
}'