// const {Kafka} = require("kafkajs")
const Kafka = require("kafkajs").Kafka
const msg = process.argv[2];
run();

async function run(){
    try{
        // Create kafka object
        const kafka = new Kafka({
            "clientId": "myapp",
            "brokers": ["localhost:9094"]
        })

        // Create producer
        const producer = kafka.producer();

        // Connect
        console.log("Connecting...")
        await producer.connect()
        console.log("Connected!")
        const partition = msg[0] < "N" ? 0 : 1;

        const result = await producer.send({
            "topic": "Users",
            "messages": [
                {
                    "value": msg,
                    "partition": partition
                }
            ]
        })

        console.log(`Send Successfully! ${JSON.stringify(result)}`)
        
        // Disconnect
        await producer.disconnect();
    }
    catch(ex){
        console.error(`Something bad happened ${ex}`)
    }
    finally{
        process.exit(0);
    }
}
