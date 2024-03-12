import json

a={
	"firstname" : "John",
	"lastname" : "Doe",
	"year" : 1979
}
b={
	"firstname" : "Bush",
	"lastname" : "Lom",
	"year" : 1978
}
data={
	"first":a,
	"second":b
}

json_str=json.dumps(data)
print(json_str)

data_out=json.loads(json_str)
print(data_out)

with open("data.json","w") as f:
	json.dump(data,f)

with open("data.json","r") as f:
	data_out=json.load(f)
	print(data_out)
