from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/webhook',methods = ['GET','POST'])
def webhook():

    data = request.get_json(silent=True)
    if data['queryResult']['intent']['displayName'] == 'details':
        res = details(data)
        return jsonify(res)

def details(data):
    try:
        import requests
        invoice_number = data['queryResult']['parameters']['invoice_number']
        result = requests.post(
        "https://sheet.best/api/sheets/6019d5ea-3192-4d8b-b08c-da4afa8435dc/tabs/Event",json={
            'EventID': '10',
            'ClientID': 'Jack Doe',
            'Action': '97',
            'InvoiceNumber': invoice_number,
            'DateCreated':''
        },
    )
        result.json()
        reply = { 'fulfillmentText': "Matched"}

    except Exception as e:
        print(e)
    return reply

if __name__ == '__main__':
    app.run(debug=True)