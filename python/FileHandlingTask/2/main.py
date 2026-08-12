import re 
from redaction_config import SENSITIVE


with open("report.txt","r") as file:
        text= file.read()


titan_count = len(re.findall("Titan", text))
acme_count = len(re.findall("Acme Corp", text))

text = re.sub("Titan", "[REDACTED]", text)
text = re.sub("Acme Corp", "[REDACTED]", text)
print(text)
print("Titan replacements:", titan_count)
print("Acme Corp replacements:", acme_count)

with open("report_redacted.txt", "w") as file:
    file.write(text)