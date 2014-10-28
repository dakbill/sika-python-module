import requests, json

class User:
	

	def __init__(self, token):
		self.token = token
		self.host = 'http://127.0.0.1:8000'
		self.headers = {
					'Content-Type':'application/json',
					'Authorization': 'Token %s' % self.token
					}

	def create_user(self, name, phone, email, options = {}):
		body = options['body'] if 'body' in options else {}
		body['name'] = name
		body['phone'] = phone
		body['email'] = email
		headers = self.headers
		response = requests.post('%s/api/users/'% self.host, data=json.dumps(body), headers=headers)
		return response.json()
	

	def create_invoice(self, total, delivery_cost, ref, first_name, items, options = {}):
		body = options['body'] if 'body' in options else {}
		body['total'] = total
		body['delivery_cost'] = delivery_cost
		body['ref'] = ref
		body['first_name'] = first_name
		body['items'] = items
		headers = self.headers
		response = requests.post('%s/api/invoices/' % self.host, data=json.dumps(body), headers=headers)
		return response.json()

	def invoices(self):
		headers = self.headers
		response = requests.get('%s/api/invoices/' % self.host, headers=headers)
		return response.json()		

	def invoice_detail(self, ref):
		headers = self.headers
		response = requests.get('%s/api/invoices/%s' % (self.host,ref), headers=headers)
		return response.json()