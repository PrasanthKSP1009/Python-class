import json
data = {
    "Name":"RAMPeX",
    "Training":"Python with DS"
}
with open("jsonData.json","w") as f:
    json.dump(data, f, indent=2)