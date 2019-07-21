# 👫👭👬**Friend Finder App: Django Based WebApp to help you find friends similar to you**


## **Inspiration**
Making new friends as an adult isn’t easy. It seems that everyone already has their friend group and they’re too busy to expand it. Simply meeting new people becomes increasingly rare. 
Luckily, making new friends doesn’t have to entail removing the headphones of strangers just to see if they’re good friendship material or not. This webapp helps users seek people who are similar to them in terms of personality traits and similar likes and dislikes.


## **Features**
- Real Time Application
- Sound Recording in background
- Decibel Measurement.
- Storage on Cloud(MQTT) to save user device memory
- Processing on cloud(Firebase)

## **Demo**
***Messages getting published to Cloud MQTT upon recording***

![alt text](https://github.com/Mphis/Decibel/blob/master/websocket.png)



***Data getting sent to Firebase from Cloud MQTT***

![alt text](https://github.com/Mphis/Decibel/blob/master/mqtt.png)




***Email sent as alert .. because decibel level is high***

![alt text](https://github.com/Mphis/Decibel/blob/master/email.png)

## **Usage/ Architecture**

- The user starts the Sound Recording with a button.
- The noise is processed in the app and the db levels are measured, along with getting the location.
- Measured db levels are sent to be stored on the MQTT cloud
- The db levels are categorized and sorted in Firebase.
- If the noise levels are hazardous for human-beings or other fauna, the concerned authorities will be notified.
- Notifications will be sent in the form of emails through firebase.

![alt text](https://github.com/Mphis/Decibel/blob/master/architecture.png)
