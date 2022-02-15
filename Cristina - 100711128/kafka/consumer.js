// const {Kafka} = require("kafkajs")
const Kafka = require("kafkajs").Kafka

run();

async function run(){
    try{
        // Create kafka object
        const kafka = new Kafka({
            "clientId": "myapp",
            "brokers": ["localhost:9094"]
        })

        // Create consumer
        const consumer = kafka.consumer({"groupId": "test"});

        // Connect
        console.log("Connecting...")
        await consumer.connect()
        console.log("Connected!")
        
        consumer.subscribe({
            "topic": "Users",
            "fromBeginning": true
        })
        await consumer.run({
            "eachMessage": async result => {
                console.log(`Received message: ${result.message.value} on parition ${result.partition}`)
            }
        })
   
    }
    catch(ex){
        console.error(`Something bad happened ${ex}`)
    }
    finally{
        
    }
}
