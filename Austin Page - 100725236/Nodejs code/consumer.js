const { Kafka } = require("kafkajs");

run();

async function run() {
  try {
    const kafka = new Kafka({
      brokers: ["localhost:9093"],
    });

    const consumer = kafka.consumer({ groupId: "test" });
    console.log("Connecting...");
    await consumer.connect();
    console.log("Connected!");

    consumer.subscribe({
      topic: "test",
      fromBeginning: true,
    });

    await consumer.run({
      eachMessage: async (result) => {
        console.log(
          "Received: " +
            result.message.value +
            " on partition: " +
            result.partition
        );
      },
    });
  } catch (err) {
    console.error("Error: " + err);
  }
}
