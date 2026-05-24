let API_URL = '/api/v1';

if (import.meta.env.DEV) {
  API_URL = 'http://localhost:8000';
}

export default API_URL;
