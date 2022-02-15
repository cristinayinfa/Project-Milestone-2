// const Kafka = require("kafkajs").Kafka
const {Kafka} = require("kafkajs")
run()
async function run(){
    try{
        const kafka = new Kafka({
            "clientId":"myapp",
            "brokers":["localhost:9093"]
        })

        const admin = kafka.admin();
        console.log("Connecting...")
        await admin.connect()
        console.log("Connected!")
        await admin.createTopics({
            "topics": [{
                "topic": "Users",
                "numPartitions": 2
            }]
        })
        console.log("Created Successfully!")
        await admin.disconnect()
    }
    catch(ex){
        console.error(`something bad happened ${ex}`)
    }
    finally{
        process.exit()
    }
}