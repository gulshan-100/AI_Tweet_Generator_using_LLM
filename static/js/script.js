// Function to generate tweets
async function generateTweets() {
    // Show loading spinner and hide the output
    document.querySelector('.loading').style.display = 'block';
    document.querySelector('.output').style.display = 'none';

    try {
        // Fetch data from backend
        const response = await fetch('/generate_tweets', { method: 'GET' });
        const data = await response.json();
        
        // Hide loading spinner and show generated tweets
        document.querySelector('.loading').style.display = 'none';
        document.querySelector('.output').style.display = 'block';

        const tweetsList = document.getElementById('tweetsList');
        tweetsList.innerHTML = `
            <li><span>🚨</span>${data.tweet1} <button class="copy-btn" onclick="copyToClipboard('${data.tweet1}')">Copy</button></li>
            <li><span>📢</span>${data.tweet2} <button class="copy-btn" onclick="copyToClipboard('${data.tweet2}')">Copy</button></li>
            <li><span>💥</span>${data.tweet3} <button class="copy-btn" onclick="copyToClipboard('${data.tweet3}')">Copy</button></li>
            <li><span>🚀</span>${data.tweet4} <button class="copy-btn" onclick="copyToClipboard('${data.tweet4}')">Copy</button></li>
            <li><span>🔥</span>${data.tweet5} <button class="copy-btn" onclick="copyToClipboard('${data.tweet5}')">Copy</button></li>
        `;
    } catch (error) {
        document.querySelector('.loading').style.display = 'none';
        alert('Error generating tweets. Please try again!');
    }
}

// Function to copy tweet to clipboard
function copyToClipboard(tweet) {
    const textArea = document.createElement('textarea');
    textArea.value = tweet;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand('copy');
    document.body.removeChild(textArea);
    alert('Tweet copied to clipboard!');
}
