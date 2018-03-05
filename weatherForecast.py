# The purpose of this script is to retrive weather forecast information
# of 3 different cities and then send out SMS message in Chinese to my phone.
# With minor modification the script can handle different cities,
# English text message and other phone numbers. 

# Dependencies
import json
import requests
from mydata import OpenWeather_api_key, account_sid, auth_token, twilio_phone, receiving_phone
from twilio.rest import Client

# define a fuction to get weather forecast from OpenWeatherMap API
def get_5D_weather_forecast(city, country):
    base_url = 'http://api.openweathermap.org/data/2.5/forecast?'
    # Build query URL
    query_url = f"{base_url}appid={OpenWeather_api_key}&q={city},{country}&units=metric"
    # Get weather data
    weather_json = requests.get(query_url).json()
    # generate lists for message
    time = [weather_json['list'][i]['dt_txt'] for i in range(0, 40, 8)]
    weather = [weather_json['list'][i]['weather'][0]['main'] for i in range(0, 40, 8)]
    temp = [weather_json['list'][i]['main']['temp'] for i in range(0, 40, 8)]
    # generate message
    message = f'''
    {time[0]}
    天气：{weather[0]} 气温：{temp[0]}度
    {time[1]}
    天气：{weather[1]} 气温：{temp[1]}度
    {time[2]}
    天气：{weather[2]} 气温：{temp[2]}度
    {time[3]}
    天气：{weather[3]} 气温：{temp[3]}度
    {time[4]}
    天气：{weather[4]} 气温：{temp[4]}度
    '''
    return message

# define a fuction to send out SMS message
def send_SMS_message(to_phone_number, body):
    client = Client(account_sid, auth_token)
    client.api.account.messages.create(
        to=to_phone_number,
        from_=twilio_phone,
        body=body)

# get weather forecast for cities
Cities = [['chicago', 'us'], ['yichang', 'cn'], ['xuchang', 'cn']]
message = [get_5D_weather_forecast(city, country) for city, country in Cities]

# generate SMS message body
final_message = f'''------------
    芝加哥五天天气预报:{message[0]}
    ------------
    宜昌五天天气预报:{message[1]}
    ------------
    许昌五天天气预报:{message[2]}
    '''

# send out SMS message through Twilio
send_SMS_message(receiving_phone, final_message)