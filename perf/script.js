import http from 'k6/http';
import { sleep } from 'k6';
import { htmlReport } from "https://raw.githubusercontent.com/benc-uk/k6-reporter/main/dist/bundle.js";

import { oneMessagePayload, threeMessagePayload, hundredMessagePayload } from './payloads.js';

export const options = {
    vus: 10,
    duration: '30s',
};

export default function () {
    http.post(
        `http://${__ENV.TARGET_HOST}/collect`,
        hundredMessagePayload,
        { headers: { 'Content-Type': 'application/json' } }
    );
    sleep(1);
}
