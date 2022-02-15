const { Kafka } = require("kafkajs");
const msg = process.argv[2];
run();

async function run() {
  try {
    const kafka = new Kafka({
      brokers: ["localhost:9093"],
    });

    const producer = kafka.producer();
    console.log("Connecting...");
    await producer.connect();
    console.log("Connected!");

    const result = await producer.send({
      topic: "test",
      messages: [
        {
          value: msg,
        },
      ],
    });

    console.log("Sent! : " + JSON.stringify(result));
    await producer.disconnect();
  } catch (err) {
    console.error("Error: " + err);
  } finally {
    process.exit(0);
  }
}
