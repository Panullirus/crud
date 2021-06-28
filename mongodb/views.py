from django.shortcuts import render
import pymongo
import dns

client = pymongo.MongoClient("mongodb+srv://m001-student:Pakito24@sandbox.cbqx4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
##x = {"db":"db"},{"col":"col"}
db = client['test']
col = db['test1']
subDelete = 0

def home(request):
    return render(request,'database/home.html',{"database":col.find({})})

def deleteUser(request):
    nombre = "daniel"
    dele = {"name":nombre}
    deleteobj = col.delete_one(dele)
    return render(request,'database/success.html', {"deleteObj":deleteobj})