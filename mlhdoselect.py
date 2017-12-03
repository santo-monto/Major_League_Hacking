from clarifai import rest
from clarifai.rest import ClarifaiApp
import json
from clarifai.rest import Image as ClImage
flag=0
app = ClarifaiApp(api_key='cbd91ed9a3524abbb448f515d453517f')

model = app.models.get("general-v1.3")
hello = ClImage(file_obj=open('/home/santosh/hello1.jpg', 'rb'))
hello=model.predict([hello])
hello = json.dumps(hello)
hello1 = json.loads(hello)
#print(hello1)
string = ['happy','joy','worried','fun','serious']
#print(hello1['status'])
for i in hello1['outputs'][0]['data']['concepts']:
    for j in string :
        if(i['name']==j) :

            print(i['name'])
            print(i['value'])
            flag=1;
            break
    if(flag==1) :
        break
