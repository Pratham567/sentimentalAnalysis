# This script sends an HTTP request using curl command to get the response
# The token used here is pubic token so it has no expiration
curl --data '{"data": ["This is a great tool!"]}' \
-H "Authorization:Token 7eda867d9f75c6dc1379a9798af8bb47d993ffaa" \
-H "Content-Type: application/json" \
-D - \
"https://api.monkeylearn.com/v3/classifiers/cl_pi3C7JiL/classify/"