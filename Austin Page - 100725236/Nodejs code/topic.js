const { Kafka } = require("kafkajs");

run();

async function run() {
  try {
    const kafka = new Kafka({
      brokers: ["localhost:9093"],
    });

    const admin = kafka.admin();
    console.log("Connecting...");
    await admin.connect();
    console.log("Connected!");
    await admin.createTopics({
      topics: [
        {
          topic: "test",
          numPartitions: 2,
        },
      ],
    });
    console.log("Created!");
    await admin.disconnect();
  } catch (err) {
    console.error("Error: " + err);
  } finally {
    process.exit(0);
  }
}
