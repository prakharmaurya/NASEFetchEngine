def filter(db, symbol, data):
    collection = db[symbol]
    try:
        lastDoc = collection.find({}).sort([('_id', -1)]).limit(1)
    except Exception as e:
        print("Error in data fetch "+e)
        return

    try:
        lastDoc = list(lastDoc)
        if(len(lastDoc)):
            if(lastDoc[0]['timestamp'] == data['records']['timestamp']):
                print('No new data')
                return
    except Exception as e:
        print("last Doc key error "+e)
        return

    if(data != {}):
        dataArray = []
        try:
            for doc in data['filtered']["data"]:
                if(doc != {}):
                    data_dict = {}
                    data_dict.update({'strikePrice': doc['strikePrice']})
                    data_dict.update({'expiryDate': doc['expiryDate']})
                    if(doc.get("PE")):
                        data_dict.update({"PE": {
                            "strikePrice": doc["PE"]["strikePrice"],
                            "expiryDate": doc["PE"]["expiryDate"],
                            "openInterest": doc["PE"]["openInterest"],
                            "changeinOpenInterest": doc["PE"]["changeinOpenInterest"],
                            "pchangeinOpenInterest": doc["PE"]["pchangeinOpenInterest"],
                            "totalTradedVolume": doc["PE"]["totalTradedVolume"],
                            "impliedVolatility": doc["PE"]["impliedVolatility"],
                            "lastPrice": doc["PE"]["lastPrice"],
                            "change": doc["PE"]["change"],
                            "pChange": doc["PE"]["pChange"],
                            "totalBuyQuantity": doc["PE"]["totalBuyQuantity"],
                            "totalSellQuantity": doc["PE"]["totalSellQuantity"]
                        }})

                    if(doc.get("CE")):
                        data_dict.update({"CE": {
                            "strikePrice": doc["CE"]["strikePrice"],
                            "expiryDate": doc["CE"]["expiryDate"],
                            "openInterest": doc["CE"]["openInterest"],
                            "changeinOpenInterest": doc["CE"]["changeinOpenInterest"],
                            "pchangeinOpenInterest": doc["CE"]["pchangeinOpenInterest"],
                            "totalTradedVolume": doc["CE"]["totalTradedVolume"],
                            "impliedVolatility": doc["CE"]["impliedVolatility"],
                            "lastPrice": doc["CE"]["lastPrice"],
                            "change": doc["CE"]["change"],
                            "pChange": doc["CE"]["pChange"],
                            "totalBuyQuantity": doc["CE"]["totalBuyQuantity"],
                            "totalSellQuantity": doc["CE"]["totalSellQuantity"]
                        }})
                    dataArray.append(data_dict)
        except Exception as e:
            print('Creating new obj exception ' + e)
            return

        try:
            collection.insert_one({
                'timestamp': data['records']['timestamp'],
                'expiryDates': data['records']['expiryDates'],
                'underlyingValue': data['records']['underlyingValue'],
                'CE': data['filtered']["CE"],
                'PE': data['filtered']["PE"],
                'data': dataArray
            })
        except Exception as e:
            print("Error at inserting data "+e)
            return
