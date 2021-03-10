curl --location --request POST 'localhost:9000/user_management/login' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=PNdu30nbwJyRBUvPRTdZb69HdBwDNimMU3HAyjvR2wtuHJFqHaLbNXX3M3eBrYyW' \
--data-raw '{
    "username": "hello",
    "password": "456789834"
}'
