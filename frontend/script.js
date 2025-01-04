const backendUrl = "https://your-backend-url.com/generate"; // Replace with your online backend URL

document.getElementById('generateBtn').addEventListener('click', async () => {
    const prompt = document.getElementById('prompt').value;
    const outputDiv = document.getElementById('output');
    outputDiv.innerHTML = "Generating image...";

    try {
        const response = await fetch(backendUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt }),
        });
        const data = await response.json();
        if (data.image_url) {
            outputDiv.innerHTML = `<img src="${data.image_url}" alt="Generated Image">`;
        } else {
            outputDiv.innerHTML = "Error: Unable to generate image.";
        }
    } catch (error) {
        outputDiv.innerHTML = "Error: Unable to connect to backend.";
    }
});
