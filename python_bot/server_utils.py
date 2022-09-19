import json

""" Function to retrieve data backend data from the JSON params file  """
def backend_params(field):
    f = open('params.json')
    params = json.loads(f.read())
    f.close()
    return params["backend"][field]

""" This should be self explanatory 😂😁 """
def get_req_field(request, field):
    return request.form.get(field)