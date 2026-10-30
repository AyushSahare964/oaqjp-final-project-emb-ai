function RunSentimentAnalysis() {
    const text = document.getElementById("textToAnalyze").value;
    fetch("/emotionDetector?textToAnalyze=" + encodeURIComponent(text))
        .then(r => r.text())
        .then(t => { document.getElementById("system_response").innerHTML = t; });
}
