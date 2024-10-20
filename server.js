const { GoogleGenerativeAI } = require("@google/generative-ai");

// Load environment variables
require("dotenv").config();

// Access API key
const genAI = new GoogleGenerativeAI(process.env.API_KEY);
const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

// Example usage
const prompt = "Write a story about a magic backpack.";

async function generateContent() {
  try {
    const result = await model.generateContent(prompt);
    console.log(result.response.text);
  } catch (error) {
    console.error("Error generating content:", error);
  }
}

generateContent();
