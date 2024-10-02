import subprocess

for i in range(1550, 1561):
    url =  "https://theweekinchess.com/zips/twic"+str(i)+"g.zip"
    curl_command = ["curl", "-IO", url]
    result = subprocess.run(curl_command, capture_output=True, text=True)

