const express = require('express');
const client = require('prom-client');


const app = express();
const collectDefaultMetrics = client.collectDefaultMetrics;
collectDefaultMetrics({ timeout: 5000 });


const httpRequestDurationMicroseconds = new client.Histogram({
    name: 'http_request_duration_ms',
    help: 'Duration of HTTP requests in ms',
    labelNames: ['method', 'route', 'code'],
    buckets: [50, 100, 200, 300, 500, 1000]
});


app.get('/', (req, res) => {
    const end = httpRequestDurationMicroseconds.startTimer();
    res.send('Hello from sample microservice!');
    end({ method: req.method, route: '/', code: 200 });
});


app.get('/health', (req, res) => res.json({ status: 'ok' }));
app.get('/metrics', async (req, res) => {
    res.set('Content-Type', client.register.contentType);
    res.end(await client.register.metrics());
});


const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Server listening on ${port}`));