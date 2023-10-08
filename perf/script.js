import http from 'k6/http';
import { sleep, check } from 'k6';

import { oneMessagePayload, threeMessagePayload, hundredMessagePayload } from './payloads.js';

export const options = {
    vus: 10,
    duration: '30s',
};

export default function () {
    const res = http.post(
        `http://${__ENV.TARGET_HOST}/collect`,
        hundredMessagePayload,
        { headers: { 'Content-Type': 'application/json' } }
    );
    check(res, {
        'is status 200': (r) => r.status === 200,
    });
}
