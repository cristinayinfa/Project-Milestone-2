const {Kafka} = require("kafkajs")
const msg = process.argv[2];
run();
async function run(){ 
    try {
        const kafka = new Kafka({
            "clientID": "myapp",
            "brokers": ["localhost:9093", "localhost:9094", "localhost:9095"]
        })

        const producer = kafka.producer();
        console.log("Connecting..")
        await producer.connect()
        console.log("Connected!")
        const partition = msg[0] < "N" ? 0 : 1
        const result = await producer.send({
            "topic": "Users",
            "messages": [
                {
                    "value": msg,
                    "partition": partition
                }
            ]
        })
        console.log(`Sent message ${JSON.stringify(result)}`)
        await producer.disconnect();
    } catch (error) {
        console.error(`Error occured ${ex}`)
    }

    finally{
        process.exit();
    }
}