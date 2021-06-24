from transmission_rpc import Client
import get_ip
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def sheet_append(ipaddress, country):
    spreadsheetId = '19S_R8ifPqt29uiEx4G4hsTh3i5U1C_ny7SpbrMVltxo'  # Please set the Spreadsheet ID.

    json_key = 'sheets.json'
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_key, scope)
    gc = gspread.authorize(credentials)
    sh = gc.open_by_key(spreadsheetId)
    if sh.sheet1.findall(ipaddress, in_row=None, in_column=None):
        #print("Already exists: " + ipaddress)
        return
    print(ipaddress)
    sh.sheet1.append_row([ipaddress,country], table_range="A1")


clients = [Client(host='192.168.1.55', port=9092, username='supergonkas', password='portugal'),
           Client(protocol="https", host='aigaion.feralhosting.com', port=443, path="/supergonkas/transmission/rpc", username='supergonkas', password='9Q4zycfZfxtXnB8Q')]
for c in clients:
    print(c.session_stats)
    list_torrents = c.get_torrents()
    for i in list_torrents:
        peers_list = i.peers
        if peers_list:
            for peers in peers_list:
                ipaddress = peers["address"]
                #print(ipaddress)
                country = get_ip.main(ipaddress)
                if country:
                    sheet_append(ipaddress, country)

