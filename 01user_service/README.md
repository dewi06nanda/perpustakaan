# User Service

User Service adalah layanan yang menyediakan data pengguna. Layanan ini bertindak sebagai **provider** untuk layanan lain seperti Book Service.

## Endpoint

### GET /users/<user_id>
Mengambil data user berdasarkan ID.

#### Contoh Request
GET http://localhost:5000/users/1


#### Contoh Response
```json
{
  "id": "1",
  "name": "Alice"
}
