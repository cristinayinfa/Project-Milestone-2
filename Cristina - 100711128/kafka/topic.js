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

        // Create admin
        const admin = kafka.admin();

        // Connect
        console.log("Connecting...")
        await admin.connect()
        console.log("Connected!")

        // Create a topic
        await admin.createTopics({
            "topics": [{
                "topic": "Users",
                "numPartitions": 2
            }]
        })
        console.log("Created Successfully!")
        
        // Disconnect
        await admin.disconnect();
    }
    catch(ex){
        console.error(`Something bad happened ${ex}`)
    }
    finally{
        process.exit(0);
    }
}
