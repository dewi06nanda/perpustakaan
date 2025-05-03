
## book_service/README.md

markdown
# Book Service

Book Service adalah layanan yang menangani data peminjaman buku. Service ini berfungsi sebagai **consumer** dari User Service dan **provider** data pinjaman.

## Endpoint

### POST /loans
Membuat data peminjaman baru.

#### Contoh Request
json
{
  "user_id": "1",
  "book_id": "b1"
}

