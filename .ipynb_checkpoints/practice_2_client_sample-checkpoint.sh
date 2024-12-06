curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{
           "price_per_unit": 10,
           "unit_solds": 200,
           "operationg_profit": 1500
         }'