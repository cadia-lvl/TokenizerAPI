
LOC=/process/service
LOC=/tokenize

curl http://0.0.0.0:8080$LOC -H 'Content-Type: application/json' -d '{"type":"text", "content":"hæ"}'
echo

curl http://0.0.0.0:8080$LOC -H 'Content-Type: application/json' -d '{"type":"text", "content":"hæ, hvað seigir þú gott. Nei."}'
echo

echo "### Error ###"
TEST='{}'
curl http://0.0.0.0:8080$LOC -H 'Content-Type: application/json' -d $TEST
echo

curl http://0.0.0.0:8080$LOC -H 'Content-Type: application/json' -d ''
echo

curl http://0.0.0.0:8080$LOC -H 'Content-Type: application/json' -d 'lskdjflkj'
echo
