from ocr import scan, validated_scan

input = (
    " _  _  _  _  _  _  _  _    \n"
    "| || || || || || || ||_   |\n"
    "|_||_||_||_||_||_||_| _|  |\n"
    "                           "
)

print(validated_scan(input))