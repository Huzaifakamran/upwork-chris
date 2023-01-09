from flask import Flask, request,jsonify
import requests
app = Flask(__name__)

@app.route('/webhook',methods = ['GET','POST'])
def webhook():
    data = request.get_json(silent=True)
    try:
        if data['queryResult']['intent']['displayName'] == 'details':
            res = details(data)
            return jsonify(res)
    except Exception as e:
        print('error main',e)

def details(data):
    print("In Function")
    try:
        print("In Function 2")
        event_id = data['queryResult']['parameters']['event_id']
        print(event_id)
        client_id = data['queryResult']['parameters']['client_id']
        action = data['queryResult']['parameters']['action']
        invoice_number = data['queryResult']['parameters']['invoice_number']
        created_date = data['queryResult']['parameters']['created_date'].split('T')[0]
        print(created_date)
        delivery_date = data['queryResult']['parameters']['delivery_date'].split('T')[0]
        pickup_date = data['queryResult']['parameters']['pickup_date'].split('T')[0]
        event_type = data['queryResult']['parameters']['event_type']
        contact_name = data['queryResult']['parameters']['contact_name']['name']
        contact_phone = data['queryResult']['parameters']['contact_phone']
        event_address = data['queryResult']['parameters']['event_address']
        event_suburb = data['queryResult']['parameters']['event_suburb']
        delivery_type = data['queryResult']['parameters']['delivery_type']
        start_time = data['queryResult']['parameters']['start_time'].split('T')[1].split('+')[0]
        finish_time = data['queryResult']['parameters']['finish_time'].split('T')[1].split('+')[0]
        delivery_time = data['queryResult']['parameters']['delivery_time'].split('T')[1].split('+')[0]
        pickup_time = data['queryResult']['parameters']['pickup_time'].split('T')[1].split('+')[0]
        referrer = data['queryResult']['parameters']['referrer']
        event_notes = data['queryResult']['parameters']['event_notes']
        print(event_notes)
        invoice_created = data['queryResult']['parameters']['invoice_created'].split('T')[0]
        print(invoice_created)
        requests.post(
        "https://sheet.best/api/sheets/6019d5ea-3192-4d8b-b08c-da4afa8435dc/tabs/Event",json={
            'EventID': str(event_id),
            'ClientID': str(client_id),
            'Action': action,
            'InvoiceNumber': str(invoice_number),
            'DateCreated':created_date,
            'DeliveryDate':delivery_date,
            'PickupDate':pickup_date,
            'EventType':event_type,
            'ContactName':contact_name,
            'ContactPhone':contact_phone,
            'EventAddress':event_address,
            'EventSuburb':event_suburb,
            'DeliveryType':delivery_type,
            'StartTime':start_time,
            'FinishTime':finish_time,
            'DeliveryTime':delivery_time,
            'PickupTime':pickup_time,
            'Referrer':referrer,
            'EventNotes':event_notes,
            'InvoiceCreated':invoice_created,
            # 'Extra':'TEST',
            # 'Travel':'TEST',
            # 'Supervision':'TEST',
            # 'EventDate':'TEST',
            # 'LastName':'TEST',
            # 'ConfirmationDone':'TEST',
            # 'Calendared':'TEST',
            # 'PowerConfirmed':'TEST',
            # 'FlatConfirmed':'TEST',
            # 'RainForecast':'TEST',
            # 'WindSpeed':'TEST',
            # 'ChrisNeedsAttention':'TEST',
            # 'PaymentMethod':'TEST',
            # 'Paid':'Paid',
            # 'Priority':'Priority',
            # 'InvoiceStatus':'st',
            # 'Status':'status',
            # 'InvoiceSentDate':'InvoiceSentDate',
            # 'ContactMethod':'ContactMethod',
            # 'InvoiceSent':'InvoiceSent',
            # 'EventStatus':'EventStatus',
            # 'HyperLinktest':'HyperLinktest',
            # 'EncodeURLTest':'EncodeURLTest',
            # 'InvoiceLink':'InvoiceLink',
            # 'InvoicePaidDate':'InvoicePaidDate'

        })
        reply = { 'fulfillmentText': "What is the extra?"}
    except Exception as e:
        print(e)
    return reply

if __name__ == '__main__':
    app.run()