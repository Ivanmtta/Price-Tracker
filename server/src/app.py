from flask import Flask, request, jsonify
from flask_pymongo import pymongo, ObjectId
from flask_cors import CORS
from web_scraper import Web_Scraper
from email_sender import Email_Sender
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import os

app = Flask(__name__)
CONNECTION_STRING = os.getenv('mongodb_connection_string')
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('price_tracker_db').items
scraper = Web_Scraper()
sender = Email_Sender()

cors = CORS(app)

def check_item_prices():
  items = []
  for item in db.find():
    items.append({
      '_id': str(ObjectId(item['_id'])),
      'name': item['name'],
      'image': item['image'],
      'original_price': float(item['original_price']),
      'current_price': float(item['current_price']),
      'url': item['url']
    })
  for item in items:
    new_price = scraper.update_price(item['url'], item['current_price'])
    if(new_price < item['current_price']):
      db.update_one({'_id': ObjectId(item['_id'])}, {"$set": {
        'current_price': new_price
      }})
  if(len(items) > 0):
    sender.send_email(items)
  print("Item prices updated")

@app.before_first_request
def initiate_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=check_item_prices, trigger="interval", hours=24)
    scheduler.start()
    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())

@app.route('/items', methods = ['POST'])
def create_item():
  item = scraper.get_item(request.json['url'])
  id = db.insert_one({
    'name': item['name'],
    'image': item['image'],
    'original_price': item['original_price'],
    'current_price': item['current_price'],
    'url': item['url']
  })
  return jsonify(str(id.inserted_id))

@app.route('/items', methods = ['GET'])
def get_users():
  items = []
  for item in db.find():
    items.append({
      '_id': str(ObjectId(item['_id'])),
      'name': item['name'],
      'image': item['image'],
      'original_price': float(item['original_price']),
      'current_price': float(item['current_price']),
      'url': item['url']
    })
  return jsonify(items)

@app.route('/delete/<id>', methods = ['DELETE'])
def delete_item(id):
  db.delete_one({'_id': ObjectId(id)})
  return jsonify({"response": "Item successfully deleted"})

if __name__ == '__main__':
  app.run()